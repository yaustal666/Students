### Question 57 | Level 1

### EN
***
Define a custom exception class which takes a string message as attribute.

<br><br>

### RU
***
Определите пользовательский класс исключения, который принимает строковое сообщение в качестве атрибута.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """
    
    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")
```

</details>

