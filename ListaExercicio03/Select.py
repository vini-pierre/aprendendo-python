import sqlite3

conn = sqlite3.connect('exercicio01.db')

cursor = conn.cursor()

#Select Author
cursor.execute('SELECT * FROM Author')

#Select Post
cursor.execute('SELECT * FROM Post')


conn.commit()

conn.close()