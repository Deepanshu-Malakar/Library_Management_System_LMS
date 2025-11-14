import mysql.connector
from backend import notifications_logic

from tkinter import messagebox

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "1234")
cur = mydb.cursor()
cur.execute("use library")

reissue_period = 7 #days

def check_if_book_reissued(user_id,title,author,edition):
    mydb.commit()
    cur.execute("select i.book_id from issue_books i, books b where i.book_id = b.book_id and i.user_id = %s and b.title = %s and b.author = %s and b.edition = %s and i.status = 'Reissued'",(user_id,title,author,edition))
    book_id = cur.fetchall()
    if len(book_id)>0:
        return True
    else: 
        return False

def get_bookid_of_issued_book(user_id,title,author,edition):
    mydb.commit()
    cur.execute("select i.book_id from issue_books i, books b where i.book_id = b.book_id and i.user_id = %s and b.title = %s and b.author = %s and b.edition = %s and i.status = 'Issued'",(user_id,title,author,edition))
    book_id = cur.fetchall()
    if len(book_id) == 0:
        messagebox.showerror("Book not issued")
        return 0
    return book_id[0][0]

def reissue_book(user_id,title,author,edition):
    if check_if_book_reissued(user_id,title,author,edition) == True:
        messagebox.showerror("Error","You have already reissued this book")
        return False
    book_id = get_bookid_of_issued_book(user_id,title,author,edition)
    if book_id == 0:
        return  False
    cur.execute("update issue_books set status = 'Reissued',return_date = DATE_ADD(return_date, INTERVAL %s DAY) where book_id = %s and status = 'Issued'",(reissue_period,book_id))
    cur.execute("update books set status = 'Reissued' where book_id = %s",(book_id,))
    messagebox.showinfo("Book Reissued","Book Reissued Successfully")
    notifications_logic.send_notification(user_id,f"You reissued the book titled: {title}, author: {author}, edition: {edition}")
    
    return True
    
    
    
def get_all_issued_books_of_user(user_id):
    mydb.commit()
    cur.execute("select b.title,b.author,b.edition,b.category,b.cover_img,b.description,i.issue_date,i.return_date,i.status from books b,issue_books i where b.book_id = i.book_id and i.status != 'Returned' and i.user_id = %s",(user_id,))
    books = cur.fetchall()
    mydb.commit()
    cur.execute("select b.title,b.author,b.edition,b.category,b.cover_img,b.description,i.issue_date,i.return_date,i.status from books b,issue_books i where b.book_id = i.book_id and i.status = 'Returned' and i.user_id = %s order by i.return_date desc",(user_id,))
    returned_books = cur.fetchall()
    for i in returned_books:
        books.append(i)
    return books

def get_books_by_category(category,user_id):
    mydb.commit()
    cur.execute("select b.title,b.author,b.edition,b.category,b.cover_img,b.description,i.issue_date,i.return_date,i.status from books b,issue_books i where b.book_id = i.book_id and i.status != 'Returned' and i.user_id = %s and b.category = %s",(user_id,category))
    books = cur.fetchall()
    mydb.commit()
    cur.execute("select b.title,b.author,b.edition,b.category,b.cover_img,b.description,i.issue_date,i.return_date,i.status from books b,issue_books i where b.book_id = i.book_id and i.status = 'Returned' and i.user_id = %s and b.category = %s",(user_id,category))
    returned_books = cur.fetchall()
    for i in returned_books:
        books.append(i)
    return books

def get_books_by_search(search_text,user_id):
    mydb.commit()
    cur.execute("select b.title,b.author,b.edition,b.category,b.cover_img,b.description,i.issue_date,i.return_date,i.status from books b,issue_books i where b.book_id = i.book_id and i.status != 'Returned' and i.user_id = %s and ( b.title like %s or b.author like %s)",(user_id,f"%{search_text}%",f"%{search_text}%"))
    books = cur.fetchall()
    mydb.commit()
    cur.execute("select b.title,b.author,b.edition,b.category,b.cover_img,b.description,i.issue_date,i.return_date,i.status from books b,issue_books i where b.book_id = i.book_id and i.status = 'Returned' and i.user_id = %s and ( b.title like %s or b.author like %s)",(user_id,f"%{search_text}%",f"%{search_text}%"))
    returned_books = cur.fetchall()
    for i in returned_books:
        books.append(i)
    return books

def get_expiry_date_reissued(user_id,title,author,edition):
    mydb.commit()
    cur.execute("select i.return_date from issue_books i, books b where i.book_id = b.book_id and i.user_id = %s and b.title = %s and b.author = %s and b.edition = %s and i.status = 'Reissued'",(user_id,title,author,edition))
    return_date = cur.fetchall()
    return return_date[0][0]