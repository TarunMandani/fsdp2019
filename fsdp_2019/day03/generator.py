# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:50:38 2019

@author: lenovo
"""

list1 = []
while True:
    user_input = input("Enter values >")
    
    #append this entry to other data structure
    list1.append(user_input)
    
    if not user_input:
        break
list1.pop()
print('List :',list1)

tuple1 = tuple(list1)
print('tuple :',tuple1)
