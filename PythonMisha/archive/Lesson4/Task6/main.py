a = input().split()
b = input()
start = int(input())
end = int(input())

def index(a: list, b, start: int = 0, end: int = None) -> int:
    if end == None:
        end = len(a)
    
    if end > len(a):
        end = len(a)

    for i in range(start, end):
        if b == a[i]:
            return i
    
    return None

print(index(a, b, start, end))