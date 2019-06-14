# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:14:41 2019

@author: lenovo
"""


tuple1 = list(input('enter days : '))
day = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
for i in day:
    if i in tuple1:
        continue
    elif i not in tuple1:
         tuple1.append(i)
        
print(tuple1)
    


str1 =('Monday', 'Wednesday', 'Thursday', 'Saturday')
print((str1[0],'Tuesday',str1[1],str1[2],'friday',str1[3],'sunday'))

