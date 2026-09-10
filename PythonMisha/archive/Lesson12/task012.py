def check(a : str) -> list:
    even = []
    for i in a:
        if int(i) % 2 == 0:
            even.append(i)
        else:
            return []
    return even    
            
for i in range(1000, 3001):
    a = str(i)
    res = check(a)
    if res != []:
        print(",".join(res))

