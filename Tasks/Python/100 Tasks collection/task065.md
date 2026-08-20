### Question 65 | Level 1

### EN
***
Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

500

<br><br>

### RU
***
Напишите программу для вычисления:

f(n)=f(n-1)+100 при n>0
и f(0)=1

с заданным n, введенным с консоли (n>0).

Пример:
Если на вход программе подается следующее значение n:

5

Тогда вывод программы должен быть:

500

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(input())
print(f(n))
```

</details>

