"""

Task 1: Temperature Converter (map + lambda)
Goal: Given a list of temperatures in Celsius, convert each temperature to Fahrenheit using map() and a lambda function.

Formula: Fahrenheit=(Celsius×9/5)+32

Given Input: celsius = [0, 20, 37, 100]

Expected Output: [32.0, 68.0, 98.6, 212.0]

"""

celsius = [0, 20, 37, 100]
converter = list(map(lambda x: (x * 9 / 5) + 32,celsius))
print(converter)

"""

Task 2: Word Length Filter (filter + lambda)
Goal: Write a filter() function with a lambda to keep only words that have 5 or more letters.

Given Input: words = ["cat", "elephant", "dog", "tiger", "lion", "giraffe"]

Expected Output: ['elephant', 'tiger', 'giraffe']

"""

words = ["cat", "elephant", "dog", "tiger", "lion", "giraffe"]
filtered = list(filter(lambda x: len(x) >= 5 ,words))
print(filtered)

"""
Task 3: Validation Checker (all & any)
Goal: Given a list of numbers, check:

Are all numbers positive (>0)?

Is any number greater than 50?

Given Input: scores = [15, 88, 42, 9, 61]

Expected Output:

All positive: True

Any over 50: True
"""

scores = [15, 88, 42, 9, 61]
positivity = all(map(lambda x: x > 0 , scores))
greater_50 = any(map(lambda x: x > 50 , scores))
print(positivity)
print(greater_50)