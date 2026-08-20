### Question 20 | Level 3

### EN
***
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

<br><br>

### RU
***
Определите класс с генератором, который может перебирать числа, делящиеся на 7, в заданном диапазоне от 0 до n.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in reverse(100):
    print(i)
```

</details>

