### Question 33 | Level 1

### EN
***
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

<br><br>

### RU
***
Определите функцию, которая может выводить словарь, где ключи являются числами от 1 до 3 (включительно), а значения - квадратами ключей.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def printDict():
    d=dict()
    d[1]=1
    d[2]=2**2
    d[3]=3**2
    print(d)
printDict()
```

</details>