from time import time

import sys
sys.setrecursionlimit(100000)


def factorial_loop(n: int) -> int:
    counter = 1
    result = 1
    while counter < n + 1:
        result *= counter
        counter += 1
    return result


def factorial_recursion(n: int) -> int:
    if n == 1:
        return 1
    return factorial_recursion(n - 1) * n


start = time()
factorial_recursion(100000 - 1)
end = time()
print((end - start) * 1000)

start = time()
factorial_loop(100000 - 1)
end = time()
print((end - start) * 1000)