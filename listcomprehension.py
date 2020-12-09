# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:12:51 2020

@author: Lekuid
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())

print ([[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i + j + k != n])