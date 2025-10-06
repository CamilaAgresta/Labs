"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 4/10/25 at 13:23
Universidad Carlos III de Madrid
Student

-------
Lab 5
Exercise: 1

Create a program that generates a random number between 1 and 20, do not show this
number on the screen and keep it hidden. Then try to find out its value. As you enter values the
program must indicate if the number entered is greater or less than the one that the program
has generated and also the number of tries.
"""
import random

r_num = random.randint(1,20)
found = False

tries = 0

while found == False:
    my_num = int(input("Enter a number between 1 and 20: "))
    tries += 1
    if my_num > r_num:
        print("The number entered is greater than the one that the program has generated")
    elif my_num < r_num:
        print("The number entered is lower than the one that the program has generated")
    else:
        found = True


print("The number is:", my_num)
print("Tries:", tries)










