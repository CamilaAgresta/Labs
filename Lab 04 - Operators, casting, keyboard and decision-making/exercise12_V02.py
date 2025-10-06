"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 4/10/25 at 12:01
Universidad Carlos III de Madrid
Student

-------
Lab 4
Exercise: 12

Create a program to simulate a calculator.
It must ask for two numbers and the operator (+ - * / // **) and show the result.
If the operator is not a valid one, it must print “wrong operator” and finish.
"""

print("Simulation of a calculator: Enter two numbers and the operator")

a = float(input("First number: "))
operator = input("Operator: ")
b = float(input("Second number: "))

operators = ["+", "-", "/", "//", "**"]

if operator in operators:
    #for i in range(len(operators)):
        #if operator == operators[i]:
            #result = no se

    res = 0
    if operator == "+":
        res = a + b
    elif operator == "-":
        res = a - b
    elif operator == "*":
        res = a * b
    elif operator == "/":
        res = a / b
    elif operator == "//":
        res = a // b
    elif operator == "**":
        res = a ** b

else:
    print("wrong operator")
