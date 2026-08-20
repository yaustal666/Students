### Question 6 | Level 2

### EN
***
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

<br><br>

### RU
***
Напишите программу, которая вычисляет и выводит значение по следующей формуле:
Q = Квадратный корень из [(2 * C * D)/H]
Фиксированные значения C и H:
C = 50, H = 30.
D — это переменная, значения которой должны подаваться на вход программе в виде последовательности, разделенной запятыми.
Пример
Предположим, что на вход программе подается следующая последовательность, разделенная запятыми:
100,150,180
Вывод программы должен быть:
18,22,24

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))
```

</details>

