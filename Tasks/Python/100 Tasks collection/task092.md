### Question 92 | Level 1

### EN
***
By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

<br><br>

### RU
***
Используя списковое включение, пожалуйста, напишите программу для вывода списка после удаления значения 24 из [12,24,35,24,88,120,155].

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print(li)
```

</details>

