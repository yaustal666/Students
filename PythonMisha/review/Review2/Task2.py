num = int(input())
def counter(num):
    digits = 0
    set = list(str(num))
    sum1 = 0
    for i in str(num):
        digits += 1
    for i in range(len(set)):
        sum1 += int(set[i])   
    return digits,sum1
print(counter(num)) 
#!!! 1 - stuck at list(str(num)) becuase i tried to convert so it would be subscriptable, 
# 2 - and another problem related to subscriptability

# set = list(str(num)) - создаешь список с 1 элементом, который строка
# строка тоже  iterable, по ней можно пройтись
# если у тебя список со строкой то обращение к букве будет set[i][j] как к таблице

# Два варианта - первый используя строку
def counter2(num: str):
    count = 0
    sum = 0

    for i in num:
        count += 1
        sum += int(i)

    return count, sum

# Второй вариант если работаем именно с числом и нельзя использовать строку
def counter3(num: int):
    count = 0
    sum = 0

    while num:
        sum += num % 10
        count += 1
        num = num // 10

    return count, sum