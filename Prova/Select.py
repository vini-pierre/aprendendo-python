import sqlite3

conn = sqlite3.connect('prova.db')

cursor = conn.cursor()

cursor.execute("""
SELECT * FROM 
Patient INNER JOIN Vaccine ON
(Patient.PatientID = Vaccine.PatientID)
""")

for linha in cursor.fetchall():
    print(linha)

conn.commit()

conn.close()