### Question 90 | Level 1

### EN
***
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

<br><br>

### RU
***
Используя списковое включение, пожалуйста, напишите программу для генерации 3D массива размером 3*5*8, каждый элемент которого равен 0.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)
```

</details>