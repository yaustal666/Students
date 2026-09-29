"""
3) School Library Queue Number Search Simulation
In a school library during exam week, 100 students are waiting at the door to enter, and each student is assigned a queue number sequentially from 1 to 100.

The teacher on duty wants to design a search algorithm that checks the list step-by-step starting from the first person to find a specific queue number.

Design the Function:
 Write a function using def that accepts two parameters (n: total number of people,  target: the number to find).

The function should count one step for each person checked and return the total number of operations performed once the number is found or the list is exhausted.
How many steps are taken when searching for student number 1?
How many steps are taken when searching for student number 50?
How many steps are taken when searching for student number 100?
What happens when searching for student number 999, who is not in line at all?
"""

from time import time


def queue_search(snts: int, num: int) -> str:
    if num > snts:
        raise ValueError(f"{num} exceeds the quantity of awaiting students")

    counter = 0
    while counter != num:
        counter += 1
    return f"Amount of steps taken:{counter}"


start = time()
queue_search(100, 1)
queue_search(100, 50)
queue_search(100, 100)
end = time()

print(f"execution time:{(end - start) * 1000}")

print(queue_search(100, 999))

# queue_search(100, 999)

# try:
#     queue_search(100, 999)
# except ValueError as e:
#     print("Error", e)

# print("After error")
