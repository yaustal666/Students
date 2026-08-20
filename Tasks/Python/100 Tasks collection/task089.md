### Question 89 | Level 1

### EN
***
By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th, 6th numbers in [12,24,35,70,88,120,155].

<br><br>

### RU
***
Используя списковое включение, пожалуйста, напишите программу для вывода списка после удаления 0-го, 2-го, 4-го, 6-го чисел из [12,24,35,70,88,120,155].

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print(li)
```

</details>

