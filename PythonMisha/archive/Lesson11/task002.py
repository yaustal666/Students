def factorial(a : int) -> int:
    fac = 1
    for i in range(1, a + 1):
        fac *= i
    return fac
print(factorial(8))