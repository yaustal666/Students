### Question 37 | Level 1

### EN
***
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

<br><br>

### RU
***
Определите функцию, которая может генерировать и выводить список, где значения являются квадратами чисел от 1 до 20 (включительно).

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li)

printList()
```

</details>