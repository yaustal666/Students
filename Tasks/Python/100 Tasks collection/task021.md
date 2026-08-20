### Question 48 | Level 1

### EN
***
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

<br><br>

### RU
***
Напишите программу, которая может использовать filter() для создания списка, элементы которого являются четными числами от 1 до 20 (включительно).

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(evenNumbers)
```

</details>

