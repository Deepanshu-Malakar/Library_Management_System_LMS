from tkinter import *
from customtkinter import *
from PIL import Image
from backend import mysql_tables
from backend import DrawBooks
from components import user_info_card

class UserDetailsPage:
    def __init__(self,master):
        self.master = master
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              bg_color="#ffffff")

        user_ids = self.get_all_users()
        user_cards = []
        for i in user_ids:
            user_card = user_info_card.UserCard(self.frame,i)
            user_cards.append(user_card)
        DrawBooks.draw_books(self.frame,user_cards)
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
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = "both",expand = True)
    def pack_forget(self):
        self.frame.pack_forget()