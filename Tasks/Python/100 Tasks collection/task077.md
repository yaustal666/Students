### Question 77 | Level 1

### EN
***
Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.

<br><br>

### RU
***
Пожалуйста, напишите программу для вывода случайного числа от 0 до 10 включительно, которое делится на 5 и 7, используя модуль random и списковое включение.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
import random
print(random.choice([i for i in range(201) if i%5==0 and i%7==0]))
```

</details>

