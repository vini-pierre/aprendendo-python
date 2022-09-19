import sqlite3

conn = sqlite3.connect('prova.db')

cursor = conn.cursor()

#Delete Patient
cursor.execute('DELETE FROM Patient WHERE PatientID = 1')

#Delete Vaccine
cursor.execute('DELETE FROM Vaccine WHERE VaccineID = 1')

conn.commit()

conn.close()