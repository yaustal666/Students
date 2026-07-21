a = input().split()
b = input()
idx = int(input())

def insert(a: list, b, idx: int) -> None:
    # [2]-[3]-[4]
    # [2]-[3]-[4]-[any]
    # [2]-[ ]-[3]-[4]
    # [2]-[b]-[3]-[4]
    a.append(0)
    for i in range(len(a) - 1, idx, -1):
        a[i] = a[i - 1]
    a[idx] = b

insert(a, b, idx)
print(a)