### Question 89 | Level 1

### EN
***
By using list comprehension, please write a program to print the list after removing elements under indexes that divides by 4.

<br><br>

### RU
***
Используя списковое включение, пожалуйста, напишите программу для вывода списка после удаления элементов, чьи индексы кратны четырем.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%4!=0]
print(li)
```

</details>

