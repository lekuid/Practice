# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 19:19:11 2020

@author: Lekuid
"""

def remove(s):
    print ([i.rstrip("!") for i in s])
    
remove(["Hi!" , "!Hi"])