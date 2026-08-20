### Question 87 | Level 1

### EN
***
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

<br><br>

### RU
***
Пожалуйста, напишите программу для вывода списка после удаления четных чисел из [5,6,77,45,22,12,24].

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
li = [5,6,77,45,22,12,24]
li = [x for x in li if x%2!=0]
print(li)
```

</details>

