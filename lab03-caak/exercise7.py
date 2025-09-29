"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 28/9/25 at 21:19
Universidad Carlos III de Madrid
Student

-------
Lab 3
Exercise: 7 - Copy of variables
Create two variables of any type, assign a value to the first one, and then assign the value of the first variable
to the second variable. Print the second variable on the screen. Extend the program with a new instruction
that changes the value of the first variable, and add another instruction to print the second variable again.
Does the second variable change its value? Why?
"""

int1 = 5
int2 = int1
print("value of second variable before change the first one:", int2)
int1 = 10
print("value of second variable after change the first one:", int2)

# The second variable does not change its value because when we do var1 = var2 an independent copy is created

print()
float1 = 5.2
float2 = float1
print("value of second variable before change the first one:", float2)
float1 = 9.5
print("value of second variable after change the first one:", float2)

print()
str1 = "hello"
str2 = str1
print("value of second variable before change the first one:", str2)
str1 = "world"
print("value of second variable after change the first one:", str2)

print()
bool1 = True
bool2 = bool1
print("value of second variable before change the first one:", bool2)
bool1 = False
print("value of second variable after change the first one:", bool2)