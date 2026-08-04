import json

def addTask(path: str, task: list) -> None:
    file = open(path, 'r')
    a: dict = json.load(file)
    a[task[0]] = task[1]
    file.close()

    file = open(path, 'w')
    json.dump(a, file)

addTask("./testData.json",  
        ["2",
            {
                "title": "Sample Title",
                "description": "Sample Description",
                "priority": 1, 
                "category": "Work"
            }
        ]
)

f = {}
y = ["13", {"title": "tit"}]

f[y[0]] = y[1]
# f["13"] = {"title": "tit"}
{
    "13": {
        "title": "tit"
    }
}