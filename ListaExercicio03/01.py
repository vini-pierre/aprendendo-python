import sqlite3

conn = sqlite3.connect('exercicio01.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Author(
    AuthorID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL
)
""")   

cursor.execute("""
CREATE TABLE IF NOT EXISTS Post(
    PostID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    AuthorID INTEGER NOT NULL,
    Title TEXT NOT NULL,
    Created DATATIME NOT NULL,
    FOREIGN KEY (AuthorID) REFERENCES Author
)
""")

conn.commit()

conn.close()