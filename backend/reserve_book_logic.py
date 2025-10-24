import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "1234")
cur = mydb.cursor()
cur.execute("use library")

def check_if_book_reserved(user_id,title,author,edition):
    cur.execute("""select * from books where 
                    book_id in (select book_id from reserve_books where user_id = %s) and
                    title = %s and 
                    author = %s and
                    edition = %s""",(user_id,title,author,edition))
    exist = cur.fetchall()
    if len(exist)>0:
        return True
    else:
        return False

def get_available_book_id(title,author,edition):
    cur.execute("select book_id from books where available = '1' and title = %s and author = %s and edition = %s ",(title,author,edition))
    book_ids = cur.fetchall()
    if len(book_ids)>0:
        return book_ids[0][0]
    else:
        return 0
    
def reserve_book(user_id,title,author,edition):
    book_id = get_available_book_id(title,author,edition)
    if book_id == 0:
        return  0
    cur.execute("insert into reserve_books values(%s,%s,curdate())",(user_id,book_id))
    cur.execute(f"update books set available = 0, status = 'Reserved' where book_id = {book_id}")
    mydb.commit()
    return 1

def unreserve_book(user_id,title,author,edition):
    cur.execute("""select book_id from books where
                book_id in (select book_id from reserve_books where user_id = %s) and 
                title = %s and
                author = %s and 
                edition = %s""",(user_id,title,author,edition))
    book_id = cur.fetchall()
    if len(book_id) == 0:
        return 0
    else:
        book_id = book_id[0][0]
        cur.execute("delete from reserve_books where user_id = %s and book_id = %s ",(user_id,book_id))
        cur.execute(f"update books set available = 1 ,status = 'Available' where book_id = {book_id}")
        mydb.commit()
        return 1
    
def get_all_reserved_books(user_id):
    cur.execute(f"select book_id from reserve_books where user_id = '{user_id}'")
    books = cur.fetchall()
    res_book_list = []
    for book in books:
        book_id = book[0]
        cur.execute("select distinct title,author,edition,category,cover_img,description from books where book_id = %s",(book_id,))
        res_book = cur.fetchall()[0]
        res_book_list.append(res_book)
    return res_book_list
