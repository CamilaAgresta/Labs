"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 4/10/25 at 12:07
Universidad Carlos III de Madrid
Student

-------
Lab 4
Exercise: 13

Create a program that asks a number and states if it is a multiple of 2, 3 and/or 5
or not a multiple of any of them. Examples of execution:
    Enter your number 30
    It is a multiple of 2
    It is a multiple of 3
    It is a multiple of 5

    Enter your number 15
    It is a multiple of 3
    It is a multiple of 5

    Enter your number 7
    Not a multiple of 2, 3 nor 5
"""

number = int(input("Enter your number: "))

if number % 2 == 0:
    print("It is a multiple of 2")
if number % 3 == 0:
    print("It is a multiple of 3")
if number % 5 == 0:
    print("It is a multiple of 5")
#elif  number % 2 != 0 and number % 3 != 0 and number % 5 != 0:
else:
    print("Not a multiple of 2, 3 nor 5")