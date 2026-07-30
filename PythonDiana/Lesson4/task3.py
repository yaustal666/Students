a = ""

with open("./input.txt", "r") as file:
    a = file.readlines()

for i in range(len(a)):
    a[i] = a[i].strip()

a.remove('')
['1 1', '1 1', '2 2', '2 2']
matrix1 = [a[i].split() for i in range(2)]
matrix2 = [a[i].split() for i in range(2, len(a))]

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        matrix1[i][j] = int(matrix1[i][j])
        matrix2[i][j] = int(matrix2[i][j])

matrix3 = [
    [0, 0], 
    [0, 0]
]

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

print(matrix3)
