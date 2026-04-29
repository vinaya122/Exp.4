# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:40:04 2026

@author: Agce
"""

# Taking list input from the user
n = int(input("Enter numbers of elements:"))
numbers = []
   
for i in range(n):
  num = int(input(f"Enter elements{i+1}:"))
  numbers.append(num) 

# Calculating sum and average
total = sum(numbers) 
average = total / n if n > 0 else 0
 
print("List:",numbers)
print("Sum of elements:",total) 
print("Average of elements:", average)         
