# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:40:16 2019

@author: lenovo
"""


num = 100
for min in range(num + 1):
    if (min % 3 == 0 and min % 5 == 0):
        print('fizzbuzz')
        continue
    elif min % 3 == 0:
        print ('fizz')
        continue
    elif min % 5 == 0:
        print ('buzz')
        continue
    print(min)