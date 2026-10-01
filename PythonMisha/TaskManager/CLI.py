import sqlite3
from TaskService import TaskService

database = sqlite3.connect("Database.db")
cursor = database.cursor()

ts = TaskService(database)

def query(request: str) -> None:
    if request == "get":
        cursor.execute(
            """
            SELECT *
            FROM tasks
            """
        )
        result = cursor.fetchall()
        print(result)

    if request == "post":
        name = input()
        description = input()
        
        cursor.execute(
            """
            INSERT into tasks (name, description)
            VALUES (?, ?)
            """,
            (name, description)
        )
        database.commit()
        
    if request == 'delete':
        id = int(input())
        
        cursor.execute(
            """
            DELETE from tasks
            WHERE id = ? 
            """,
            (id,)
        )
        database.commit()
        
while True:
    req = input()
    if req == 'exit':
        break
    query(req)

# if request == "post":
#     name = input()
#     description = input()
    
#     ts.add_task(name, description)