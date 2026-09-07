"""

Exercise 4: Student Class with Average Grade

Problem Statement: Write a Python program to create a Student class that stores a student’s name and a list of marks. 
Add a method average() that calculates and returns the average of all marks.

Purpose: This exercise shows how instance attributes can store complex data types such as lists, not just simple values. 
It also practices combining OOP with list operations and arithmetic, a pattern common in gradebooks, dashboards, and reporting tools.

Given Input: s1 = Student("Alice", [85, 90, 78, 92, 88])

Expected Output: Alice's Average Grade: 86.6

"""

class Student:
    
    def __init__(self, name, marks: list):
        self.name = name
        self.marks = marks
        
    def average(self):
       return  sum(self.marks) / len(self.marks)
    
Student1 = Student("Alice", [85, 90, 78, 92, 88])
print(f"{Student1.name}'s Average Grade : {Student1.average()}")
            