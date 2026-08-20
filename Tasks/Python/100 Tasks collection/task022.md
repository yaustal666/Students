### Question 49 | Level 1

### EN
***
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

<br><br>

### RU
***
Напишите программу, которая может использовать map() для создания списка, элементы которого являются квадратами чисел от 1 до 20 (включительно).

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
squaredNumbers = map(lambda x: x**2, range(1,21))
print(squaredNumbers)
```

</details>