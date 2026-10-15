def selection_sort(arr: list) -> list:
    for i in range(len(arr) - 1):
        l = find_min(arr, i)
        arr[i], arr[l] = arr[l], arr[i]
    return arr


def find_min(arr: list, left):
    min_value = arr[left]
    min_idx = left

    for i in range(left, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_idx = i

    return min_idx

arr = [240, 120, 450, 90, 310]
print(selection_sort(arr))
