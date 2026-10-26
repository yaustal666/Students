"""Question 4: Bucket Sort (Sorting Exam Scores into Ranges)
Scenario: A teacher wants to sort exam scores ranging from 0 to 100. 
They first distribute the scores into 5 different buckets based on score ranges
(0–19, 20–39, 40–59, 60–79, 80–100), sort each bucket internally, and then combine them.
Your Task: Write a Bucket Sort function that distributes scores into buckets, sorts them, 
and concatenates the result."""

def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        j = i - 1
        current = arr[i]
        while current < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current
    return arr

def bucket_sort(arr : list) -> list:
    # раскидать по бакетам
        # Как создать бакеты?
    buckets = [[] for i in range(5)]
    
        # Как распрелделить числа по бакетам?

    for number in arr:
        b = 0
        e = 19
        for j in range(len(buckets)):
            if number > b + 20 * j and number < e + 20 * j:
                buckets[j].append(number)
            
    # отсортировать бакеты
    for i in range(len(buckets)):
        buckets[i] = insertion_sort(buckets[i])
        
    # собрать
    # result = [i for i in buckets[j] for j in range(5)]

    result = []
    for i in buckets:
        for j in i:
            result.append(j)

    return result

print(bucket_sort([13, 12, 34, 13, 65, 25]))