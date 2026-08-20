### Question 56 | Level 1

### EN
***
Write a function to compute 5/0 and use try/except to catch the exceptions.

<br><br>

### RU
***
Напишите функцию для вычисления 5/0 и используйте try/except для перехвата исключений.

<br><br>

<details>  
<summary>Solution/Решение</summary>

```python
def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except Exception as err:
    print('Caught an exception')
finally:
    print('In finally block for cleanup')
```

</details>

