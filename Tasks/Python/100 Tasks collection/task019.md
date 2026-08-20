### Question 46 | Level 1

### EN
***
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

<br><br>

### RU
***
Напишите программу, которая может использовать map() для создания списка, элементы которого являются квадратами элементов из [1,2,3,4,5,6,7,8,9,10].

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print(squaredNumbers)
```

</details>

