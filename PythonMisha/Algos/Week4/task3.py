def bubble_sort(arr: list):
    n = len(arr)

    for i in range(n - 1):
        flag = True

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                flag = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if flag:
            return arr
    return arr

# O(n^2) if we sort number. O(1) * O(n^2) = O(n^2)
# if string? O(m) * O(n^2) = O(m*n^2)