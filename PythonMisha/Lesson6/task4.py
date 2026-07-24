# Давай напишем функцию, которая будет проверять,
# является ли тип iterable

def isIterable(a: type) -> bool:
    if '__iter__' in dir(a):
        return True
    return False

print(isIterable(str))