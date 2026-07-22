# Я так понимаю это задание на поиск площади. Но я не вижу здесь вычисления площади
# Площадь прямоугольника это длина на высоту
# Используя данные координаты можно найти ширину и высоту и перемножить их

rec1 = float(input('x1 :'),), float(input('y1 :'))
rec2 = float(input('x2 :'),), float(input('y2 :'))
rec3 = float(input('x3 :'),), float(input('y3 :'))
rec4 = float(input('x4 :'),), float(input('y4 :'))

def coord(rec1: float, rec2: float, rec3: float, rec4: float):
    squares = []
    for i,j in rec1 , rec2, rec3, rec4:
        result = i * j 
        squares.append(result)
        print(squares)
coord(rec1, rec2, rec3, rec4)    #!!! loops over all previous nums and print them - mistake