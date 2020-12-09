# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:09:42 2020

@author: Lekuid
"""
import pylab as p

matrix = p.np.array(range(1,31)).reshape(6,5)
print(matrix)
#print(matrix[2:4,0:2])
#print(matrix[[0,1,2,3],[1,2,3,4]])
print(matrix[[0, 4, 5],3:])
