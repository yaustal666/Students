# Question 2: Counting Sort (Sorting Customer Ratings)
# Scenario: A restaurant wants to sort anonymous ratings given by customers, 
# which range from 0 to 5. Since the values fall within a narrow integer range (0–5), 
# instead of comparing elements individually, they use an algorithm that counts the 
# frequency of each rating (Counting Sort).

def counting_sort(arr: list) -> list:
    a = [0, 0, 0, 0, 0, 0]
    result = [0 for _ in range(len(arr))]

    for i in arr:
        a[i] += 1

    for i in range(1, len(arr)):
        a[i] = a[i] + a[i-1] - 1

    for i in range(len(arr) - 1, -1, -1):
        result[a[arr[i]]] = arr[i]
        a[arr[i]] -= 1

    return result 

# arr = [1, 0, 1, 0, 2, 2, 2, 1]
# result = [0, 0, 1, 1, 1, 2, 2, 2]

# a = [2, 3, 3]
# a = [2, 5, 8] - 1 = [1, 4, 7]

# res = []
# i = 7
# arr[i] = 1 ? where
# a[arr[i]] - 4
# res[4] = 1
# res[a[arr[i]]] = arr[i]