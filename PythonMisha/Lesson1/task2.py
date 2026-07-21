pool = input().split()

# for i in pool - когда ты хочешь Только читать список
# for i in range() - когда ты хочешь и читать и писать и что угодно. Ты просто генерируешь индексы 

for i in range(0, len(pool)):
    pool[i] = int(pool[i])

print(pool)

minimum = int(pool[0])
maximum = int(pool[0])

maxIndex = 0
minIndex = 0

for i in range(0, len(pool)):
    nums = int(pool[i])
    if nums > maximum:
        maximum = nums
        maxIndex = i
    if nums < minimum:
        minimum = nums
        minIndex = i

pool[maxIndex], pool[minIndex] = pool[minIndex], pool[maxIndex]
print(pool)

# 12 13 *
# 166
# 45 7 +
# 52
# exit
# terminate