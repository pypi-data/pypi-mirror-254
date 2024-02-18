"""Module containing services needed for executing queries with Duckdb + Iceberg."""

import re
from typing import Optional

import duckdb
from pyarrow.lib import RecordBatchReader
from pyiceberg.catalog import Catalog, load_catalog, load_rest
from pyiceberg.expressions import AlwaysTrue

from duckberg.exceptions import TableNotInCatalogException
from duckberg.sqlparser import DuckBergSQLParser
from duckberg.table import DuckBergTable, TableWithAlias

BATCH_SIZE_ROWS = 1024
DEFAULT_MEM_LIMIT = "1GB"
DEFAULT_DB_THREAD_LIMIT = 1
DEFAULT_CATALOG_NAME = "default"


class DuckBerg:
    """The query engine for easy querying Iceberg data through DuckDb.

    Args:
        catalog_name: The name of the catalog.
        catalog_config: The catalog config that is used for PyIceberg init.
        database_names: The list of database names that are used to filter just databases we need.
        table_names: The list of table names that are planned to be used. This list is useful to filter out the tables
            that are not Iceberg tables.
    """

    def __init__(
        self,
        catalog_name: str,
        catalog_config: dict[str, str],
        database_names: list[str],
        table_names: Optional[list[str]] = None,
        duckdb_connection: duckdb.DuckDBPyConnection = None,
        db_thread_limit: Optional[int] = DEFAULT_DB_THREAD_LIMIT,
        db_mem_limit: Optional[str] = DEFAULT_MEM_LIMIT,
        batch_size_rows: Optional[int] = BATCH_SIZE_ROWS,
    ):
        self.db_thread_limit = db_thread_limit
        self.db_mem_limit = db_mem_limit
        self.batch_size_rows = batch_size_rows
        self.duckdb_connection = duckdb_connection

        if self.duckdb_connection is None:
            self.duckdb_connection = duckdb.connect()
            self.__init_duckdb()

        self.sql_parser = DuckBergSQLParser()
        self.tables: dict[str, DuckBergTable] = {}

        self.__init_duckdb()
        self.__init_tables(catalog_config, catalog_name, database_names, table_names)

    def __init_duckdb(self):
        self.duckdb_connection.execute(f"SET memory_limit='{self.db_mem_limit}'")
        self.duckdb_connection.execute(f"SET threads TO {self.db_thread_limit}")

    def __init_tables(self, catalog_config, catalog_name, database_names, table_names):
        self.tables = {}

        catalog: Catalog = load_catalog(catalog_name, **catalog_config)

        namespaces = catalog.list_namespaces()
        namespaces = [i for i in namespaces if i[0] in database_names]

        tables = {}
        for n in namespaces:
            tables_list = catalog.list_tables(n)
            if table_names:
                tables_list = [t for t in tables_list if t[1] in table_names]
            tables: dict[str, DuckBergTable] = {
                ".".join(t): DuckBergTable.from_pyiceberg_table(catalog.load_table(t)) for t in tables_list
            }
            self.tables = self.tables | tables

    def list_tables(self):
        return list(self.tables.keys())

    def list_partitions(self, table: str):
        t = self.tables[table]

        if t.partitions is None:
            t.precomp_partitions()

        return t.partitions

    def select(
        self, sql: str, table: str = None, partition_filter: str = None, sql_params: [str] = None
    ) -> RecordBatchReader:
        if table is not None and partition_filter is not None:
            return self._select_old(sql, table, partition_filter, sql_params)

        parsed_sql = self.sql_parser.parse_first_query(sql)
        extracted_tables = self.sql_parser.extract_tables(parsed_sql)

        table: TableWithAlias
        for table in extracted_tables:
            table_name = table.table_name

            if table_name not in self.tables:
                raise TableNotInCatalogException

            row_filter = AlwaysTrue()
            if table.comparisons is not None:
                row_filter = table.comparisons

            table_data_scan_as_arrow = self.tables[table_name].scan(row_filter=row_filter).to_arrow()
            self.duckdb_connection.register(table_name, table_data_scan_as_arrow)

        if sql_params is None:
            return self.duckdb_connection.execute(sql).fetch_record_batch(self.batch_size_rows)
        else:
            return self.duckdb_connection.execute(sql, parameters=sql_params).fetch_record_batch(self.batch_size_rows)

    def _select_old(self, sql: str, table: str, partition_filter: str, sql_params: [str] = None):
        table_data_scan_as_arrow = self.tables[table].scan(row_filter=partition_filter).to_arrow()
        self.duckdb_connection.register(table, table_data_scan_as_arrow)

        if sql_params is None:
            return self.duckdb_connection.execute(sql).fetch_record_batch(self.batch_size_rows)
        else:
            return self.duckdb_connection.execute(sql, parameters=sql_params).fetch_record_batch(self.batch_size_rows)
