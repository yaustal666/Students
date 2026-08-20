### Question 94 | Level 1

### EN
***
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

<br><br>

### RU
***
Имея список [12,24,35,24,88,120,155,88,120,155], напишите программу для вывода этого списка после удаления всех дубликатов с сохранением исходного порядка.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(li))
```

</details>

