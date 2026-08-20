### Question 35 | Level 1

### EN
***
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

<br><br>

### RU
***
Определите функцию, которая может генерировать словарь, где ключи являются числами от 1 до 20 (включительно), а значения - квадратами ключей. Функция должна выводить только значения.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for (k,v) in d.items():	
        print(v)

printDict()
```

</details>

