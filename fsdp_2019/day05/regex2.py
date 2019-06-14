# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:07:08 2019

@author: lenovo
"""

userinput = input("enter a email = ")
import re
if (re.findall(r'^[\w\-]+@\w+\.\w{2,4}',userinput)):
        print (userinput)
else:
        print("unvalid email")