### Question 69 | Level 1

### EN
***
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70

<br><br>

### RU
***
Пожалуйста, напишите программу с использованием генератора для вывода чисел от 0 до n, которые делятся на 5 и 7, в формате, разделенном запятыми, где n вводится с консоли.

Пример:
Если на вход программе подается следующее значение n:

100

Тогда вывод программы должен быть:

0,35,70

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input())
values = []
for i in NumGenerator(n):
    values.append(str(i))

print(",".join(values))
```

</details>

