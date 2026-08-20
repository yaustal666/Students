### Question 9 | Level 2

### EN
***
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

<br><br>

### RU
***
Напишите программу, которая принимает последовательность строк в качестве входных данных и выводит строки после преобразования всех символов в предложении в верхний регистр.
Предположим, что на вход программе подается:
Hello world
Practice makes perfect
Тогда вывод должен быть:
HELLO WORLD
PRACTICE MAKES PERFECT

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print(sentence)
```

</details>

