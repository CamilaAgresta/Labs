"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 3/10/25 at 18:37
Universidad Carlos III de Madrid
Student

-------
Lab 4
Exercise: 3

Write a program that reads two integer numbers on the keyboard and shows the result of dividing
the first by the second. If the second is zero, instead of performing the division it will print
"Cannot divide by zero"
"""

print("we are going to divide one number by another")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if b == 0:
    print("Cannot divide by zero")
else:
    print("a/b =", a/b)
