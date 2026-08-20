### Question 13 | Level 2

### EN
***
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

<br><br>

### RU
***
Напишите программу, которая принимает предложение и подсчитывает количество букв и цифр.
Предположим, что на вход программе подается:
hello world! 123
Тогда вывод должен быть:
LETTERS 10
DIGITS 3

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])
```

</details>

