### Question 11 | Level 2

### EN
***
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

<br><br>

### RU
***
Напишите программу, которая принимает последовательность четырехзначных двоичных чисел, разделенных запятыми, в качестве входных данных и проверяет, делятся ли они на 5 или нет. Числа, которые делятся на 5, должны быть выведены в виде последовательности, разделенной запятыми.
Пример:
0100,0011,1010,1001
Тогда вывод должен быть:
1010
Примечание: Предполагается, что данные вводятся с консоли.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))
```

</details>

