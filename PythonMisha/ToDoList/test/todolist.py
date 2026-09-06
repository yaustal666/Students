import json

class Task:
    def __init__(self, id):
        self.id = id
        self.title = ""
        self.description = ""
        self.priority = ""

    def __str__(self):
        return f"id: {self.id}\ntitle: {self.title}\ndesc: {self.description}\nprior: {self.priority}"
    
class TaskManager:
    def __init__(self, path = "./testData.json"):
        self.path: str = path
        self.tasks: dict[str, Task] = {}

        self.load_tasks()
        
    def load_tasks(self):
        loaded_tasks = []
        with open(self.path, "r") as file:
            loaded_tasks = json.load(file)

        for id, task_data in loaded_tasks.items():
            task = Task(id)
            task.title = task_data["title"] 
            task.description = task_data["description"]
            task.priority = task_data["priority"]

            self.tasks[id] = task

    def add_task(self, task: Task) -> None:
        self.tasks[task.id] = task

    def update_task(self, id, title, description, priority) -> None:
        task = self.tasks[id]
        task.title = title
        task.description = description
        task.priority = priority

    def remove_task(self, id: str) -> None:
        self.tasks.pop(id)

    def get_tasks_by_priority(self, priority: int) -> list:
        return list(filter(lambda task: task.priority == priority, self.tasks.values()))

tm = TaskManager()
tm.update_task("1", "Hello", "world", 5)
print(tm.tasks["1"])
