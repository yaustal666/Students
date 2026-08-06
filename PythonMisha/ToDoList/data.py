import json

def addTask(path: str, task: list) -> None:
    file = open(path, 'r')
    a = json.load(file)

    a[task[0]] = task[1]
    file.close()

    file = open(path, 'w')
    json.dump(a, file)

def getTask(path: str, taskId: str) -> dict:
    file = open(path, 'r')
    a = json.load(file)
    file.close()
    return a[taskId]

print(getTask("./testData.json", "1"))

addTask("./testData.json",  
        ["2",
            {
                "title": "Sample Title",
                "description": "Sample Description",
                "priority": 2, 
                "category": "Work"
            }
        ]
)

print(getTask("./testData.json", "2"))
