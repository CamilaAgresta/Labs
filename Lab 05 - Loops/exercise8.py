"""
Bachelor in Data Science and Engineering 
Subject: Programming
Created by Camila Alba Agresta Kohen  
Created on 12/10/25 at 21:54
Universidad Carlos III de Madrid
Student

-------
Lab 5
Exercise: 8

Create a program that plays "Twenty 0ne”, a simple dice version of Blackjack. For this game
two dices will be rolled. The points will be calculated as the sum of the rolls of the two dices.
Although the game can be played with several players, to simplify it we will play only with two.
The rules are as follows:
    • Each player plays only once per game.
    • The player can roll the dice as many times as desired and can stop at any time if the
        score is no higher than 21. Numbers obtained in each roll are added to the previous in
        order to establish the score.
    • If a player reaches a score greater than 21 she loses immediately, so the other player is
        automatically the winner.
    • If no player has exceeded 21, the participant whose total is nearest to 21 points, wins.
        If the two players reach the same score, then it will be declared a tie.
    • The number of games to be played will be a value defined as a constant in the program.
        Taking into account the specifications established and the example provided:
    ▪ Program the move corresponding to player 1 until she decides to stop, or the score
        is higher than 21, in this last case player 1 has lost.
    ▪ Program also the move corresponding to player 2 and display the winner (or the tie)
    ▪ Modify the exercise to run multiple games as indicated in the statement.
"""

import random

N_GAMES = 2
repeat = True
repeat2 = True
game = 0

for i in range(N_GAMES):
    points1 = 0  # points of the player 1
    points2 = 0  # points of the player 2
    game += 1

    while repeat and points1 <= 21:
        print("GAME", game, " -  PLAYER 1")
        dice = random.randint(2,12)
        points1 += dice
        print("The points accumulated are", points1)
        ans = input("Would you like to roll the dice again? (yes/no) ").lower().strip()
        if ans == "no":
            repeat = False

    while repeat2 and points2 <= 21:
        print("GAME", game, " -  PLAYER 2")
        dice = random.randint(2,12)
        points2 += dice
        print("The points accumulated are", points2)
        ans = input("Would you like to roll the dice again? (yes/no) ").lower().strip()
        if ans == "no":
            repeat = False

    if points1 > 21:
        print("*********** PLAYER 2 WINS ***********")
    elif points2 > 21:
        print("*********** PLAYER 1 WINS ***********")
    else:
        if points1 > points2:
            print("*********** PLAYER 1 WINS ***********")
        elif points1 < points2:
            print("*********** PLAYER 2 WINS ***********")
        else:
            print("*********** TIE ***********")

