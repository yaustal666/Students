### Question 4 | Level 1

### EN
***
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

<br><br>

### RU
***
Напишите программу, которая принимает последовательность чисел, разделенных запятыми, с консоли и генерирует список и кортеж, содержащие каждое число.
Предположим, что на вход программе подается:
34,67,55,33,12,98
Тогда вывод должен быть:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)
```

</details>

