# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:47:58 2019

@author: lenovo
"""

from collections import OrderedDict

order = OrderedDict()

while True:
    userinput = ('enter item and price = ')
    
    if not userinput:
        break
    
    temp = userinput.split()
    price = temp[-1]

    item = " ".join(temp[:-1])
    

    order[item] = order.get(item,0) + int(price)

for k,v in order.items():
    print (k,v)