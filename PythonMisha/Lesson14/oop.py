class Task:

    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
    
class TaskList:
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def addTask(self, task: Task) -> None:
        self.tasks.append(task)

    def __str__(self):
        return self.title

    def __add__(self, other):
        return 2
    
l = TaskList("Work")
m = TaskList("Guu")
print(m + l)



# a = Task("he", "hh", 2)
# l.addTask(a)

# print(l.tasks[0].priority)