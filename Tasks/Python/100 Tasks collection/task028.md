### Question 8 | Level 2

### EN
***
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

<br><br>

### RU
***
Напишите программу, которая принимает последовательность слов, разделенных запятыми, в качестве входных данных и выводит слова в виде последовательности, разделенной запятыми, после сортировки в алфавитном порядке.
Предположим, что на вход программе подается:
without,hello,bag,world
Тогда вывод должен быть:
bag,hello,without,world

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
items=[x for x in input().split(',')]
items.sort()
print(','.join(items))
```

</details>

