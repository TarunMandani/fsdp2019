# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:17:13 2019

@author: lenovo
"""

file = open("passwd",mode="r")
count = file.readlines()
print(count)

dict1 = {}

for line in count:
    lst=line.split(':')
    dict1[lst[0]] = lst[2]
print(dict1)