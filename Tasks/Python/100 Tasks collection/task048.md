### Question 31 | Level 1

### EN
***
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

<br><br>

### RU
***
Определите функцию, которая может принимать две строки в качестве входных данных и выводить в консоль строку с максимальной длиной. Если две строки имеют одинаковую длину, функция должна выводить все строки построчно.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def printValue(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1>len2:
        print(s1)
    elif len2>len1:
        print(s2)
    else:
        print(s1)
        print(s2)
        
printValue("one","three")
```

</details>
