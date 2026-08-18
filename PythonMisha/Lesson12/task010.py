a = input().split()
b = []

for i in a:
    if not i in b:
        b.append(i)

# a = list(set(a))

b.sort()
print(' '.join(b))