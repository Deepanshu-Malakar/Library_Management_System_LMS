import mysql.connector
from tkinter import messagebox
mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "1234")
cur = mydb.cursor()
cur.execute("use library")
issue_period = 7
max_issues = 4

def get_all_reserved_books():
    mydb.commit()
    cur.execute("select b.title,b.author,b.edition,b.category,b.cover_img,b.description,r.user_id from books b, reserve_books r where b.book_id = r.book_id")
    books = cur.fetchall()
    return books

def get_books_by_category(category):
    mydb.commit()
    cur.execute(f"select b.title,b.author,b.edition,b.category,b.cover_img,b.description,r.user_id from books b, reserve_books r where b.book_id = r.book_id and b.category = '{category}'")
    books = cur.fetchall()
    return books

def get_books_by_title_author_reserver(search_text):
    mydb.commit()
    cur.execute(f"select b.title,b.author,b.edition,b.category,b.cover_img,b.description,r.user_id from books b, reserve_books r where b.book_id = r.book_id and ( b.title like '%{search_text}%' or b.author like '%{search_text}%' or r.user_id like '%{search_text}%')")
    books = cur.fetchall()
    return books

#......................................

def issue_book(user_id,title,author,edition):
    mydb.commit()
    cur.execute("select r.book_id from reserve_books r, books b where b.book_id = r.book_id and r.user_id = %s and b.title = %s and b.author = %s and b.edition = %s",(user_id,title,author,edition))
    book_id = cur.fetchall()
    if len(book_id) == 0:
        messagebox.showerror("Error","User has not reserved this book, please refresh the page")
        return False
    book_id = book_id[0][0]
    if user_already_has_book(user_id,title,author,edition) or user_limit_exceeded(user_id):
        return False
    #delete from reserve books
    #add in issue books
    #update status in books
    cur.execute(f"delete from reserve_books where book_id = {book_id}")
    insert_issue_book(user_id,book_id)
    mydb.commit()
    return True


def insert_issue_book(user_id,book_id):
    mydb.commit()
    cur.execute("insert into issue_books values(%s,%s,curdate(),DATE_ADD(CURDATE(), INTERVAL %s DAY),'Issued')",(book_id,user_id,issue_period))
    cur.execute(f"update books set available = 0,status = 'Issued' where book_id = {book_id}")
    mydb.commit()
    messagebox.showinfo("Success","Book Issued Successfully")

def user_already_has_book(user_id,title,author,edition):
    mydb.commit()
    cur.execute("select i.book_id from issue_books i,books b where i.user_id = %s and b.book_id = i.book_id and b.title = %s and b.author = %s and b.edition = %s and i.status != 'Returned';",(user_id,title,author,edition))
    book_id = cur.fetchall()
    if len(book_id)>0:
        messagebox.showerror("Error","User Already has the book")
        return True
    else:
        return False
    
def user_limit_exceeded(user_id):
    mydb.commit()
    cur.execute(f"select * from issue_books where user_id = '{user_id}' and status != 'Returned'")
    books_reserved = len(cur.fetchall())
    if books_reserved >= max_issues:
        messagebox.showerror("Error","Users Issue Limit Exceeded, return the previously issued books to continue")
        return True
    else:
        return False


    
    