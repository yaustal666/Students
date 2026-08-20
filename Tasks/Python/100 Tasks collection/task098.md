### Question 98 | Level 1

### EN
***
Please write a program which accepts a string from console and print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

<br><br>

### RU
***
Пожалуйста, напишите программу, которая принимает строку с консоли и выводит символы, имеющие четные индексы.

Пример:
Если на вход программе подается следующая строка:

H1e2l3l4o5w6o7r8l9d

Тогда вывод программы должен быть:

Helloworld

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
s = input()
s = s[::2]
print(s)
```

</details>

