"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 28/9/25 at 22:08
Universidad Carlos III de Madrid
Student

-------
Lab 3
Exercise: 9 - Division by zero
Declare three int variables. Assign 5 to the first one and 0 to the second one. Assign to the third variable
the result of dividing the first variable by the second one. Print the result on the screen. Is there an error?
Why? Does the result change if the variables are declared as float instead?
"""
int1 = 5
int2 = 0
result = int1 / int2
print("int1 / int2 =", result)

# The program gives an error ZeroDivisionError: division by zero

float1 = 5.0
float2 = 0.0
result2 = float1 / float2
print("float1 / float2 =", result2)

# gives the same error
