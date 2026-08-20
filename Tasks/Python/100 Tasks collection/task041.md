### Question 21 | Level 3

### EN
***
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
...
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

<br><br>

### RU
***
Робот движется по плоскости, начиная с исходной точки (0,0). Робот может двигаться в направлениях UP, DOWN, LEFT и RIGHT на заданное количество шагов. Траектория движения робота показана ниже:
UP 5
DOWN 3
LEFT 3
RIGHT 2
...
Числа после направления — это количество шагов. Пожалуйста, напишите программу для вычисления расстояния от текущей позиции после последовательности движений до исходной точки. Если расстояние является дробным числом, выведите ближайшее целое число.
Пример:
Если на вход программе поданы следующие кортежи:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Тогда вывод программы должен быть:
2

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
```

</details>

