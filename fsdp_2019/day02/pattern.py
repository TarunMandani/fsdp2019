# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:03:38 2019

@author: lenovo
"""
no = int(input("enter pattern max * no  = "))
for i in range(0,no,1):
    print('*'*i)
for i in range(no,0,-1):
    print('*'*i)