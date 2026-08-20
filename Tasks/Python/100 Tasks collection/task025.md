### Question 5 | Level 1

### EN
***
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

<br><br>

### RU
***
Определите класс, который имеет как минимум два метода:
getString: для получения строки с консольного ввода
printString: для вывода строки в верхнем регистре.
Также включите простую тестовую функцию для проверки методов класса.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()
```

</details>

