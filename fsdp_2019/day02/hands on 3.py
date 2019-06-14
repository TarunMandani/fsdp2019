# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:27:30 2019

@author: lenovo
"""
month = input("month = ")
year = int(input('year = '))
def leapyear (year):
    return (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0)
leapyear1 = leapyear(year)

def month_and_year(month,leapyear1):
    if month in['january','march','may','july','august','october','december']:
        print("31 days")
    elif month in['april','june','september','november']:
        print("30 days")
    elif month == 'Feburary' and leapyear1 == True:
        print('29 days')
    elif month == 'Feburary' and leapyear1 == False:
        print("28 days")
month_and_year(month,leapyear1)