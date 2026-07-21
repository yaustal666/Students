# 6
from random import randint

loop = int(input())
set = [randint(0, 1000) for i in range(loop)]
iterible = 0
for i in range(loop):
    
    if i % 3 != 0 and i**i <= 100000:
        iterible += 1
print(set, iterible, end = '\n') #I didnt really catch how to create infinite loop but most of all what exactly to cease when value is greater than 100000


# Запустить бесконечный цикл можно вот так, то есть Пока правда делай что-то, но True всегда правда
count = 0
while True:
    num = randint(0, 1000) # генерируем рандомное число
    if not num % 3 == 0: # То есть считаем только когда не делится на 3
        count += 1
    
    if num**2 > 100000: #Если квадрат больше 100000, заканчиваем цикл
        break
print(count)