# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:27:55 2020

@author: Lekuid
"""

#total number of plants

total_plants = int(input())

#empty list and comparison var

q = 0
r = []

#taking values into list

while q < total_plants:
    q += 1
    r.append(int(input()))
    
#total plant and total sum of heights

total_distinctheight = len(set(r))
total_distinctheight_sum = sum(set(r))

#output

print (total_distinctheight_sum/total_distinctheight)

#len() is used to get the length of a list
#set() is used to remove duplicate entries