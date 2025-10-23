from backend import mysql_tables
cur = mysql_tables.mydb.cursor()
mydb = mysql_tables.mydb

def insert_user(user_id,email,role):
    cur.execute(""" 
        insert into users values(%s,%s,%s)""",(user_id,email,role))
    mydb.commit()

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