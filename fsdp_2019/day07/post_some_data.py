# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:38:15 2019

@author: lenovo
"""


"""
Research the below wesbite and post some data on it
https://requestbin.com
"""


import json
import requests

Host = "https://en9ft5z2nc0qb.x.pipedream.net"

data = {"firstname":"Tarun Mandani","year":"3rd year"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )