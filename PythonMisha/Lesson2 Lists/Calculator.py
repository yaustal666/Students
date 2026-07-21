#Calculator 

while True:
    # следующий формат 1 2 +
    print('What is the next calculation?')
    command = input().split()

    # Проверка на exit именно тут, иначе мы предлагаем пользователю 
    # ввести все числа и после этого программа внезапно закрывается
    if len(command) == 1 and command[0] == 'exit':
        break

    a, b, type = command
    a = float(a)
    b = float(b)
    # либо
    # a = float(command[0])
    # b = float(command[1])
    # type = command[2]

    if type == '+':
         result = a + b
         print(result)

    if type == '-':
        result = a - b
        print(result)

    if type == '*':
        result = a * b
        print(result)
        
    if type == '/':
        result = a / b
        print(result) 
        
         