#Все ок
n = input()     #first questiom from the second file
if n == n[:: -1]:
    print(True)
else:
    print(False)


# Все ок
#third question
def divisible(n):
    result = []
    for i in range (1, n+1):
        if n % i == 0:
            result.append(True)
        else:
            result.append(False)
    print(result)
divisible(5)


#  Все ок
#fourth question
def divisors(n):
    count = 0
    for i in range(2, n+1):
        if n%i ==0:
            count += 1
    print(count)
divisors(10)
divisors(5)

# Все ок
#fifth question
def prime(n):
    count = 0
    for i in range(2, n + 1):
        if n % i == 0:
            count += 1
    if count == 1:
        print(True)
    else:
        print(False)
prime(5)
prime(10)

# Все ок
# sixth question
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            print(False)
            return
    print(True)
prime(5)
prime(10)


# Все ок
#seventh question
import math
def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(False)
            return
    print(True)
prime(5)
prime(10)