### Question 3 | Level 1

### EN
***
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

<br><br>

### RU
***
Дано целое число n. Напишите программу, которая генерирует словарь, содержащий пары (i, i*i) для всех целых чисел i от 1 до n включительно, а затем выводит этот словарь.
Предположим, что на вход программе подается число:
8
Тогда вывод должен быть:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)
```

</details>