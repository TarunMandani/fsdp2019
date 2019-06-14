# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:10:46 2019

@author: lenovo
"""

numbers = int(input('enter the no = '))
s=str(numbers)
print(int(s[::-1]))

revers = int(s[::-1])

if (numbers / revers == 1):
    print ('True')
else:
    print('false')
 