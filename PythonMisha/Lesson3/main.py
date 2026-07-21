table = [[0, 0, 0, 0, 0] for i in range(5)]

# [0, 1, 2, 3, 4]
# [1, 2, 3, 0, 5]
# [0, 0, 4, 5, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 8]

for i in range(len(table)):
    for j in range(len(table[i])):
        table[i][j] = i + j

for i in table:
    print(*i)