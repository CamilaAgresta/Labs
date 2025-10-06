"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 3/10/25 at 18:41
Universidad Carlos III de Madrid
Student

-------
Lab 4
Exercise: 4

Write a program that reads two names and two ages on the keyboard and prints who is older.
Example: if we introduce Pepe 23 and Luisa 18, it must print Pepe is older than Luisa. If they are
the same age it must print Pepe and Luisa are the same age
"""
name1 , age1 = input("Enter the first name: ") , int(input("and the first age: "))
name2 , age2 = input("Enter the second name: ") , int(input("and the second age: "))

if age1 > 0 and age2 > 0:
    if age1 > age2:
        print(name1, "is older than", name2)
    if age1 < age2:
        print(name2, "is older than", name1)
    else:
        print(name1,"and", name2,"are the same age")
else:
    print("The age must be positive")