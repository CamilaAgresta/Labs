"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 3/10/25 at 20:04
Universidad Carlos III de Madrid
Student

-------
Lab 4
Exercise: 7

Write a program that reads a single character on the keyboard and prints on the screen if "It
is a number" or "It is not a number".
"""

numbers = "0123456789"

character = input("Enter a single character: ")

if character in numbers:
    print("It is a number")
else:
    print("It is not a number")