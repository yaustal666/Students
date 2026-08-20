### Question 44 | Level 1

### EN
***
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

<br><br>

### RU
***
Напишите программу, которая принимает строку в качестве входных данных и выводит "Yes", если строка равна "yes", "YES" или "Yes", в противном случае выводит "No".

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
s = input()
if s == "yes" or s == "YES" or s == "Yes":
    print("Yes")
else:
    print("No")
```

</details>