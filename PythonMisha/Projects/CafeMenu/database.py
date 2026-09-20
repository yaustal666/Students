import sqlite3

database = sqlite3.connect('database.db')
cursor = database.cursor()

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    price REAL NOT NULL CHECK(price > 0),
    category TEXT NOT NULL CHECK(category IN ('Soup', 'Drink'))
)
"""
)