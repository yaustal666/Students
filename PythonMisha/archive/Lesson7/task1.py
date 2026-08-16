# Напиши функцию кидания кубика с n сторонами, 
# значения на нем от 1 до n

# Напиши функцию для замера среднего результата 
# броска кубика с n сторонами за N попыток

from random import randint 

def roll(n: int) -> int:
    return randint(1, n)

def averageRoll(n: int, b: int) -> float:
    m = 0
    for i in range(b):
        m += roll(n) 
    return m / b

print(averageRoll(21, 1000000))     