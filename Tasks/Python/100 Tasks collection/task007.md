### Question 34 | Level 1

### EN
***
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

<br><br>

### RU
***
Определите функцию, которая может выводить словарь, где ключи являются числами от 1 до 20 (включительно), а значения - квадратами ключей.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    print(d)

printDict()
```

</details>

