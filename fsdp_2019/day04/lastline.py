# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:32:56 2019

@author: lenovo
"""

filename = input('enter the file name= ')
try:
    file = open (filename , mode="rt")
    
except:
    print ("file cant open",file)
    exit()
    
lines = file.readlines()
lines = lines[-1]
print (lines)
    