# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:29:24 2020

@author: Lekuid
"""

import random

num = random.randint(1, 100)
print ("Let's Start guessing")
n = 0
tries = 7

while n != num:
    n = int(input())
    
    if n > num and tries != 0:
        tries -= 1
        print ("Try going lower, tries left", tries)
    elif n < num and tries != 0:
        tries -= 1
        print ("Try going higher, tries left", tries)
    elif n == num:
        print ("You guessed it, The number was", num)
        break
    elif tries == 0:
        print ("You ran out of tries, The number was", num)
        break