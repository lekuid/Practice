# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:13:58 2020

@author: Lekuid
"""

def cakes(recipe, available):
    tot = []
    n = min(len(recipe), len(available))
    items = [x for x in recipe.keys() if x in available.keys()]
    while len(recipe) <= len(available):
        while n > 0:
            n-=1
            tot.append(available.get(items[n])/recipe.get(items[n]))
        return int(str(min(tot)).rsplit('.')[0])
    else:
        return 0