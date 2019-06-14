# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:00:05 2019

@author: lenovo
"""
  

    
    
from functools import reduce

people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]

my_filter_list = list(map(lambda x:x['height'], filter( lambda x: 'height' in x,people )))
fianal=reduce(lambda x,y:x+y , my_filter_list)/len(my_filter_list)
print(fianal)
