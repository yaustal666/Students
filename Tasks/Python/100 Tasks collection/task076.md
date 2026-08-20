### Question 76 | Level 1

### EN
***
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

<br><br>

### RU
***
Пожалуйста, напишите программу для вывода случайного четного числа от 0 до 10 включительно, используя модуль random и списковое включение.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
import random
print(random.choice([i for i in range(11) if i%2==0]))
```

</details>

