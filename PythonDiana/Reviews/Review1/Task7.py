# Здесь все ок
# единственное обычно если вложенный цикл то переменные называют i j k, дальше обычно не бывает

n = int(input())  #seventh quesyion
count = 0
for i in range(1, 5):
    for a in range(1, 5):
        for b in range(1, 5):
            print(i, a, b)
            if a + b + i == n:
                count += 1
print(count)