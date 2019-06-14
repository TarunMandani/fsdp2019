# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:48:06 2019

@author: lenovo
"""


import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
response.content #its convert in bites class

jsondata = response.json()

[
jsondata["coord"]["lon"],
jsondata["coord"]["lat"],
jsondata["weather"],
jsondata["wind"]["speed"],
jsondata["sys"]["sunrise"],
jsondata["sys"]["sunset"]
]