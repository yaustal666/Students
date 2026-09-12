from dataclasses import dataclass, asdict
from pydantic import BaseModel

# classical
# class Task:
#     def __init__(self, name, description, significance):
#         self.name = name
#         self.description = description
#         self.significance = significance

#dataclasses method
# @dataclass
# class Task:
#     name: str
#     description: str
#     significance: int

#     def foo(self):
#         return self.name

# task = Task("task1", "do something", 2)
# print(asdict(task))

#pydantic method(most used one)
class Task(BaseModel):
    name: str
    description: str
    significance: int

task = Task(name="Name", description="Do something", significance=2)
print(task)