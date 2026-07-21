someList = [[0, 0, 0] for i in range(4)]


for i in range(4):
    for j in range(3):
        someList[i][j] = i + j

for i in someList:
    print(*i)