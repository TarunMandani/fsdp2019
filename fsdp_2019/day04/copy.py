# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:52:22 2019

@author: lenovo
"""

with open ("words.txt",mode="rt") as file1:
    with open ("words1.txt",mode="wt") as file2:
        for line in file1:
            file2.write(line)
        
            