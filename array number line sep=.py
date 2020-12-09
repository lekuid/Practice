# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:48:46 2020

@author: Lekuid
"""

def seq(n):
    p = []
    q = 0
    while q < n:
        q += 1
        p.append(q)
    print(*p, sep='')
        

seq(int(input()))