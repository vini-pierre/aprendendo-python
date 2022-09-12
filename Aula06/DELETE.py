import sqlite3

conn = sqlite3.connect('espm4s.db')

cursor = conn.cursor()

cursor.execute('DELETE FROM tb_pessoas WHERE id = 1')

print('deletado com sucesso')

conn.commit()

conn.close()