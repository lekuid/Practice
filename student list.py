# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 11:53:54 2020

@author: Lekuid
"""

n = int(input())
student_list = []
records = []

while n > 0:
    n -= 1
    student_list.append(str(input()))
    student_list.append(float(input()))
    records.append(student_list)
    student_list = []

for [name, marks] in records:
    sorted = records(key = lambda marks:marks[1])
