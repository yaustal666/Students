# Обновил эту задачу в списке задач, переделай пожалуйста

# Дано два значения, первое - ключ, второе - значение для этого ключа
a = "key"
b = "value"
# Создайте словарь и добавьте в него запись ключ-значение
firstdict = {
    a : b
}

# То же самое, но для новых данных
key = "a"
value = "b"
secondDIct = {
    key : value
}

# Тоже самое, но теперь значения даны с помощью списка
# Первый элемент - ключ, второй - значение
kvp = ["list_key", "some interesting value"]
thirdDict = {
    kvp[0] : kvp[1]
}
# Выведите словарь, по итогу в нем должно быть три записи
fourthtargetDict = {}
fourthtargetDict.update({
    a : b,
    key : value,
    value : 'b',
    kvp[0] : kvp[1]
})
print(fourthtargetDict)
