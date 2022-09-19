import sqlite3

conn = sqlite3.connect('prova.db')

cursor = conn.cursor()

#Patient
PatientID = int(input('Digite o número do ID do paciente: '))
Name = input('Digite o novo nome: ')

cursor.execute('UPDATE Patient SET Name = ? WHERE PatientID = ?', (Name,PatientID))

#Vaccine
VaccineID = int(input('Digite o número do ID da vacina: '))
VaccineName = input('Digite o novo nome da vacina: ')

cursor.execute('UPDATE Vaccine SET VaccineName = ? WHERE VaccineID = ?', (VaccineName,VaccineID))

conn.commit()

conn.close()