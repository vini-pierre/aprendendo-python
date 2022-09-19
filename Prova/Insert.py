import sqlite3
import datetime

conn = sqlite3.connect('prova.db')

cursor = conn.cursor()

Name = input('Digite o nome: ')
LastName = input('Digite o último nome: ')

PatientID = int(input('Digite o ID do Paciente: '))
VaccineName = input('Digite o nome da vacina: ')
DoseData = datetime.datetime.now()
DoseNumber = int(input('Digite o número de doses: '))
VaccineType = input('Digite o tipo de vacina: ')

cursor.execute('INSERT INTO Patient (Name, LastName) VALUES (?,?)', (Name,LastName))
cursor.execute('INSERT INTO Vaccine (PatientID, VaccineName, DoseData, DoseNumber, VaccineType) VALUES (?,?,?,?,?)', (PatientID,VaccineName,DoseData,DoseNumber,VaccineType))

conn.commit()

conn.close()