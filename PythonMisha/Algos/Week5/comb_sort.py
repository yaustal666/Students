"""Question 1: Comb Sort (Sorting Cargo Packages by Weight)
Scenario: A courier wants to sort packages on a conveyor belt from lightest to heaviest.
Since swapping adjacent packages one by one (Bubble Sort) takes too much time, 
they compare and swap packages across a wide gap starting from the ends,
gradually reducing this gap in each pass (shrink factor: 1.3) until the sorting is complete.
Your Task: Write a function that sorts the given list of weights using the Comb Sort logic.
*Use a shrink factor of 1.3 to calculate the gap size in each pass."""

def combsorting(arr: list) -> list:
    flag = False

    d = 11
    f = 1.3
    while not flag:
        d = int(d // f)

        if d <= 1:
            d = 1
            flag = True

        i = 0
        while i + d < len(arr):
            if arr[i] > arr[i + d]:
                arr[i], arr[i + d] = arr[i + d], arr[i]
                flag = False
            i += 1

    return arr

print(combsorting([13, 12, 34, 13, 65, 25]))