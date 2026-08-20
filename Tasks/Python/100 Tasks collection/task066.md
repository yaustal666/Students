### Question 66 | Level 1

### EN
***
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

13

<br><br>

### RU
***
Последовательность Фибоначчи вычисляется на основе следующей формулы:

f(n)=0 если n=0
f(n)=1 если n=1
f(n)=f(n-1)+f(n-2) если n>1

Пожалуйста, напишите программу для вычисления значения f(n) с заданным n, введенным с консоли.

Пример:
Если на вход программе подается следующее значение n:

7

Тогда вывод программы должен быть:

13

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
print(f(n))
```

</details>

