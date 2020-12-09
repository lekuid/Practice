# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 19:22:19 2020

@author: Lekuid
"""

def leap(year):
    return year%4 == 0 and (not year%100 == 0 or year%400 == 0)

print (leap(int(input())))