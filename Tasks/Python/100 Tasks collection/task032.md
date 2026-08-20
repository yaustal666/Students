### Question 12 | Level 2

### EN
***
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

<br><br>

### RU
***
Напишите программу, которая найдет все числа от 1000 до 3000 (включительно), такие что каждая цифра числа является четной.
Полученные числа должны быть выведены в одну строку, разделенные запятыми.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))
```

</details>

