# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:08:28 2019

@author: lenovo
"""







numbers = input("enter numbers = ").split(',')


pall = [int(n) for n in numbers]
new = list(map(lambda x:True if x==x[::-1] else False,numbers))

print(new)
