import os

from duckberg import DuckBerg

os.environ["AWS_DEFAULT_REGION"] = ""
os.environ["AWS_ACCESS_KEY_ID"] = ""
os.environ["AWS_SECRET_ACCESS_KEY"] = ""
os.environ["AWS_SESSION_TOKEN"] = ""

MINIO_URI = "http://localhost:9000/"
MINIO_USER = "admin"
MINIO_PASSWORD = "password"

catalog_config: dict[str, str] = {
    "type": "glue",
}

catalog_name = "default"

db = DuckBerg(
    catalog_name=catalog_name,
    catalog_config=catalog_config,
    database_names=["slido_iceberg"],
    table_names=["datapi_questions_iceberg"]
)

tables = db.list_tables()

# New way of quering data without partition filter
query: str = "SELECT * FROM 'slido_iceberg.datapi_questions_iceberg'"
df = db.select(
    sql=query,
    table="slido_iceberg.datapi_questions_iceberg",
    partition_filter="organization_id = '4ad6a753-3252-49bd-9f5d-adaa150ad58a'",
).read_pandas()

print(len(df))

query = "SELECT * FROM 'slido_iceberg.datapi_questions_iceberg' WHERE organization_id='4ad6a753-3252-49bd-9f5d-adaa150ad58a'"
df = db.select(sql=query).read_pandas()
df.head(10)
print(len(df))