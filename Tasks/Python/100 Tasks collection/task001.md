### Question 1 | Level 1

### EN
***
Write a program which will find all numbers that

* Divisible by 7 but are not a multiple of 5
* Are inside [2000, 3200].

The numbers obtained should be printed in a comma-separated sequence on a single line.

<br><br>

### RU
***
Напишите программу которая находит все числа, которые

* Делятся на 7 и не имеют множителя 5
* Лежат в промежутке [2000, 3200].

Полученные числа необходимо вывести в одну строку, разделенные запятыми

<br><br>

<details>
<summary>Solution/Решение</summary>
  
```python
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))
```

</details>

