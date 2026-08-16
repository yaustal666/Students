from random import random
from time import time

def approximate_pi(n: int) -> float:
    in_circle: int = 0
    x: float = 0 
    y: float = 0 
    result: float = 0

    # (0, 1) -> (-1, 1) ?
    # (0, 1) * 2 -> (0, 2) - 1 -> (-1, 1) 

    for i in range(n):
        x = random() * 2 - 1
        y = random() * 2 - 1
        if x ** 2 + y ** 2 <= 1:
            in_circle += 1
        

    result = 4 * in_circle / n
    return result

n: int = int(input())

start = time()
res = approximate_pi(n)
end = time()
difference = (end - start) * 1000

print(difference)
print(res)