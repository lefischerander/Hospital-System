import names
import pyodbc

DRIVER = '{ODBC Driver 18 for SQL Server}'
SERVER = 'DESKTOP-HCFNQVT'
DATABASE = 'LANK'
USERNAME = 'LANK_USER'
PASSWORD = 'Lank1.'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-CC0D63;DATABASE=LANK;UID=LANK_USER;PWD=Lank1.;TrustServerCertificate=YES')

cursor = conn.cursor()

for i in range(101):
    cursor.execute("update A set firstname=?, surname =? from (select subject_id, firstname, surname, ROW_NUMBER() over (order by subject_id) rn from dbo.patients) A where rn = ?", names.get_first_name(), names.get_last_name(), i)

cursor.commit()