### Question 67 | Level 1

### EN
***
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13

<br><br>

### RU
***
Последовательность Фибоначчи вычисляется на основе следующей формулы:

f(n)=0 если n=0
f(n)=1 если n=1
f(n)=f(n-1)+f(n-2) если n>1

Пожалуйста, напишите программу с использованием спискового включения для вывода последовательности Фибоначчи в формате, разделенном запятыми, с заданным n, введенным с консоли.

Пример:
Если на вход программе подается следующее значение n:

7

Тогда вывод программы должен быть:

0,1,1,2,3,5,8,13

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
values = [str(f(x)) for x in range(0, n+1)]
print(",".join(values))
```

</details>

