# Нужно скопировать содержимое файла data.json в файл result.json
import json

file = open("data.json")
a = json.load(file)
print(a)