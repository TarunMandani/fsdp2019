# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:48:32 2019

@author: lenovo
"""

userinput = input("Enter String: ")

character = {}

for word in userinput:

    character[word] = character.get(word,0) + 1
    
print (character)