array = [10,3,5,4,6,8,9,7,0,-100]
from archive.Lesson15.sorts import bubble_sort

array = bubble_sort(array)

def bin_search(a: list, n: int) -> int:
    R = len(a) - 1
    L = 0

    while L <= R:
        m = (R - L) // 2

        if n == a[L + m]:
            return L + m
        
        if n > a[L + m]:
            L = L + m + 1
            continue

        if n < a[L + m]:
            R = R - m - 1

    return -1
                      
        
print(bin_search(array, 7))