import sqlite3
import datetime

conn = sqlite3.connect('exercicio01.db')

cursor = conn.cursor()


Name = input('Digite o nome: ')
Title = input('Digite o titulo: ')
Data = datetime.datetime.now()

cursor.execute('INSERT INTO Author (Name) VALUES (?)', (Name,))
cursor.execute('INSERT INTO Post (AuthorID, Title, Created) VALUES (?,?,?)', (1,Title,Data))


conn.commit()

conn.close()