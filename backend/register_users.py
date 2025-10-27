from backend import mysql_tables
from backend import notifications_logic

cur = mysql_tables.mydb.cursor()
mydb = mysql_tables.mydb

def insert_user(user_id,email,role):
    cur.execute(""" 
        insert into users values(%s,%s,%s)""",(user_id,email,role))
    mydb.commit()
    notifications_logic.send_notification(user_id,"Your account is created")

def check_if_user_exist(user_id):
    cur.execute(f"select user_id from users where user_id = '{user_id}'")
    data = cur.fetchall()
    if len(data)>0:
        return True
    else:
        return False
    """
create table if not exists students(
        student_id varchar(30) primary key,
        first_name varchar(20),
        last_name varchar(20),
        phone_no varchar(10),
        DOB date,
        gender varchar(1),
        email varchar(100),
        password varchar(30),
        department varchar(50)
    )"""
    
def insert_student(student_id,first_name,last_name,phone,dob,gender,email,password,department):
    cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(student_id,first_name,last_name,phone,dob,gender,email,password,department))
    mydb.commit()
    notifications_logic.send_notification(student_id,"Your account is created")

def get_student(student_id):
    cur.execute(f"select * from students where student_id = '{student_id}'")
    student_record = cur.fetchall()
    if len(student_record)<1:
        return student_record
    student_record = student_record[0]
    data = {"student id":student_record[0],
            "first name":student_record[1],
            "last name":student_record[2],
            "phone ":student_record[3],
            "dob":student_record[4],
            "gender":student_record[5],
            "email":student_record[6],
            "password":student_record[7],
            "department":student_record[8]}
    return data

    """ 
        create table if not exists scholars(
            scholar_id varchar(30) primary key,
            first_name varchar(20),
            last_name varchar(20),
            phone_no varchar(10),
            DOB date,
            gender varchar(1),
            email varchar(100),
            password varchar(30),
            topic varchar(50))
            """

def insert_scholar(scholar_id,first_name,last_name,phone,dob,gender,email,password,topic):
    cur.execute("insert into scholars values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(scholar_id,first_name,last_name,phone,dob,gender,email,password,topic))
    mydb.commit()
    notifications_logic.send_notification(scholar_id,"Your account is created")

def get_scholar(scholar_id):
    cur.execute(f"select * from scholars where scholar_id = '{scholar_id}'")
    scholar_record = cur.fetchall()
    if len(scholar_record)<1:
        return scholar_record
    scholar_record = scholar_record[0]
    data = {"scholar id":scholar_record[0],
            "first name":scholar_record[1],
            "last name":scholar_record[2],
            "phone ":scholar_record[3],
            "dob":scholar_record[4],
            "gender":scholar_record[5],
            "email":scholar_record[6],
            "password":scholar_record[7],
            "topic":scholar_record[8]}
    return data


    """ 
        create table if not exists faculty(
            faculty_id varchar(30) primary key,
            first_name varchar(20),
            last_name varchar(20),
            phone_no varchar(10),
            DOB date,
            gender varchar(1),
            email varchar(100),
            password varchar(30),
            department varchar(50)
        )"""

def insert_faculty(faculty_id,first_name,last_name,phone,dob,gender,email,password,department):
    cur.execute("insert into faculty values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(faculty_id,first_name,last_name,phone,dob,gender,email,password,department))
    mydb.commit()
    notifications_logic.send_notification(faculty_id,"Your account is created")

def get_faculty(faculty_id):
    cur.execute(f"select * from faculty where faculty_id = '{faculty_id}'")
    faculty_record = cur.fetchall()
    if len(faculty_record)<1:
        return faculty_record
    faculty_record = faculty_record[0]
    data = {"faculty id":faculty_record[0],
            "first name":faculty_record[1],
            "last name":faculty_record[2],
            "phone ":faculty_record[3],
            "dob":faculty_record[4],
            "gender":faculty_record[5],
            "email":faculty_record[6],
            "password":faculty_record[7],
            "topic":faculty_record[8]}
    return data


