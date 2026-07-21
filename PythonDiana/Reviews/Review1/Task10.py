# Все ок

# tenth question
n = int(input())
a = 1
b = 1
for i in range(n-2):
    c = a + b
    a = b
    b = c
print(b)

# Еще вариант, на 1 переменную меньше
a = 1
c = 0
for i in range(n):
    c = c + a
    a = c - a
print(c)