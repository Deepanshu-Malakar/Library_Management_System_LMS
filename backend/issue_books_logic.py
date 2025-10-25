import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "1234")
cur = mydb.cursor()
cur.execute("use library")

"""
                create table if not exists issue_books(
                    book_id int,
                    user_id varchar(30),
                    issue_date date,
                    return_date date,
                    status varchar(30)  [Issued,Returned,Due]
                )"""


issue_period = 7 # books can be issued for 7 days before exipry
max_issues = 4 # maximum books user can issue

# Issue Book Helper Functions........................

def get_available_book_id(title,author,edition):
    mydb.commit()
    cur.execute("select book_id from books where available = '1' and title = %s and author = %s and edition = %s ",(title,author,edition))
    book_ids = cur.fetchall()
    if len(book_ids)>0:
        return book_ids[0][0]
    else:
        messagebox.showerror("Error","Sorry, the book is not available for issue")
        return 0
    
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

def user_does_not_exist(user_id):
    mydb.commit()
    cur.execute(f"select role from users where user_id = '{user_id}' ")
    role = cur.fetchall()
    if len(role) == 0:
        messagebox.showerror("Error","User does not exist")
        return True
    role = role[0][0]

    if role.lower() == "student":
        cur.execute(f"select * from students where student_id = '{user_id}'")
        user = cur.fetchall()
        if len(user) == 0:
            messagebox.showerror("Error","User does not exist")
            return True
        
    elif role.lower() == "faculty":
        cur.execute(f"select * from faculty where faculty_id = '{user_id}'")
        user = cur.fetchall()
        if len(user) == 0:
            messagebox.showerror("Error","User does not exist")
            return True
        
    elif role.lower() == "scholar":
        cur.execute(f"select * from faculty where faculty_id = '{user_id}'")
        user = cur.fetchall()
        if len(user) == 0:
            messagebox.showerror("Error","User does not exist")
            return True
    
    elif role.lower() == "librarian":
        messagebox.showerror("Error","Librarian cannot Borrow Books")
        return True
    return False
    
    
    
def issue_book(user_id,title,author,edition):
    if user_does_not_exist(user_id) or user_already_has_book(user_id,title,author,edition) or user_limit_exceeded(user_id):
        return False
    book_id = get_available_book_id(title,author,edition)
    if book_id == 0:
        return False
    insert_issue_book(user_id,book_id)
    return True


# Return Books Helper Functions...........


# search queries..................
def get_all_issued_books():
    mydb.commit()
    query = """
        SELECT 
            b.title, b.author, b.edition, b.category, 
            b.cover_img, b.description,
            i.user_id, i.issue_date, i.return_date
        FROM issue_books AS i
        JOIN books AS b ON b.book_id = i.book_id
        WHERE i.status != 'Returned';
    """
    cur.execute(query)
    data = cur.fetchall()
    return data

def get_issued_books_by_category(category):
    mydb.commit()
    query = """
        SELECT 
            b.title, b.author, b.edition, b.category, 
            b.cover_img, b.description,
            i.user_id, i.issue_date, i.return_date
        FROM issue_books AS i
        JOIN books AS b ON b.book_id = i.book_id
        WHERE i.status != 'Returned' AND b.category = %s;
    """
    cur.execute(query, (category,))
    return cur.fetchall()

def search_issued_books(search_text):
    mydb.commit()
    query = """
        SELECT 
            b.title, b.author, b.edition, b.category, 
            b.cover_img, b.description,
            i.user_id, i.issue_date, i.return_date
        FROM issue_books AS i
        JOIN books AS b ON b.book_id = i.book_id
        WHERE i.status != 'Returned'
          AND (b.title LIKE %s OR b.author LIKE %s OR i.user_id LIKE %s);
    """
    pattern = f"%{search_text}%"
    cur.execute(query, (pattern, pattern, pattern))
    return cur.fetchall()




def remove_from_issued_books(user_id,book_id):
    cur.execute("update issue_books set status = 'Returned' where user_id = %s and book_id = %s and status != 'Returned'",(user_id,book_id))
    cur.execute("update books set available = 1, status = 'Available' where book_id = %s",(book_id,))
    mydb.commit()

def pending_fine(user_id):
    f = 0
    return f


def return_book(user_id,title,author,edition):
    mydb.commit()
    if pending_fine(user_id):
        messagebox.showerror("Error",f"You have a fine pending of Rs{pending_fine(user_id)}.00 Please pay the fine to continue")
        return False
    cur.execute("select i.book_id from issue_books i, books b where b.book_id = i.book_id and i.user_id = %s and b.title = %s and b.author = %s and b.edition = %s and i.status != 'Returned'",(user_id,title,author,edition))
    book_id = cur.fetchall()
    if len(book_id)==0:
        messagebox.showerror("Error","User has not issued this book. Please refresh the page")
        return False
    book_id = book_id[0][0]
    remove_from_issued_books(user_id,book_id)
    messagebox.showinfo("Success","Book returned successfully")
    return True
