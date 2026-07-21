import copy

matrix1 = []
matrix2 = []
x, y = 0, 0

with open("input.txt", "r") as file:
    x, y = [int(x) for x in file.readline().strip().split()]
    file.readline()

    for i in range(x):
        matrix1.append([int(x) for x in file.readline().strip().split()])
    
    file.readline()

    for i in range(x):
        matrix2.append([int(x) for x in file.readline().strip().split()])

matrix3 = copy.deepcopy(matrix1)

for i in range(x):
    for j in range(y):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

print(matrix1)
print(matrix2)
print(matrix3)

# with open("output.txt", "w") as file:
#     for i in matrix3:
#         for j in i:
#             file.write(str(j))
#             file.write(" ")
#         file.write("\n")