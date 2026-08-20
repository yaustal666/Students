### Question 80 | Level 1

### EN
***
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7, between 1 and 1000 inclusive.

<br><br>

### RU
***
Пожалуйста, напишите программу для случайной генерации списка из 5 чисел от 1 до 1000 включительно, которые делятся на 5 и 7.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))
```

</details>