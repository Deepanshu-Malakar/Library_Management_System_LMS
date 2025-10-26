import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "1234")
cur = mydb.cursor()
cur.execute("use library")


"""create table if not exists request_book(
                    user_id varchar(30),
                    title varchar(30),
                    author varchar(30),
                    edition int,
                    category varchar(30),
                    cover_img varchar(512),
                    description varchar(1024) 
                )"""

def insert_request(user_id,title,author,edition,category,cover_img,description):
    cur.execute("insert into request_book values(%s,%s,%s,%s,%s,%s,%s)",(user_id,title,author,edition,category,cover_img,description))
    mydb.commit()

