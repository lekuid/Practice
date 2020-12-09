# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:10:39 2020

@author: Lekuid
"""

def encode_resistor_colors(ohms_string):
    resis = {0: 'black', 1: 'brown', 2: 'red', 3: 'orange', 4: 'yellow', 5: 'green', 6: 'blue', 7: 'violet', 8: 'gray', 9: 'white'}
    ohms = float(''.join([x for x in ohms_string.split(' ')[0] if not x.isalpha()]))
    if 'k' in ohms_string:
        ohms = ohms*1000
    if 'M' in ohms_string:
        ohms = ohms*1000000
    num_bands = []
    num_bands.append(resis.get(int(str(ohms)[0])))
    num_bands.append(resis.get(int(str(ohms)[1])))
    n=0
    while n < list(resis.keys())[-1] and len(str(int(ohms/10**list(resis.keys())[n]))) > 2:
        n+=1
    num_bands.append(resis.get(n))
    num_bands.append('gold')
    return ' '.join(num_bands)

print(encode_resistor_colors(input('Enter Ohms:')))