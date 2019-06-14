# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:28:15 2019

@author: lenovo
"""
userinput = input("enter a no = ")
import re
if (re.findall(r'^[+-.]\d*\.\d+',userinput)):
        print ("True")
else:
        print("false")
    
    
