"""

Exercise 4: Anagram Checker
Practice Problem: Write a function that determines if two strings are anagrams (contain the exact same characters in a different order).

Exercise Purpose: This problem introduces the concept of algorithmic sorting as a comparison tool.
It demonstrates that transforming data into a “canonical” or “standard” form (sorted) makes comparison trivial.

Given Input: word1 = "listen", word2 = "silent"

Expected Output: Is "listen" an anagram of "silent"? True

"""
from collections import Counter


def AnagramChecker(a : list, b: list) -> str:
    c = Counter(a.lower())
    v = Counter(b.lower())
    m = set(a.lower()) | set(b.lower())
    for i in m:
        if not c.get(i, 0) == v.get(i, 0):
            return print (f'Is {a} an anagram of {b}? False')
    return print (f'Is {a} an anagram of {b}? True')

AnagramChecker('LISTENN', 'Silent')

# return print() - либо просто делаешь print
# либо возвращаешь строку и делаешь print уже снаружи

#