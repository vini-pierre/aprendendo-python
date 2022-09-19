import sqlite3

conn = sqlite3.connect('prova.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Patient(
    PatientID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    LastName TEXT NOT NULL
)
""")   

cursor.execute("""
CREATE TABLE IF NOT EXISTS Vaccine(
    VaccineID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    PatientID INTEGER NOT NULL,
    VaccineName TEXT NOT NULL,
    DoseData DATATIME NOT NULL,
    DoseNumber INTEGER NOT NULL,
    VaccineType TEXT NOT NULL,
    FOREIGN KEY (PatientID) REFERENCES Patient
)
""")

conn.commit()

conn.close()