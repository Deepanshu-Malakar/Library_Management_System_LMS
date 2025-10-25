import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "1234")
cur = mydb.cursor()
cur.execute("create database if not exists library")
cur.execute("use library")



def create_tables():

    # create librarian table
    cur.execute("create table if not exists librarian(" \
    "lib_id varchar(30) primary key," \
    "first_name varchar(20)," \
    "last_name varchar(20)," \
    "phone_no varchar(10)," \
    "DOB date," \
    "gender varchar(1)," \
    "email varchar(100)," \
    "password varchar(30)" \
    ")")

    # create books table
    cur.execute("create table if not exists books(" \
    "book_id int primary key," \
    "title varchar(30)," \
    "author varchar(30)," \
    "edition int," \
    "category varchar(30)," \
    "status varchar(20)," \
    "available int," \
    "cover_img varchar(512)," \
    "description varchar(1024)" \
    ")")

    # Students Table...............
    cur.execute(""" 
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
    )""")

    # Faculty Table..................
    cur.execute(""" 
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
    )""")

    #Scholars Table.................
    cur.execute(""" 
    create table if not exists scholars(
        scholar_id varchar(30) primary key,
        first_name varchar(20),
        last_name varchar(20),
        phone_no varchar(10),
        DOB date,
        gender varchar(1),
        email varchar(100),
        password varchar(30),
        topic varchar(50))""")
    
    #Users Table........................
    cur.execute(""" 
        create table if not exists users(
            user_id varchar(30),
            email varchar(100),
            role varchar(30));""")
    
    #Favourites table......................
    cur.execute("""create table if not exists favourites(
                    user_id varchar(30),
                    title varchar(30),
                    author varchar(30),
                    edition int
                )""")
    
    # Reserve Books Table...................
    cur.execute("""
                create table if not exists reserve_books(
                    user_id varchar(30),
                    book_id int,
                    transaction_date date
                )
            """)
    
    # Issue Books Table..........................
    cur.execute("""
                create table if not exists issue_books(
                    book_id int,
                    user_id varchar(30),
                    issue_date date,
                    return_date date,
                    status varchar(30)
                )""")
    
    cur.execute("""create table if not exists doubts(
                    doubt_id int primary key,
                    user_id varchar(30),
                    doubt text
                )""")

    mydb.commit()


# Librarian..............................................................................
def insert_librarian(lib_id,first_name,last_name,ph_no,dob,gender,email,password):
    cur.execute("insert into librarian values(%s,%s,%s,%s,%s,%s,%s,%s)",(lib_id,first_name,last_name,ph_no,dob,gender,email,password))
    mydb.commit()

def display_librarian():
    cur.execute("select * from librarian")
    return cur.fetchall()

def find_librarian(lib_id):
    cur.execute(f"select * from librarian where lib_id = '{lib_id}'")
    try:
        data = cur.fetchall()[0]
        record = {"lib_id":data[0],
                "first_name":data[1],
                "last_name":data[2],
                "ph_no":data[3],
                "DOB":data[4],
                "gender":data[5],
                "email":data[6],
                "password":data[7]
                }
        return record
    except:
        return 0
#/ Librarian..............................................................................


# Books..................................................................................

def insert_book(book_id,title,author,edition,category,status,available,cover_img,description):
    cur.execute("insert into books values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(book_id,title,author,edition,category,status,available,cover_img,description))
    mydb.commit()

def display_books():
    cur.execute("select * from books")
    return cur.fetchall()

def find_book(book_id):
    cur.execute(f"select * from books where book_id = '{book_id}'")
    try:
        data = cur.fetchall()[0]
        record = {"book_id":data[0],
                "title":data[1],
                "author":data[2],
                "edition":data[3],
                "category":data[4],
                "status":data[5],
                "available":data[6],
                "status":data[7],
                "description":data[8]
                }
        return record
    except:
        return 0 
def generate_book_id():
    cur.execute("select max(book_id) from books")
    data = cur.fetchall()[0][0]
    if data==None:
        return 1001
    else:
        return data+1

def get_book_by_title():
    cur.execute(f"""SELECT distinct title,author,edition,category,cover_img,description from books;
                """)
    return cur.fetchall()

def get_copies_of_book(title,author,edition):
    mydb.commit()
    cur.execute("select count(book_id) from books where title=%s and author = %s and edition = %s and available = 1 and status = 'Available';",(title,author,edition))
    return cur.fetchall()[0][0]
#/ Books..................................................................................




