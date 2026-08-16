a = int(input())
b = int(input())

# input - func
# call
# result - str
# int - func
# call
# pass args - str
# result - int
# assignment
# a - int

if a > b:
    print(a)
else:
    print(b)

for i in range(100):
    print(1)

def evenNum(a: int):
    if a % 2 == 0:
        return True
    else:
        return False

print(evenNum(101))


import random
a = random.randint(1, 4) 

match a:
    case 1: print("Hello")
    case 2: print("2")
    case 3: print(3)
    case 4: print("No")
    case _: print("default")

a = []

for i in range(10):
    a.append(random.randint(0, 100))

n = 10
b = [1, 1]
for i in range(n):
    if (i <= 1): print(b[i])
    else:
        b.append(b[i - 1] + b[i - 2])
        print(b[i])


def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

print(fib(10)) 