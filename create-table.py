import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute(
    """CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
    )"""
)

c.execute("INSERT INTO users (username, password) VALUES ('admin', 'password')")
c.execute("INSERT INTO users (username, password) VALUES ('moderator', 'password')")

conn.commit()
conn.close()
