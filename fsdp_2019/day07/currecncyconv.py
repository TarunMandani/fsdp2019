# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:15:32 2019

@author: lenovo
"""


"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
import json
import requests

url1 = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=58825d4ac705d23d979e"


def get_method():
    response = requests.get("https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=58825d4ac705d23d979e")
    return response

print (get_method().text)