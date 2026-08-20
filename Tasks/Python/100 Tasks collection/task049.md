### Question 32 | Level 1

### EN
***
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

<br><br>

### RU
***
Определите функцию, которая может принимать целое число в качестве входных данных и выводить "It is an even number" (это четное число), если число четное, иначе выводить "It is an odd number" (это нечетное число).

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
def checkValue(n):
    if n%2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
        
checkValue(7)
```

</details>