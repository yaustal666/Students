a = input().split()
b = input().split()

def extend(a: list, b: list) -> None:
    for i in b:
        a.append(i)

extend(a, b)
print(a)