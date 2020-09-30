# CS1501: Tools of the Trade
# Week 6 - Testing
# Python Implementation of Week Demo
# Source: https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/ 




# The Bank Account Class

# Python program using OOP concept to perform some simple bank operations like deposit and withdrawal of money.

class Bank_Account: 
    def __init__(self): 
        self.balance=0
        print("Instance created of the Bank Account Machine.") 
  
    def deposit(self, amount): 
        self.balance += amount 
        return "Amount Deposited: " + str(amount)
  
    def withdraw(self, amount): 
        self.balance-=amount 
        return "You Withdrew: " + str(amount)
  
    def display(self): 
        return "Your Available Balance= " + str(self.balance)
  
# Driver code 
   
# creating an object of class 
s = Bank_Account() 
   
# Calling functions with that class object 
s.deposit(50000) 
s.withdraw(10000) 
s.display() 