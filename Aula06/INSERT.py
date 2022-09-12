import sqlite3

conn = sqlite3.connect('espm4s.db')

cursor = conn.cursor()

nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))

cursor.execute('INSERT INTO tb_pessoas (nome,idade) VALUES (?,?)', (nome, idade))

print('linha criada')

conn.commit()

conn.close()