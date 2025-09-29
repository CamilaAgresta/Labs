"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 28/9/25 at 21:09
Universidad Carlos III de Madrid
Student

-------
Lab 3
Exercise: 5 - Float precision
Declare two float variables. Initialize the first variable with the value 12345678901234567.0 and the
second one with 12345678901234568.0. Print the result of their subtraction. What is the result? Repeat
the same procedure with two integer variables (removing the decimal part). What is the result? Why?
Print the result of the operation 0.3 - 0.2. What happens?
"""

float1 = 12345678901234567.0
float2 = 12345678901234568.0

print("second float minus the first:", float2 - float1)
# The result is 0.0
# The precission limit of float variables is 16 digit

int1 = 12345678901234567
int2 = 12345678901234568

print("second int minus the first:", int2 - int1)
# The result is 1
# The integer type variable doesn't have a precission limit

print("0.3 - 0.2 =", 0.3 - 0.2)
# The result is 0.09999999999999998
