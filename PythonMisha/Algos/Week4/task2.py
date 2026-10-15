def insertion_sort(arr: list) -> list:
    
    for i in range(1, len(arr)):
        j = i - 1
        current = arr[i]
        while current < arr[j] and j >= 0:
            # arr[j], arr[j + 1] = arr[j + 1], arr[j]
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current
    return arr

arr = [6, 5, 4, 3, 2, 1]
print(insertion_sort(arr))