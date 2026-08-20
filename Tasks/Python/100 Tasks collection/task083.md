### Question 83 | Level 1

### EN
***
Please write a program to print the running time of execution of "1+1" for 100 times.

<br><br>

### RU
***
Пожалуйста, напишите программу для вывода времени выполнения операции "1+1" 100 раз.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
from timeit import Timer
t = Timer("for i in range(100):1+1")
print(t.timeit())
```

</details>

