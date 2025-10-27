from tkinter import *
from customtkinter import *
from PIL import Image
from backend import mysql_tables
from backend import DrawBooks
from components import user_info_card
from components import search_bar

class UserDetailsPage:
    def __init__(self,master):
        self.master = master
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              bg_color="#ffffff")
        
        self.upper_frame2 = CTkFrame(self.frame,
                                fg_color="transparent",
                                bg_color="transparent",
                                width=1920,
                                height=70,
                                border_color="#C6C6C6",
                                border_width=0,
                                corner_radius=0)
        
        self.upper_frame2.pack(padx=0,pady=0,side="top",fill="x")

        self.card_frame = CTkFrame(self.frame,fg_color="#ffffff",
                              bg_color="#ffffff")
        self.card_frame.pack(padx=0,pady=0,side="top",fill="x")

        self.search_bar_frame = search_bar.SearchBar(self.upper_frame2)
        self.search_bar_frame.entry.configure(placeholder_text = "Search Users by name or id")
        self.search_bar_frame.pack(padx=10,pady=5,side="right")
        self.search_bar_frame.search_btn.bind("<Button-1>",lambda e: self.apply_search_filter(self.search_bar_frame.entry.get()))
        self.search_bar_frame.entry.bind("<Return>",lambda e: self.apply_search_filter(self.search_bar_frame.entry.get()))
        self.search_bar_frame.search_options_btn.bind("<Button-1>",lambda e: self.master.focus())




        user_ids = self.get_all_users()
        user_cards = []
        for i in user_ids:
            user_card = user_info_card.UserCard(self.card_frame,i)
            user_cards.append(user_card)
        DrawBooks.draw_books(self.card_frame,user_cards)

    def get_all_users(self):
        # mysql_tables.cur.execute("select user_id from users")
        mysql_tables.cur.execute("""SELECT u.user_id
                                    FROM users u
                                    LEFT JOIN students s ON u.user_id = s.student_id
                                    LEFT JOIN scholars sc ON u.user_id = sc.scholar_id
                                    LEFT JOIN faculty f ON u.user_id = f.faculty_id
                                    LEFT JOIN librarian l ON u.user_id = l.lib_id
                                    WHERE s.student_id IS NOT NULL
                                    OR sc.scholar_id IS NOT NULL
                                    OR f.faculty_id IS NOT NULL
                                    OR l.lib_id IS NOT NULL;
                                    """)
        user_ids = mysql_tables.cur.fetchall()
        new = [x[0] for x in user_ids]
        return new
    

# Search user Functions..........................
    def apply_search_filter(self,search_text):
        for widget in self.card_frame.winfo_children():
            widget.destroy()
        books = self.get_users_by_id_name(search_text)
        DrawBooks.draw_books(self.card_frame,books)
    
    def get_users_by_id_name(self,search_text):
        cur = mysql_tables.cur
        results = []

        # Search in students
        cur.execute("""
            SELECT student_id
            FROM students
            WHERE student_id LIKE %s
            OR first_name LIKE %s
            OR last_name LIKE %s
        """, (f"%{search_text}%", f"%{search_text}%", f"%{search_text}%"))
        results.extend([r[0] for r in cur.fetchall()])

        # Search in faculty
        cur.execute("""
            SELECT faculty_id
            FROM faculty
            WHERE faculty_id LIKE %s
            OR first_name LIKE %s
            OR last_name LIKE %s
        """, (f"%{search_text}%", f"%{search_text}%", f"%{search_text}%"))
        results.extend([r[0] for r in cur.fetchall()])

        # Search in scholars
        cur.execute("""
            SELECT scholar_id
            FROM scholars
            WHERE scholar_id LIKE %s
            OR first_name LIKE %s
            OR last_name LIKE %s
        """, (f"%{search_text}%", f"%{search_text}%", f"%{search_text}%"))
        results.extend([r[0] for r in cur.fetchall()])

        # Search in librarian
        cur.execute("""
            SELECT lib_id
            FROM librarian
            WHERE lib_id LIKE %s
            OR first_name LIKE %s
            OR last_name LIKE %s
        """, (f"%{search_text}%", f"%{search_text}%", f"%{search_text}%"))
        results.extend([r[0] for r in cur.fetchall()])

        user_details = []
        for user_id in results:
            user_details.append(user_info_card.UserCard(self.card_frame,user_id))
        return user_details



 
    

# / Search User  Functions.........................
    
    # def apply_search_filter(search_text):
    #     pass
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = "both",expand = True)
    def pack_forget(self):
        self.frame.pack_forget()