import sqlite3

database = sqlite3.connect('Books.db')
cursor = database.cursor()

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    language TEXT
);
"""
)

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    author_id INTEGER,

    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
);
"""
)

database.commit()