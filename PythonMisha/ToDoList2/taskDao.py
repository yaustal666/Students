# Создание слоя доступа к данным TaskDAO

from task import Task
import sqlite3

class TaskDao:
    def __init__(self, database: sqlite3.Connection):
        self.database = database
        self.cursor = database.cursor

    def add_task(self, task: Task) -> None:
        self.cursor.execute(
            """
            INSERT INTO tasks (name, description, significance) 
            VALUES (?, ?, ?)
            """,
            (task.name, task.description, task.significance)
        )

        self.database.commit()
        

    def update_task(self, task: Task) -> None:
        self.cursor.execute(
            """
            UPDATE tasks 
            SET name = ?, description = ?, significance = ?
            WHERE id = ?
            """,
            (task.name, task.description, task.significance, task.id) 
        )

        self.database.commit()

    def delete_task(self, task: Task) -> None:
        self.cursor.execute(
            """
            DELETE FROM tasks
            WHERE id = ?
            """,
            (task.id,)
        )

        self.database.commit()

    def get_task_by_id(self, id: int) -> Task:
        pass

    def get_tasks(self) -> list[Task]:
        pass

    def get_tasks_by_significance(self, significance: int) -> list[Task]:
        pass

