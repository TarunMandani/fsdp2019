# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:04:54 2019

@author: lenovo
"""
i=0
with open("totalstudents.txt","wt") as file:
    while True:
        if i<25:
            userinput = input('enter name of student = ')
            if not userinput:
                 break
            file.write(userinput+'\n')
            i+=1
        else:
            break
        
