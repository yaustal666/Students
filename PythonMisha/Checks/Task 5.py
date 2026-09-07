"""

Exercise 5: Product Class with Stock Value Calculator
Problem Statement: Write a Python program to create a Product class with three instance attributes: 
name, price, and quantity. Add a method total_value() that returns the total stock value by multiplying price by quantity.

Purpose: This exercise models a real-world business scenario using OOP. 
It reinforces how instance methods can derive new information from existing attributes, a pattern widely used in inventory management,
e-commerce, and financial applications.

Given Input: p1 = Product("Laptop", 899.99, 5)

Expected Output: Total stock value of Laptop: $4499.95

"""

class Product:
    
    def __init__(self, name, price, quality):
        self.name = name
        self.price = price
        self.quality = quality

    def total_value(self):
        result = self.price * self.quality
        return result
    
s1 = Product("Laptop", 899.99, 5)
print('$',s1.total_value())