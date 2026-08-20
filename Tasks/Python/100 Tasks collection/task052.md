### Question 52 | Level 1

### EN
***
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

<br><br>

### RU
***
Определите класс с именем Circle, который может быть создан с радиусом. Класс Circle имеет метод, который может вычислить площадь.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print(aCircle.area())
```

</details>

