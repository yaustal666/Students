### Question 56
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions.

Solution:
<details>

<summary> Click to extend </summary>

```python
def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except Exception, err:
    print('Caught an exception')
finally:
    print('In finally block for cleanup')
```

</details>

