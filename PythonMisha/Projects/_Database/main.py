import sqlite3

database = sqlite3.connect("taskDatabase.db")
cursor = database.cursor()

cursor.execute(
"""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        priority INTEGER CHECK(priority <= 3 AND priority >= 1)
    )
"""
)

def add_task_to_database(title, desc, priority):
    cursor.execute(
    """
    INSERT INTO tasks (title, description, priority) 
    VALUES (?, ?, ?);
    """,
    (title, desc, priority)
    )

    database.commit()

title = input()
description = input()
priority = int(input())

add_task_to_database(title, description, priority)