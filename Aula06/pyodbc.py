import pyodbc

server = 'dlapoio.database.windows.net'
database = 'masterUber'
username = 'andre'
password = 'ShC12%Uz'
driver = 'SQL Server'

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)

cursor = cnxn.cursor()

cursor.execute('SELECT * FROM tb_pessoas')

for linha in cursor.fetchall():
    print(linha)