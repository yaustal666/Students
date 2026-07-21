from random import randint

# Everything in python is an object
# For example in C language - there are no objects at all
# What is an object?

class Cat:
    def __init__(self, kind, age, name):
        self.kind = kind
        self.age = age
        self.name = name 
    
    def meow():
        print("meow!")

newCat = Cat("Manchkin", 8, "Boris")
newCat.meow()


# Lists

# How to create a list?
list1 = []
list4 = list()
list2 = [1, 2, 3]
list3 = [3] * 10

# How to take values
# By index
print(list3[1])
list3[1] = 2

# Slices
a = list3[1:4:2]

# Iterating
for i in list3:
    print(i)

for i in range(len(list3)):
    list3[i] = int(list3[i])


# List comprehension
list4 = [1 for i in range(10)]
list4 = [i**2 for i in range(10)]
list4 = [str(i) for i in list4]

pool = input().split() # 1 2 3 4 5 6
pool = [int(i) for i in pool]
print(pool)

# Manipulating a list
someList = [1, 2, 3]
someList.insert(1, 55)
print(someList)

# In
pool = [1, 2, 3, 4, 5]
a = 3

# Здесь забыл важный момент, данный цикл найдет ВСЕ значения a в списке и на каждый напишет True
# А мы хотели просто проверить есть ли, поэтому я добавил break - цикл остановится, как только мы найдем
# хотя бы 1 совпадение

for i in pool:
    if i == a:
        print(True)
        break

pool = [randint(1, 100) for i in range(10)]
print(pool)

pool2 = []
pool2 = pool + pool2 
pool2 = pool2[-1:  : -1]

for i in range(len(pool) - 1, -1, -1):
    pool2.append(pool[i])

print(pool2)