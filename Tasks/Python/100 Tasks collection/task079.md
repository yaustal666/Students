### Question 79 | Level 1

### EN
***
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

<br><br>

### RU
***
Пожалуйста, напишите программу для случайной генерации списка из 5 четных чисел от 100 до 200 включительно.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
import random
print(random.sample([i for i in range(100,201) if i%2==0], 5))
```

</details>

