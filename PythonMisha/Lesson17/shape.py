import math

class Rectangle:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    
    def area(self):
        result = self.a * self.b
        return result


class Circle:
    def __init__(self, r: int):
        self.R = r
    
    def area(self):
        result = self.R ** 2 * 3.14
        return result

class Vector2:
    def __init__(self, x, y):
        pass

    def zero():
        return Vector2(0, 0)

circle = Circle(5)
print(circle.area())

recteangle = Rectangle(4,9)
print(recteangle.area())

