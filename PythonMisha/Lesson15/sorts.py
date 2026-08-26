def bubble_sort(a: list) -> list:
    for i in range(len(a) - 1):
        flag = False
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                m = a[j]
                a[j] = a[j + 1]
                a[j + 1] = m 
                flag = True
        if not flag:
            return a
    return a