# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:36:46 2020

@author: Lekuid
"""

import random

points = 0
possible_move = ["rock", "paper", "scissor"]

while points <= 3:
    
    move = random.choice(possible_move)
    your_move = str(input("Choose:"))

    if move == your_move:
        print ("Tie!")
    elif move != your_move and move == "rock" and your_move == "scissor":
        print ("Lose!")
        points -= 1
    elif move != your_move and move == "paper" and your_move == "scissor":
        print ("Win!")
        points += 1
    elif move != your_move and move == "rock" and your_move == "paper":
        print ("Win!")
        points += 1
    elif move != your_move and move == "paper" and your_move == "rock":
        print ("Lose!")
        points -= 1
    elif move != your_move and move == "scissor" and your_move == "paper":
        print ("Lose!")
        points -= 1
    elif move != your_move and move == "scissor" and your_move == "rock":
        print ("Win!")
        points += 1
    elif your_move == "exit":
        break
    else:
        print ("invalid input! Try again.")
        
    print ("PC Chose=", move, ",You chose=", your_move, "\n Current Points=", points)
    