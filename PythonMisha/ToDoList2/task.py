#  Создание модели - датакласс Task
class Task:
    def __init__(self, name, description, significance):
        self.name = name
        self.description = description
        self.significance = significance
        self.id = 0