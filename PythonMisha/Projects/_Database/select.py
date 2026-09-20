import sqlite3
from pydantic import BaseModel

class Task(BaseModel):
    name: str
    description: str
    significance: int

database = sqlite3.connect("taskDatabase.db")
cursor = database.cursor()

lines = cursor.execute(
"""
SELECT * FROM tasks;
"""
)

rows = lines.fetchall()

tasks = []
for i in rows:
    tasks.append(Task(name=i[1], description=i[2], significance=i[3]))

print(tasks)