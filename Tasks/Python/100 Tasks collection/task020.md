### Question 47 | Level 1

### EN
***
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

<br><br>

### RU
***
Напишите программу, которая может использовать map() и filter() для создания списка, элементы которого являются квадратами четных чисел из [1,2,3,4,5,6,7,8,9,10].

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print(evenNumbers)
```

</details>