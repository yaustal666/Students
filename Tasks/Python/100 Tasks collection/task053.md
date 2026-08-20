### Question 53 | Level 1

### EN
***
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

<br><br>

### RU
***
Определите класс с именем Rectangle, который может быть создан с длиной и шириной. Класс Rectangle имеет метод, который может вычислить площадь.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print(aRectangle.area())
```

</details>

