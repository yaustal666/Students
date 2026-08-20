### Question 2 | Level 1

### EN
***
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.

Suppose the following input is supplied to the program:
8\
Then, the output should be:
40320

<br><br>

### RU
***
Напишите программу, которая вычисляет факториал заданного числа.
Результаты должны быть выведены в одну строку, разделенные запятыми.

Предположим, что на вход программе подается число:
8\
Тогда вывод должен быть:
40320

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))
```

</details>