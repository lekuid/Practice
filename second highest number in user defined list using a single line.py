# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:58:58 2020

@author: Lekuid
"""

#total scores
n = int(input())

#score list, string input which is converted to int int and mapped
#sorting in ascending order and removing duplicates
a = list(sorted(set(map(int, str(input()).split(' ')))))

#len() starts at 1 while list start at 0, so -1 gives last,-2 second last
print(a[len(a) - (n-(n-2))])


print (list(sorted(set(map(int, str(input()).split(' '))))))