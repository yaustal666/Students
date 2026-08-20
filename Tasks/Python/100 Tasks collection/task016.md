### Question 43 | Level 1

### EN
***
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

<br><br>

### RU
***
Напишите программу для генерации и вывода другого кортежа, значениями которого являются четные числа из заданного кортежа (1,2,3,4,5,6,7,8,9,10).

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
    if tp[i]%2==0:
        li.append(tp[i])

tp2=tuple(li)
print(tp2)
```

</details>