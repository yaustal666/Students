def compress_noorder(a : str) -> str:
    listed = [i for i in a]

    dicted = [("A", 2), ("B", 3), ("A", 5)]

    for i in listed:
        if not i in dicted:
            dicted[i] = 1
        else:
            dicted[i] += 1

    s = ''.join((f"{j}{i}"  for i ,j in dicted.items()))
    return s
# print(compress_noorder('АААААБББББООРРБББББЛЛЛ'))

def comp_next(a: str) -> str:
    tupl = []
    count = 1
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            count += 1
            if i == len(a) - 2:
                tupl.append((a[i], count))
        else:
            tupl.append((a[i], count))
            count = 1
            if i == len(a) - 2:
                tupl.append((a[i+1], 1))
            
    return tupl
# print(comp_next('АААААБББББООРРБББББЛЛЛРР'))

def comp_prev(a: str) -> str:
    res = ""
    prev = a[0]
    count = 1

    for i in range(1, len(a)):
        if a[i] == prev:
            count += 1
            prev = a[i]
        else:
            res += str(count) + prev
            count = 1
            prev = a[i]

        if i == len(a) - 1:
            res += str(count) + a[i]

    return res
print(comp_prev('ААААААААААААААААААААААААААААААААБББББООРРБББББЛЛЛР'))

message = comp_prev('ААААААААААААААААААААААААААААААААБББББООРРБББББЛЛЛР')

"1000A2000B"
def decompress(a : str) -> str:
    transformed = []
    number = ""
    for i in range(len(a)):
        if a[i].isdigit():
            number += a[i]
        else:
            transformed.append(a[i] * int(number))
            number = ""
         
    return ''.join(transformed)

print(decompress(message))