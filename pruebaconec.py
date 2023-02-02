import pyodbc

SERVER = '3420-KOSORIO\SQLEXPRESS'
DATABAESE = 'Control_Asistencia'
USERNAME = 'sa'
PASSWORD = '1234'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      SERVER+';DATABASE='+DATABAESE+';UID='+USERNAME+';PWD=' + PASSWORD)

cursor = cnxn.cursor()

cursor.execute("SELECT * FROM BSC_PAIS")

row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()
