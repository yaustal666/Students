### Question 93 | Level 1

### EN
***
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

<br><br>

### RU
***
Имея два списка [1,3,6,78,35,55] и [12,24,35,24,88,120,155], напишите программу для создания списка, элементы которого являются пересечением указанных выше списков.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
set1=set([1,3,6,78,35,55])
set2=set([12,24,35,24,88,120,155])
set1 &= set2
li=list(set1)
print(li)
```

</details>

