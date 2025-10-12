"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 9/10/25 at 17:12
Universidad Carlos III de Madrid
Student

-------
Lab 5
Exercise: 4

As you know, when we ask the user to enter a number in Python using input, we need to cast
the number to int or float to be able to work with it. But if the user enters something which
is not a number the program fails. A possible solution is to use the isdigit() function of
strings, which returns True if the string is a number (for example '3434'.isdigit() returns
True). This works for integer numbers but not for float, as the point is not recognized as a
number ('34.22'.isdigit() returns False). Create a program that asks the user to
enter a number and keeps asking until a number is introduced. At the end it prints the square
of the entered number. It must work both for integer and float numbers
"""

# NO SE COMO HACERLO SIN LISTAS

num = input("Enter a number: ")

num2 = num.split(".",2)

if len(num2) <= 1:
    num = int(num)
    print("The square of",num,"is", num**0.5)

else:
    if num2[0].isdigit() and num2[1].isdigit():
        num = float(num)
        print("The square of", num, "is", num ** 0.5)
    else:
        print(num, "it is not a number")


