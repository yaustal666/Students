### Question 64 | Level 1

### EN
***
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

3.55

<br><br>

### RU
***
Напишите программу для вычисления 1/2+2/3+3/4+...+n/n+1 с заданным n, введенным с консоли (n>0).

Пример:
Если на вход программе подается следующее значение n:

5

Тогда вывод программы должен быть:

3.55

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
n=int(input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(sum)
```

</details>

