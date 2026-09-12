# Запуск / эндпоинты

import sqlite3
from taskManager import TaskManager

database = sqlite3.connect("app.db")

tm = TaskManager(database)

tm.add_task("Name 1", "Do", 3)