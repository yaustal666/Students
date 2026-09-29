import sqlite3

database = sqlite3.connect("Database.db")
cursor = database.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);
""")
