# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:20:14 2020

@author: Lekuid
"""

import random

num = random.randint(1, 100)
print ("Let's Start guessing")
n = 0

while n != num:
    n = int(input())
    
    if n > num:
        print ("Try going lower")
    elif n < num:
        print ("Try going higher")
    elif n == num:
        break
    
print ("You guessed it, The number was", num)

        