"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 4/10/25 at 11:04
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
notes_coins = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.20, 0.10, 0.05, 0.02, 0.01]

if money < 0.01:
    print("Sorry, this amount is to low")

else:
    while money > 0:
        n = 0
        for i in range(len(notes_coins)):
            n = money//notes_coins[i]
            money = round(money - n * notes_coins[i], 2)
            if n > 0:
                print(notes_coins[i],"€: ", round(n), sep="")
