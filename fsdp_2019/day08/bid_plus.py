# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:41:49 2019

@author: lenovo
"""

"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""


import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as BS

url = "https://bidplus.gem.gov.in/bidlists"

driver = webdriver.Chrome("C:\\Users\\lenovo\\Desktop\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get(url)

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for i in range (1,11):
    bid_no = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text
    A.append(bid_no)
    
    items = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text
    B.append(items)
    
    Q_R = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text
    C.append(Q_R)
    
    dep_name_add = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text
    D.append(dep_name_add)
    
    start = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text
    E.append(start)
    
    end = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text
    F.append(end)
    
html_page = driver.page_source

soup = BS(html_page)


from collections import OrderedDict

col_name = ["bid_no","iteams","quantity required","department name and address","start","end"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))


df = pd.DataFrame(col_data) 
df.to_csv("bid_no.csv")
