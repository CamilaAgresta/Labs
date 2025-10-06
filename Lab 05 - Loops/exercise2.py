"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 4/10/25 at 14:16
Universidad Carlos III de Madrid
Student

-------
Lab 5
Exercise: 2

Ask the user two integer numbers A and B such as A + 5 < B. Keep asking until the former
condition is met. Then randomly generate and print 5 integer numbers in the interval [A,B]
such as they are even and odd in an alternative way. It does not matter if the values are
repeated; the aim is alternatively printing odd and even numbers.
Example: for the interval [3,9] a valid sequence of numbers is: 6, 7, 6, 3, 4
"""
import random

print("Enter two integer numbers A and B such as A + 5 < B")
condition = False

while not condition:
    a = int(input("A: "))
    b = int(input("B: "))
    if a + 5 < b:
        condition = True

        sequence = ""
        n = 0
        while n < 5 :
            num = random.randint(a,b)
            if num % 2 == 0:
                sequence += num
                n += 1

