import sqlite3

conn = sqlite3.connect('exercicio01.db')

cursor = conn.cursor()

#Delete Author
cursor.execute('DELETE FROM Author WHERE AuthorID = 1')

#Delete Post

conn.commit()

conn.close()