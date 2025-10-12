"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 10/10/25 at 12:05
Universidad Carlos III de Madrid
Student

-------
Lab 5
Exercise: 5

Define a program that allows simulating the behavior of an ATM. The program must meet the
following requirements
    - Randomly create a 4-digits PIN number and the account balance, which must be in the range
        50 to 5,000 Euros. Notice that the PIN must be stored as string, otherwise any leading zero it
        may have will be lost.
    - Request the corresponding PIN code to the user, giving up to three attempts to enter the
        correct number. In case of failing three times the program will show a message on the screen
        and finish.
    - If the pin is correct it must show a menu with the different operations that the ATM allows, as
        seen in the next example:
            Welcome
            ------------------------
            1- Deposit
            2- Cash withdrawal
            3- Exit
            Choose the operation:
After each operation, indicate on the screen the available balance in the account. If the cash
withdrawal operation exceeds the amount available in the bank account, the operation will be
denied and the corresponding message will be displayed.
"""
import random

pin = ""

for i in range(4):
    pin += str(random.randint(0,9))

#print(pin)

balance = random.randint(50,5000)

user_pin = input("Enter your PIN: ")

#print(pin == user_pin)

#while pin != user_pin:
