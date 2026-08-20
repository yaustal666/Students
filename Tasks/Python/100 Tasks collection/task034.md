### Question 14 | Level 2

### EN
***
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

<br><br>

### RU
***
Напишите программу, которая принимает предложение и подсчитывает количество букв в верхнем и нижнем регистрах.
Предположим, что на вход программе подается:
Hello world!
Тогда вывод должен быть:
UPPER CASE 1
LOWER CASE 9

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])
```

</details>

