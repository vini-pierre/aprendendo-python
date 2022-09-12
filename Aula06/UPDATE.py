import sqlite3

conn = sqlite3.connect('espm4s.db')

cursor = conn.cursor()

cursor.execute('UPDATE tb_pessoas SET nome = ? WHERE id = ?', ('Vini Pierre', 1))

print('update efetuado com sucesso')

conn.commit()

conn.close()