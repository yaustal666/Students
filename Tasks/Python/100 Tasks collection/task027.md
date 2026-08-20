### Question 7 | Level 2

### EN
***
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,.., Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

<br><br>

### RU
***
Напишите программу, которая принимает 2 цифры X и Y в качестве входных данных и генерирует двумерный массив. Значение элемента в i-й строке и j-м столбце массива должно быть i*j.
Примечание: i=0,1.., X-1; j=0,1,.., Y-1.
Пример
Предположим, что на вход программе подаются следующие значения:
3,5
Тогда вывод программы должен быть:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
input_str = input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print(multilist)
```

</details>

