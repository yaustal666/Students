"""1) Rabbit Population Speed Test (Algorithm Comparison)
You will design two different algorithms that determine the number of rabbit pairs on a farm across months.
 Run both algorithms first for n = 10, then for n = 35, and observe the execution time spent by each.
 Both will produce mathematically identical results; however, their working principles and computational overhead will differ significantly.

Hints:

Hint 1 (Recursive - Self-Calling): Place a base case inside the function:
If n<= 1, return n directly.
If the number is greater than 1, call the function recursively by summing the results of the previous
two months: fibonacci(n - 1) + fibonacci(n - 2)

Hint 2 (Iterative - Loops and Variables):
Assign the initial values a = 0 and b = 1.
Create a for loop running from 2 up to n and shift the values at each step:
assign the value of b to a, and assign the sum of the previous a and b to b (a, b = b, a + b)

Hint 3 (Time Measurement):
Add import time at the beginning of your code.
Start the stopwatch right before calling the function with start = time.time(),
capture end = time.time() when the function completes, and print the elapsed difference (end - start)
"""

from time import time


def population_iteration(n: int) -> list:
    sequence = [1, 1, 2]
    for i in range(2, n + 2):
        sequence.append(sequence[i] + sequence[i - 1])
    return sequence[-1]


start = time()
print(population_iteration(10))
end = time()
print(f"time elapsed for iteration: {end - start}")


def population_recursion(n: int) -> int:
    if n <= 1:
        return 1
    return population_recursion(n - 1) + population_recursion(n - 2)


start = time()
population_recursion(10)
end = time()
print(f"time elapsed for recursion: {end - start}")
