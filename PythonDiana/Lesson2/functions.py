def findValue(someList: list, value) -> int:
    for i in range(len(someList)):
        if someList[i] == value:
            return i

# def isEven(x: int) -> bool:
#     if x % 2 == 0:
#         return True
#     return False

# for i in [1, 2, 3, 4, 5]:
#     print(i, isEven(i))

# def area(length: float, width: float) -> float:
#     return length * width

# rectangles: dict = {
#     1: {
#         "length": 1.3, 
#         "width": 4.5
#     },
#     2: {
#         "length": 1.3, 
#         "width": 4.5
#     },
#     3: {
#         "length": 1.3, 
#         "width": 4.5
#     }
# }

# for i, rectangle in rectangles.items():
#     a = area(rectangle["length"], rectangle["width"])
#     print(a)


from random import randint

# n - кол-во граней у кубика
def rollDice(n: int) -> int:
    return randint(1, n)

# n - количество граней, m - количество бросков
# посчитать среднее значение среди всех выпавших значений
def calculateRollStatistics(m : int , n: int) -> float:
    x = 0
    for i in range(m):
        x += rollDice(n)
    
    return x / m

print(calculateRollStatistics(1000000, 7))

