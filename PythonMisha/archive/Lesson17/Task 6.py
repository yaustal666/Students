"""

Exercise 6: Reverse Each Word of a String
Practice Problem: Given a sentence, reverse each individual word within the string while maintaining the original word order.

Exercise Purpose: This exercise teaches you the difference between reversing a sequence (the whole string) and 
iterating through sub-sequences (words). It emphasizes the use of the .split() and .join() methods, 
which are essential for text processing.

Given Input: "Python is awesome"

Expected Output: "nohtyP si emosewa"

"""

def reverse(a: str) -> str:
    to_return = []
    for j in a.split():
            to_return.append(j[: :-1])

    to_return = ' '.join(to_return) 
    return to_return
                
    
changed = reverse("Python is awesome")
print(changed)