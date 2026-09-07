"""

Exercise 6: Bank Account with Deposit & Overdraw Protection

Problem Statement: Write a Python program to create a BankAccount class with a balance attribute and two methods: deposit(amount) that adds funds to the balance,
and withdraw(amount) that deducts funds but prevents the balance from going below zero.

Purpose: Learn data validation and conditional logic inside instance methods. 
Preventing overdraw is a real-world business rule, and implementing it here teaches you how classes can enforce constraints on their own data, 
a core idea behind encapsulation in OOP.

Given Input: Starting balance of 1000, deposit 500, withdraw 200, then attempt to withdraw 2000.

"""
from pydantic import BaseModel


class BankAccount(BaseModel):
    balance: int

    def deposit(self, top_up):
        self.balance += top_up
        return self.balance
    
    def withdraw(self, withdraw):
        if withdraw > self.balance:
            print('insufficient deposit to withdraw') 
        else:
            self.balance -= withdraw
            return self.balance


class Bankaccount:
    
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, top_up):
        self.balance += top_up
        return self.balance
    
    def withdraw(self, withdraw):
        if withdraw > self.balance:
            print('insufficient deposit to withdraw') 
        else:
            self.balance -= withdraw
            return self.balance

account1 = Bankaccount(1000)
print(account1.withdraw(600))

