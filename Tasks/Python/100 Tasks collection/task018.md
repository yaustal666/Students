### Question 45 | Level 1

### EN
***
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

<br><br>

### RU
***
Напишите программу, которая может отфильтровать четные числа в списке с помощью функции filter. Список: [1,2,3,4,5,6,7,8,9,10].

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print(evenNumbers)
```

</details>