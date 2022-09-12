import sqlite3

conn = sqlite3.connect('espm4s.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_pessoas(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INT NOT NULL
)
""")   

conn.commit()

conn.close()