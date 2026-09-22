from pydantic import BaseModel
import json

class Task(BaseModel):
    name: str
    description: str
    significance: int

class TaskManager:
    def __init__(self):
        self.tasks = {}
    
    def addTaskByValues(self, name, description, significance):
        self.tasks[name] = Task(name=name, description=description, significance=significance)

    def addTask(self, task):
        self.tasks[task.name] = task
    
    def update(self, name, description, significance):
        task_to_update = self.tasks[name]
        task_to_update.description = description
        task_to_update.significance = significance
        
    def deleteTask(self, name):
        self.tasks.pop(name)

    def printTasks(self):
        print(self.tasks)

task = Task(name="Name", description="Do something", significance=2)

# save / serialization
with open("tasks.json", "w") as file:
    json.dump(task.model_dump_json(), file)

# load / deserialization
with open("tasks.json", "r") as file:
    tasks = json.load(file)
    task1 = Task.model_validate_json(tasks)
    print(type(task1))