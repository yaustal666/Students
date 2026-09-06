from pydantic import BaseModel

class Task(BaseModel):
    name: str
    description: str
    significance: int


class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def addTask(self, name, description, significance):
        self.tasks.append(Task(name=name, description=description, significance=significance))

    def addTask(self, task):
        self.tasks.append(task)
        
    def deleteTask(self, name):
        task_to_delete = list(filter(lambda task: task.name == name, self.tasks))
        
        if len(task_to_delete) > 0:
            task_to_delete = task_to_delete[0]
            self.tasks.remove(task_to_delete)


tm = TaskManager()

name = input()
desc = input()
sig = int(input())

task = Task(name="Name", description="Do something", significance=2)
tm.addTask(task)

tm.addTask("Name", "Do", 3)
