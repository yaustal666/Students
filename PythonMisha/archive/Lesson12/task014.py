a = input()

upper = 0
lower = 0
for i in a:
    if i.isupper() == True:
        upper += 1
    if i.islower() == True:
        lower += 1

print(f"UPPER {upper} LOWER {lower}")