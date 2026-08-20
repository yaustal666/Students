### Question 60 | Level 1

### EN
***
Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example:
If the following words is given as input to the program:

2 cats and 3 dogs.

Then, the output of the program should be:

['2', '3']

<br><br>

### RU
***
Напишите программу, которая принимает последовательность слов, разделенных пробелами, в качестве входных данных и выводит слова, состоящие только из цифр.

Пример:
Если на вход программе подаются следующие слова:

2 cats and 3 dogs.

Тогда вывод программы должен быть:

['2', '3']

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
import re
s = input()
print(re.findall(r"\d+", s))
```

</details>

