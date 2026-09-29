# Task Manager
# Чтобы программа позволяла мне добавить задание
# Посмотреть список всех заданий
# Задание - просто назване задания
# Через fastapi - endpoints
# При перезапуске программы задачи должны сохраняться
# Хочу уметь удалять
# Хочу чтобы у задачи было описание
# Хочу уметь изменять данные о каком-то конкретном задании

import sqlite3
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_tasks():
    database = sqlite3.connect("Database.db")
    cursor = database.cursor()

    cursor.execute("""
        SELECT *
        FROM tasks
        """)
    result = cursor.fetchall()
    return result


@app.post("/")
def add_task(name: str, description: str):
    database = sqlite3.connect("Database.db")
    cursor = database.cursor()

    cursor.execute(
        """
        INSERT into tasks (name, description)
        VALUES(?, ?)
        """,
        (name, description),
    )
    database.commit()


@app.delete("/")
def delete_task(id: int):
    database = sqlite3.connect("Database.db")
    cursor = database.cursor()

    cursor.execute(
        """
        DELETE FROM tasks
        WHERE id = ?
        """,
        (id,),
    )
    database.commit()


@app.patch("/")
def update_task(id, name=None, description=None):
    database = sqlite3.connect("Database.db")
    cursor = database.cursor()

    # if name is None:
    #     # select запрос чтобы получить имя по id
    #     # name = имя из запроса

    # if description is None:
    #     # select запрос чтобы получить описание по id
    #     # description = описание из запроса

    cursor.execute(
        """
        UPDATE tasks
        set name = ?, description = ?
        WHERE id = ?
        """,
        (name, description, id),
    )
    database.commit()
