### Question 68 | Level 1

### EN
***
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

<br><br>

### RU
***
Пожалуйста, напишите программу с использованием генератора для вывода четных чисел от 0 до n в формате, разделенном запятыми, где n вводится с консоли.

Пример:
Если на вход программе подается следующее значение n:

10

Тогда вывод программы должен быть:

0,2,4,6,8,10

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1

n=int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))
```

</details>

