import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "1234")
cur = mydb.cursor()
cur.execute("use library")

def add_to_favourites(user_id,title,author,edition):
    cur.execute("insert into favourites values(%s,%s,%s,%s)",(user_id,title,author,edition))
    mydb.commit()

def delete_from_favourites(user_id,title,author,edition):
    cur.execute("delete from favourites where user_id = %s and title = %s and author = %s and edition = %s",(user_id,title,author,edition))
    mydb.commit()

def check_if_favourites(user_id,title,author,edition):
    cur.execute("select * from favourites where user_id = %s and title = %s and author = %s and edition = %s",(user_id,title,author,edition))
    data = cur.fetchall()
    if len(data)>0:
        return True
    else:
        return False

def get_all_favourites(user_id):
    cur.execute(f"select title,author,edition from favourites where user_id = '{user_id}'")
    books = cur.fetchall()
    fav_book_list = []
    for book in books:
        title = book[0]
        author = book[1]
        edition = book[2]
        cur.execute("select distinct title,author,edition,category,cover_img,description from books where title = %s and author = %s and edition = %s",(title,author,edition))
        fav_book = cur.fetchall()[0]
        fav_book_list.append(fav_book)
    return fav_book_list

