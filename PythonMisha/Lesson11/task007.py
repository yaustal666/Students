row = int(input())
column = int(input())

x = []
for i in range(row):
    x.append([])

for i in x:
    for j in range(column):
        i.append(0)

for i in range(row):
    for j in range(column):
        x[i][j] = j * i

print(x)