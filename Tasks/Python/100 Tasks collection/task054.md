### Question 54 | Level 1

### EN
***
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

<br><br>

### RU
***
Определите класс с именем Shape и его подкласс Square. Класс Square имеет функцию init, которая принимает длину в качестве аргумента. Оба класса имеют функцию area, которая может выводить площадь фигуры, при этом площадь Shape по умолчанию равна 0.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare = Square(3)
print(aSquare.area())
```

</details>

