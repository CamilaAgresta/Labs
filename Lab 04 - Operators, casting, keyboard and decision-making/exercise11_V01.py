"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 4/10/25 at 10:35
Universidad Carlos III de Madrid
Student

-------
Lab 4
Exercise: 11

Create a program that receives as input a positive number, which will correspond to a quantity of money,
and calculates and prints the minimum number of notes and coins for it. If the quantity of any coin or
note is zero it must not be printed.
    - Notes: 500, 200, 100, 50, 20, 10 and 5€
    - Coins: 2, 1, 0.5, 0.20, 0.10, 0.05, 0.02 and 0.01€

Example, if 348.07 is introduced it should print:
    200€: 1
    100€: 1
    20€: 2
    5€: 1
    2€: 1
    1€: 1
    0.05€: 1
    0.02€: 1
"""

money = float(input("Enter a quantity of money: "))

if money < 0.01:
    print("Sorry, this amount is to low")

else:

    if money >= 500:
        n500 = money//500
        money -= n500 * 500
        print("500€:", int(n500))
    if money >= 200:
        n200 = money//200
        money -= n200 * 200
        print("200€:", int(n200))
    if money >= 100:
        n100 = money//100
        money -= n100 * 100
        print("100€:", int(n100))
    if money >= 50:
        n50 = money//50
        money -= n50 * 50
        print("50€:", int(n50))
    if money >= 20:
        n20 = money//20
        money -= n20 * 20
        print("20€:", int(n20))
    if money >= 10:
        n10 = money//10
        money -= n10 * 10
        print("10€:", int(n10))
    if money >= 5:
        n5 = money//5
        money -= n5 * 5
        print("5€:", int(n5))
    if money >= 2:
        n2 = money//2
        money -= n2 * 2
        print("2€:", int(n2))
    if money >= 1:
        n1 = money//1
        money -= n1 * 1
        print("1€:", int(n1))
    if money >= 0.5:
        n05 = money//0.5
        money -= n05 * 0.5
        print("0.5€:", int(n05))
    if money >= 0.2:
        n02 = money//0.2
        money -= n02 * 0.2
        print("0.20€:", int(n02))
    if money >= 0.1:
        n01 = money//0.1
        money -= n01 * 0.1
        print("0.10€:", int(n01))
    if money >= 0.05:
        n005 = money//0.05
        money -= n005 * 0.05
        print("0.05€:", int(n005))
    if money >= 0.02:
        n002 = money//0.02
        money -= n002 * 0.02
        print("0.02€:", int(n002))
    if money >= 0.01:
        n001 = money//0.01
        money -= n001 * 0.01
        print("0.01:", int(n001))



