from pydantic import BaseModel
from dataclasses import dataclass, asdict
import json

class Task(BaseModel):
    id: int
    title: str
    priority: int

class TaskManager(BaseModel):
    tasks: list[Task]


task = Task(id=1, title="h", priority=2)
tl = TaskManager(tasks=[])
tl.tasks.append(task)
print(task)

# @dataclass
# class Task:
#     id: int
#     title: str
#     priority: int

# task = Task(1, "h", 2)
# print(task)