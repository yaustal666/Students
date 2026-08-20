### Question 100 | Level 1

### EN
***
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

<br><br>

### RU
***
Напишите программу для решения классической древней китайской головоломки:
Мы насчитали 35 голов и 94 ноги среди кур и кроликов на ферме. Сколько кроликов и сколько кур у нас?

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def solve(numheads, numlegs):
    ns = 'No solutions!'
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    return ns, ns

numheads = 35
numlegs = 94
solutions = solve(numheads, numlegs)
print(solutions)
```

</details>