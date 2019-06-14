# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:39:04 2019

@author: lenovo
"""


import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
result = list(map(lambda x: random.choice(code_names),names))
print(result)