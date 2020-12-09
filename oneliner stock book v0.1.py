# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:41:02 2020

@author: Lekuid
"""

def fillable(stock, merch, n):
    return merch in stock.keys() and n <= list(stock.values())[list(stock.keys()).index(merch)]

stock = {'football': 4,'boardgame': 10,'leggos': 1,'doll': 5,}


print(fillable(stock, str(input('Item:')), int(input('Quantity:'))))