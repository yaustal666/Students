# Создание таблицы

import sqlite3

database = sqlite3.connect("app.db")
cursor = database.cursor()

cursor.execute(
"""
CREATE TABLE tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    significance INTEGER NOT NULL CHECK(significance <= 5 AND significance >= 1)
);
"""
)