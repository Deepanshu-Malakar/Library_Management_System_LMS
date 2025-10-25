import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "1234")
cur = mydb.cursor()
cur.execute("use library")

def get_doubt_id():
    mydb.commit()
    cur.execute("select * from doubts")
    doubt_id = len(cur.fetchall())+1
    return doubt_id

def insert_doubt(user_id,doubt):
    doubt_id = get_doubt_id()
    cur.execute("insert into doubts values(%s,%s,%s)",(doubt_id,user_id,doubt))
    mydb.commit()
