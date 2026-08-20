### Question 39 | Level 1

### EN
***
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

<br><br>

### RU
***
Определите функцию, которая может генерировать список, где значения являются квадратами чисел от 1 до 20 (включительно). Затем функция должна вывести последние 5 элементов списка.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li[-5:])

printList()
```

</details>