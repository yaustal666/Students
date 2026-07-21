#4 failed attempt - вообще то код верно работает, ты проверял?
# Да, он странный - но работает

a = int(input())
b = int(input())
set = [a, b]
check = 0
for i in set:
    if i > check:
        check = i
print(check)

# next attempt -  это тоже верно работает

a = int(input())
b = int(input())
check = 0
if a > check:
    check = a
if b > check:
    check = b
print(check)

# Обычное решение, опять обращаю внимание на формат выходных данных - по заданию это либо "A" либо "B", не число
a = int(input())
b = int(input())
if a > b:
    print("A")
else:
    print("B")

# Вариант через 0, логика такая, мы считаем a - b, если результат меньше 0, то a > b, иначе наоборот
a = int(input())
b = int(input())

if a - b < 0:
    print("A")
else:
    print("B")

# Так работает на assembler. Операции + и - две самые базовые операции, остальные во многом строятся из них
# Сравнение с нулем в прямом смысле не происходит на уровне assembler, там немного другой механизм.
# Это просто интересная инфа для справки так сказать.