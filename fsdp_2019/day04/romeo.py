# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:56:55 2019

@author: lenovo
"""

with open ("romeo.txt","rt") as file:
    split_ = file.readlines()
    print (split_)
    
    
    character = {}

    for line in split_:
        words = line.split()
        for word in words:
            if word not in character:
                character[word] = 1
            else:
                character[word] += 1
    
print (character)
        
    
    