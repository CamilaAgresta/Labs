"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 12/10/25 at 21:26
Universidad Carlos III de Madrid
Student

-------
Lab 5
Exercise: 7

Create a program which plays "Rock, paper, scissors", with the next specifications:
    • There will be one player who plays against the machine.
    • The number of games will be a constant in the program. The game will be repeated the
        number of times indicated in this constant.
    • The following message will be shown in order to ask the user for the move:
            ROCK, PAPER OR SCISSORS?
The program will randomly obtain the move (rock, paper or scissors). The program will show
the winner according to the following rules:
    ▪ Rock crushes scissors (Rock wins)
    ▪ Scissors cuts paper (Scissors wins)
    ▪ Paper wraps stone (Paper wins)
    ▪ In case of tie, the message “TIE” will be shown
"""
import random
from platform import machine

N_PLAYS = 3

print("*****", N_PLAYS ,"games will be run *****")

for i in range(N_PLAYS):
    user = input("ROCK, PAPER or SCISSORS? ").lower().strip()
    element = random.randint(1,3)
    if element == 1:
        machine = "rock"
    elif element == 2:
        machine = "paper"
    else:
        machine = "scissors"

    print("Program chooses", machine)

    if user == machine:
        print("TIE")
    else:
        if user == "rock":
            if machine == "paper":
                print("***** PROGRAM WINS *****")
            else: # machine == "scissors"
                print("***** PLAYER WINS *****")
        elif user == "paper":
            if machine == "scissors":
                print("***** PROGRAM WINS *****")
            else: # machine == "rock"
                print("***** PLAYER WINS *****")
        else: # user == "scissors"
            if machine == "rock":
                print("***** PROGRAM WINS *****")
            else: # machine == "paper"
                print("***** PLAYER WINS *****")

