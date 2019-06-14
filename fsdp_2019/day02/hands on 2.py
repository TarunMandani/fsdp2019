# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:53:26 2019

@author: lenovo
"""

leap_year = int(input("enter year = "))

if(leap_year % 4 == 0 and leap_year % 100 != 0):
    print ("True")
elif (leap_year % 400 == 0):
    print ("True")
elif (leap_year % 100 == 0):
    print ("false")
else :
    print ("false")