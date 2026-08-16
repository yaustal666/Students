#failed to success

def palindrome():
    a = input()
    for i in range(0,len(a)):
        check1 = a[i]
        for j in range(-1, len(a), -1):
            check2 = a[j]
            if check1 != check2:
                return False
    return True
print(palindrome()) #guess the problem in the lower part of if check 1 and check 2

# Два варианта - развернутый, проходим один раз по строке
# и сравниваем первый с последним, второй с предпоследним и тд до середины
# если нашли несовпадение - конец и возвращаем false
# Понадобится только 1 цикл. Запускаем i от 0 до длины len(a)
# i - индекс слева, индекс с конца вычисляется как len(a) - i - 1 либо в питоне просто -i

# Второй вариант выглядит так
def plaingrome():
    a = input()
    return a == a[::-1]