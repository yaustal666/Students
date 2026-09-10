from collections import Counter

a = Counter("heEllo".lower())
for i, v in a.items():
    print(i, v)
    
    
def dictMerge(a: dict, b: dict) -> dict:
    all_keys = set(a) | set(b)
    merged = {}
    for y in all_keys:
        merged[y] = a.get(y, 0) + b.get(y, 0)
    return merged
        
def merge(a: dict, b):
    res = b.copy()
    for k, v in a.items():
        if res.get(k) is None:
            res[k] = v
        else:
            res[k] += v
    return res

('b', 25)
d = {'b': 25, 'c': 15, 'a': 10}
print(
    dict(
        sorted(
                d.items(), 
                key = lambda item: item[1]
            )
    )
)