# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 07:25:08 2019

@author: lenovo
"""


state_name = ['Alabama', 'California', 'Oklahoma', 'Florida']

vowel = list("aeiouAEIOU")

final = []

for state in state_name:
    templist = []
    for char in state:
        if char not in vowel:
            templist.append(char)
    final.append("".join(templist))
    
print (final)
    



