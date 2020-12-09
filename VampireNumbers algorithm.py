# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:48:21 2020

@author: Lekuid
"""
from itertools import combinations

pos = list(combinations([i for i in range(10, 1000)], 2))
mul = [i*y for i, y in pos if i]

n = 0
k =[]

while n in range(len(pos)):
    split_pos = [i for i in str(mul[n])]
    split_mul = [i for i in str(pos[n]) if i.isdigit()]
    split_mul.sort()
    split_pos.sort()
    if split_pos == split_mul and split_pos[-1] == split_mul[-1] != 0:
        k.append(mul[n])
        k.sort()
    n+=1

print(k)
    
