"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 3/10/25 at 20:22
Universidad Carlos III de Madrid
Student

-------
Lab 4
Exercise: 9

Create a program that calculates and shows the final salary of a worker depending on the base
salary and seniority according to the following rules:
    a. Ask the user about the base salary. If the base salary is bigger or equal than 1000 just show it as
        the final salary.
    b. If the base salary is less than 1000, ask the user about the seniority (only ask about it in this case!)
        - If seniority is at least 10 years, the salary will be increased by 20%.
        - If seniority is less than 10 years, the salary will be increased by 5%.

Example of output:
Final salary of the worker is: XXX Euros
"""

salary = int(input("Enter your base salary: "))

if 0 < salary < 1000:
    seniority = int(input("How long have you been with the company? "))
    if 0 < seniority < 10:
        salary += salary*0.05
    else:
        salary += salary * 0.20

print("salary of the worker is:",salary, "Euros")
