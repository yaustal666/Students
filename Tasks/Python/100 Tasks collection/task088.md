### Question 88 | Level 1

### EN
***
By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

<br><br>

### RU
***
Используя списковое включение, пожалуйста, напишите программу для вывода списка после удаления чисел, которые делятся на 5 и 7, из [12,24,35,70,88,120,155].

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
li = [12,24,35,70,88,120,155]
li = [x for x in li if x%5!=0 and x%7!=0]
print(li)
```

</details>

