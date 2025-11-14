import mysql.connector
from tkinter import messagebox
from backend import notifications_logic

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "1234")
cur = mydb.cursor()
cur.execute("use library")

def get_all_due_books():
    mydb.commit()
    query = """
        SELECT 
            b.title, b.author, b.edition, b.category, 
            b.cover_img, b.description,
            i.user_id, i.issue_date, i.return_date
        FROM issue_books AS i
        JOIN books AS b ON b.book_id = i.book_id
        WHERE i.status = 'Due';
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

def get_books_by_category(category):
    mydb.commit()
    query = """
        SELECT 
            b.title, b.author, b.edition, b.category, 
            b.cover_img, b.description,
            i.user_id, i.issue_date, i.return_date
        FROM issue_books AS i
        JOIN books AS b ON b.book_id = i.book_id
        WHERE i.status = 'Due' AND b.category = %s;
    """
    cur.execute(query, (category,))
    return cur.fetchall()

def get_books_by_search_text(search_text):
    mydb.commit()
    query = """
        SELECT 
            b.title, b.author, b.edition, b.category, 
            b.cover_img, b.description,
            i.user_id, i.issue_date, i.return_date
        FROM issue_books AS i
        JOIN books AS b ON b.book_id = i.book_id
        WHERE i.status = 'Due'
          AND (b.title LIKE %s OR b.author LIKE %s OR i.user_id LIKE %s);
    """
    pattern = f"%{search_text}%"
    cur.execute(query, (pattern, pattern, pattern))
    return cur.fetchall()

def approve_due_book(user_id,title,author,edition):
    mydb.commit()
    cur.execute("select i.book_id from issue_books i,books b where b.book_id = i.book_id and i.user_id = %s and b.title = %s and b.author = %s and b.edition = %s and i.status = 'Due'",(user_id,title,author,edition))
    book_id = cur.fetchall()
    if len(book_id) == 0:
        messagebox.showerror("Error","User doesnot has this book as due")
        return False
    book_id = book_id[0][0]
    cur.execute("update issue_books set status = 'Returned',return_date = curdate() where book_id = %s and status = 'Due'",(book_id,))
    cur.execute("update books set available = 1,status = 'Available' where book_id = %s",(book_id,))
    mydb.commit()
    notifications_logic.send_notification(user_id,f"Your due book titled: {title}, author: {author}, edition: {edition} got approved")
    messagebox.showinfo("success","book approved successfully")
    