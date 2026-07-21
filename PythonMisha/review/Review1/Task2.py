#2

# Все ок
# Еще один вариант сразу получить список чисел
# Через list comprehension
comb = [int(i) for i in input().split()]

comb = list(input())
maximum = int(max(comb))
print(maximum)


#Все ок
#alternative

a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(a, 'is the greatest')
if b > a and b > c:
    print(b, "is the greatest")
if c > a and c > b:
    print(c, 'is the greatest ')