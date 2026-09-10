"""
exercise 5: Flatten a Nested List
Practice Problem: Write a recursive function that takes a list containing other lists (of any depth) and
returns a single “flat” list of all elements.

Exercise Purpose: Intermediate Python often involves dealing with nested data (like JSON).
This exercise teaches Recursion—the ability of a function to call 
itself—to drill down into nested structures until it finds base values.
"""

# i - element of list
# i - either number either other list
# i - number - do nothing
def flattenList(a : list) -> list:
    result = []
    for i in a:
        if not isinstance(i, int):
            result.extend(flattenList(i)) # here i have many questions because i still didnt catch this moment and the way it  it caried out
        else:
            result.append(i)
    
    return result



print(flattenList( [1, [2, 3], [4, [5, 6]], 7]))
# [1, [2, 3], [4, [5, 6]], 7] - [1, 2, 3, 4, [5, 6], 7]

