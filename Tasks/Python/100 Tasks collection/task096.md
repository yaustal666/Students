### Question 96 | Level 1

### EN
***
Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

<br><br>

### RU
***
Пожалуйста, напишите программу, которая подсчитывает и выводит количество каждого символа в строке, введенной с консоли.

Пример:
Если на вход программе подается следующая строка:

abcdefgabc

Тогда вывод программы должен быть:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
dic = {}
s = input()
for s in s:
    dic[s] = dic.get(s,0)+1
print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))
```

</details>

