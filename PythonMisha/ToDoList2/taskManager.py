# Управляющий класс TaskManager
import sqlite3
from taskDao import TaskDao
from task import Task

class TaskManager:
    def __init__(self, database: sqlite3.Connection):
        self.taskDao = TaskDao(database)
    
    def add_task(self, name, description, significance) -> None:
        self.taskDao.add_task(Task(name, description, significance))