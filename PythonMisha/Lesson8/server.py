from fastapi import FastAPI

class TaskManager:
    def __init__(self, tasks):
        self.tasks = tasks

tasks = {
    "1": {
        "title": "Task1",
        "description": "bla bla 1",
        "subtasks": {
            "1_1": "subtask 1",
            "1_2": "subtask 2" 
        },
        "priority": 0
    },
    "2": {
        "title": "Task2",
        "description": "bla bla 2",
        "subtasks": {
            "2_1": "subtask 1",
            "2_2": "subtask 2" 
        },
        "priority": 1
    },
    "3": {
        "title": "Task3",
        "description": "bla bla 3",
        "subtasks": {
            "2_1": "subtask 1",
            "2_2": "subtask 2" 
        },
        "priority": 1
    },
    "4": {
        "title": "Task4",
        "description": "bla bla 4",
        "subtasks": {
            "2_1": "subtask 1",
            "2_2": "subtask 2" 
        },
        "priority": 3
    },
}
task_manager = TaskManager(tasks)

def get_all_tasks(tm: TaskManager) -> list:
    return list(tm.tasks.items())

def get_task_by_id(tm: TaskManager, id: int) -> dict:
    return tm.tasks[str(id)]

# return [(i, tm.tasks[i]) for i in tm.tasks if tm.tasks[i]["priority"] == pr]
def get_tasks_by_priority(tm: TaskManager, pr: int) -> list:
    group = []
    for i in tm.tasks:
        if tm.tasks[i]["priority"] == pr:
            group.append((i, tm.tasks[i]))
    return group       
        

def get_task_subtasks(tm: TaskManager, id: int) -> list: # [["1_1", subtask 1], ["1_2", "subtask 2"]]
    pass

app = FastAPI()

@app.get("/")
async def root():
    return get_task_by_id(task_manager, 1)
