"""
2) Collecting Pocket Money in a Piggy Bank (Recursive Sum vs. Iterative Sum)
A student deposits money into a piggy bank for n days, adding
an amount equal to the day number each day (1 TL on Day 1, 2 TL on Day 2 ... n TL on Day n).

What would happen if n = 5?

Find the total accumulated money using summation algorithms:

Iterative Logic: Initializes total = 0 and sums the amounts using a range(1, n + 1) loop (O)
Recursive Logic: At each step, the function takes the current day's money and calls itself to compute the sum of previous days (n + recursive_sum(n - 1))
"""


def piggy_bank_iteration(days: int) -> str:
    all_money = 0
    for i in range(1, days + 1):
        all_money += i
    return f"total accumulated money: {all_money}"


def piggy_bank_recursion(days: int) -> int:
    if days == 1:
        return 1
    return piggy_bank_recursion(days - 1) + days
