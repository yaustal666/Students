a = input().split()
deposit = 0
for i in range(0, len(a), 2):
    command = a[i]
    value = int(a[i + 1])

    if command == 'D':
        deposit += value
    if command == 'W':
        deposit -= value
print(deposit)