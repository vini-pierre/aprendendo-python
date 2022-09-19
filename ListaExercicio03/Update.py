import sqlite3

conn = sqlite3.connect('exercicio01.db')

cursor = conn.cursor()

#Update Author
cursor.execute('UPDATE Author SET Name = ? WHERE AuthorID = ?', ('Vini Pierre', 1))

#Update Post
cursor.execute('UPDATE Post SET Title = ? WHERE PostID = ?', ('feijão', 1))

conn.commit()

conn.close()