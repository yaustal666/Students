### Question 91 | Level 1

### EN
***
By using list comprehension, please write a program to print the list after removing the 0th, 4th, 5th numbers in [12,24,35,70,88,120,155].

<br><br>

### RU
***
Используя списковое включение, пожалуйста, напишите программу для вывода списка после удаления 0-го, 4-го, 5-го чисел из [12,24,35,70,88,120,155].

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print(li)
```

</details>

