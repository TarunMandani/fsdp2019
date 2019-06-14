# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:46:43 2019

@author: lenovo
"""

A1 = int(input("marks of assignment 1 ="))
A2 = int(input("marks of assignment 2 ="))
A3 = int(input("marks of assignment 3 ="))
E1 = int(input("marks of exam 1 ="))
E2 = int(input("marks of exam 2 ="))
weighted_score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
print(weighted_score)