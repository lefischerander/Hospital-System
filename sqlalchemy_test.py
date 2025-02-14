import sqlalchemy as sa
import pandas as pd

MACHINE = "DESKTOP-LEANDER"
DB = "LANK_TEMP"
USER = "LANK_USER"
PASSWORD = "Lank1."

connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={MACHINE};DATABASE={DB};UID={USER};PWD={PASSWORD};TrustServerCertificate=YES"
connection_url = sa.URL.create(
    "mssql+pyodbc", query={"odbc_connect": connection_string}
)
engine = sa.create_engine(connection_url)

with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("SELECT subject_id, gender FROM PATIENTS"), conn)

print(df)
