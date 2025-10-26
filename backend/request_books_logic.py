import mysql.connector
from backend import mysql_tables
from tkinter import messagebox
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

import mysql.connector
from backend import mysql_tables
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="library"
)
cur = mydb.cursor()

def insert_request(user_id, title, author, edition, category, cover_img, description):
    cur.execute(
        "INSERT INTO request_book VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (user_id, title, author, edition, category, cover_img, description)
    )
    mydb.commit()

def check_if_book_exists(title, author, edition):
    mysql_tables.cur.execute(
        "SELECT * FROM books WHERE title=%s AND author=%s AND edition=%s",
        (title, author, edition)
    )
    result = mysql_tables.cur.fetchall()
    return len(result) > 0

def update_or_retain_description(title, author, edition, new_description):
    if check_if_book_exists(title, author, edition):
        if new_description == "No Description Available":
            mysql_tables.cur.execute(
                "SELECT description FROM books WHERE title=%s AND author=%s AND edition=%s",
                (title, author, edition)
            )
            result = mysql_tables.cur.fetchall()
            description = result[0][0]
            return description
        else:
            mysql_tables.cur.execute(
                "UPDATE books SET description=%s WHERE title=%s AND author=%s AND edition=%s",
                (new_description, title, author, edition)
            )
            mysql_tables.mydb.commit()
            return new_description
    else:
        return new_description

def add_book(title, author, edition, copies):
    cur.execute(
        "SELECT * FROM request_book WHERE title=%s AND author=%s AND edition=%s",
        (title, author, edition)
    )
    data = cur.fetchall()

    if len(data) == 0:
        messagebox.showerror("Error", "This book is not requested. Please refresh the page.")
        return

    category = data[0][4]
    cover_img = data[0][5]
    description = data[0][6]

    # ✅ Pass description correctly
    description = update_or_retain_description(title, author, edition, description)

    for i in range(copies):
        book_id = mysql_tables.generate_book_id()
        mysql_tables.insert_book(
            book_id, title, author, edition, category, "Available", "1", cover_img, description
        )

    # ✅ Fix delete statement
    cur.execute(
        "DELETE FROM request_book WHERE title=%s AND author=%s AND edition=%s",
        (title, author, edition)
    )
    mydb.commit()

    messagebox.showinfo("Success", "Books added successfully.")

def get_all_requested_books():
    cur.execute("""
        SELECT 
            title,
            author,
            edition,
            category,
            cover_img,
            description,
            COUNT(*) AS total_requests
        FROM request_book
        GROUP BY title, author, edition, category, cover_img, description
    """)
    return cur.fetchall()

def get_book_by_category(category):
    cur.execute("""
        SELECT 
            title,
            author,
            edition,
            category,
            cover_img,
            description,
            COUNT(*) AS total_requests
        FROM request_book
        WHERE category = %s
        GROUP BY title, author, edition, category, cover_img, description
    """, (category,))
    return cur.fetchall()


def get_books_by_title_or_author(search_text):
    cur.execute("""
        SELECT 
            title,
            author,
            edition,
            category,
            cover_img,
            description,
            COUNT(*) AS total_requests
        FROM request_book
        WHERE title LIKE %s OR author LIKE %s
        GROUP BY title, author, edition, category, cover_img, description
    """, (f"%{search_text}%", f"%{search_text}%"))
    return cur.fetchall()

