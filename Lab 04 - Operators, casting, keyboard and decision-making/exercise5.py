"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 3/10/25 at 18:55
Universidad Carlos III de Madrid
Student

-------
Lab 4
Exercise: 5

Write a program that prints on the screen the price of a cinema ticket according to the age of the
customer, which will be read by keyboard. (a) Normal ticket: 9 Euros; (b) Children under 5: 60% discount; (c)
People over 60: 55% discount; (d) Young people under 26: 20% discount
"""
ticket = 9
age = int(input("How old are you? "))

if age >= 0:
    if age <= 5:
        ticket -= ticket * 0.60
    elif age >= 60:
        ticket -= ticket * 0.55
    elif age <= 26:
        ticket -= ticket * 0.20
else:
    print("The age must be positive")

print("Your cinema ticket costs:", round(ticket, 2), "€")
