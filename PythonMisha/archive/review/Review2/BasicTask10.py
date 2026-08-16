
# Все ок
def printText():
    print('Hello World!')
printText()  #!!!  tried to find out how to invoke def


# Все ок, но надо аннтоации добавить для красоты
def greatest(a, b, c):
    nums = [a, b, c]
    maximum = max(nums)
    # можно вот так сократить
    # maximum = max([a, b, c])
    return maximum
print(greatest(5, 6, 7))



# Все ок, но надо аннтоации добавить для красоты
# Функции которые возвращают boolлучше называть isSomething
#  В данном случае isEven например. Как вопрос.
def even(a):
    if a % 2 == 0:
        return True
    else:
        return False
print(even(int(input())))



#
a = int(input())
b = int(input())
#надо аннтоации добавить для красоты
def comparison(a, b):
    target = 0
    if a > 0:
        target = a
        if target > b:
            return target
    if b > a and b > target:
        return b

    # немного не понял
    # if a > b:
    #   return a
    # else:
    #   return b
    # Разве не тоже самое?    
print(comparison(a, b))  



# Все ок, но надо аннтоации добавить для красоты
a = 1
def loop(a):
    print([a for i in range(10)])
loop(a)


#10.6
from random import randint
def loop():
     count = 0
     pool = [] #to check further which nums we got
     while True:
        nums = randint(0, 1000)
        pool.append(nums)
        count += 1 
        if nums % 3 == 0:
            count -= 1
        if nums % 3 == 0 and nums ** nums > 100000:
            return count, pool
print(loop())      #1 - it undercounts by 1:i reckon because of  if nums % 3 == 0 

# Вот так оно выглядит, тут важен порядок, чтобы праивльно считалось
def loop():
    count = 0
    while True:
        nums = randint(0, 1000)
        if not nums % 3 == 0:
            count += 1

        if nums ** nums > 100000:
            return count



# Все ок
def combination():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                print(i,j,k)    
combination()

  
# Не понял что это за задача, если это про рассчет площади то зачем деление на 0.5?
# Напиши мне в телегу объясни  
a = list(map(float, input().split())) 
b = list(map(float, input().split())) 
c = list(map(float, input().split())) 
d = list(map(float, input().split())) 
def square(a : float , b : float, c : float, d : float):
    disc = ((a[1] - a[0]) + (b[1] - b[0])) / 0.5
    return disc
print(square(a, b, c, d)) 
# попробуй нарисовать прямоугольник и подписать координаты углов, станет видно как посчитать длину и ширину   