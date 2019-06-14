# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:36:57 2019

@author: lenovo
"""

"""

Code Challenge 1
Write a python code to insert records to a sqlite
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""
import sqlite3
from pandas import DataFrame


conn = sqlite3.connect ( 'db_university.db' )

c = conn.cursor()

c.execute ("""CREATE TABLE students(
          S_no TEXT,
          STUDENT_NAME TEXT,
          STUDENT_AGE  INTIGER,
          STUDENT_ROLL_NO INTIGER,
          STUDENT_BRANCH TEXT
          )""")

c.execute("INSERT INTO students VALUES (01,'Tarun Mandani',20, 20, 'ec')")
c.execute("INSERT INTO students VALUES (02,'Deepak Swami' , 22 ,06 ,'ec')")
c.execute("INSERT INTO students VALUES (03,'Tarun Jangir' , 20 ,19, 'ec')")
c.execute("INSERT INTO students VALUES (04,'Khushank', 20 , 11 , 'ec')")
c.execute("INSERT INTO students VALUES (05,'Garvit', 20 , 08 , 'ec')")
c.execute("INSERT INTO students VALUES (06,'Arun Mandani',20, 18, 'ec')")
c.execute("INSERT INTO students VALUES (07,'Deepika Swami' , 18 ,01 ,'ec')")
c.execute("INSERT INTO students VALUES (08,'varun Jangir' , 20 ,15, 'ec')")
c.execute("INSERT INTO students VALUES (09,'Khushi', 20 , 12 , 'ec')")
c.execute("INSERT INTO students VALUES (10,'radhika', 20 , 02 , 'ec')")


c.execute("SELECT * FROM students")

print ( c.fetchall() )

c.execute("SELECT * FROM students")



df = DataFrame(c.fetchall())  
df.columns = ["S_no","STUDENT_NAME","STUDENT_AGE","STUDENT_ROLL_NO","STUDENT_BRANCH"]


conn.commit()

conn.close()

