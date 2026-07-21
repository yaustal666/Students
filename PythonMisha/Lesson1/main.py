pool = input().split()
for i in range(0, len(pool) - 1, 2):
    pool[i], pool[i + 1] = pool[i + 1], pool[i]
print(pool)