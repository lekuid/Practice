# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:17:12 2020

@author: Lekuid
"""

num = int(input())

if num % 2 == 0 and num in range(2, 5):
    print ("Not Weird")
elif num % 2 == 0 and num in range(6, 20):
    print ("Weird")
elif num % 2 == 0 and num > 20:
    print ("Not Weird")
else:
    print("Weird")
