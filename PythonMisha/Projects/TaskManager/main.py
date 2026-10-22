# Можно добавить задание, посмотреть список всех заданий,
# удалить задание, изменить задание
# Задание имеет название и описание
# Пользовательский интерфейс через swagger
# Задачи персистентны
# CLI (command line interface)

# + У задачи есть приоритет, нужно уметь выводить задачи
# 1 - Отсортированными по приоритету, 
# 2 - Задачи какого-то конкретного приоритета
# Нужно иметь возможность получить информацию о конкретном задании по его id
# Запрос на получение всех заданий должен отправлять только имя и приоритет
# Запрос на получение конкретного задания отправляет все данные о задании
# Должно поддерживаться и в swagger и в CLI

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

    cursor.execute(
        """
        UPDATE tasks
        set name = ?, description = ?
        WHERE id = ?
        """,
        (name, description, id),
    )
    database.commit()
