# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:17:09 2019

@author: lenovo
"""
"""

Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.


"""



import pymongo





client = pymongo.MongoClient("mongodb+srv://Tarun:myfather%4018@cluster0-kt5ax.mongodb.net/test?retryWrites=true&w=majority")
db = client.db_university




def add_student(sno,name,age,roll_no,branch):

    db.students.insert_one(
            {
          "S_no " : sno,
          "STUDENT_NAME" : name,
          "STUDENT_AGE" : age,
          "STUDENT_ROLL_NO" : roll_no,
          "STUDENT_BRANCH" : branch
            })
    return "students added successfully"


def fetch_all_student():
    user = db.students.find()
    for i in user:
        print (i)




add_student('01','Tarun Mandani',20, 20, 'ec')
add_student('02','Deepak Swami' ,22,6,'ec')
add_student('03','Tarun Jangir' , 20 ,19, 'ec')
add_student('04','Khushank', 20 , 11 , 'ec')
add_student('05','Garvit', 20 , 8 , 'ec')
add_student('06','Arun Mandani',20, 18, 'ec')
add_student('07','Deepika Swami' , 18 ,1 ,'ec')
add_student('08','varun Jangir' , 20 ,15, 'ec')
add_student('09','Khushi', 20 , 12 , 'ec')
add_student('10','radhika', 20 , 2 , 'ec')

fetch_all_student()
