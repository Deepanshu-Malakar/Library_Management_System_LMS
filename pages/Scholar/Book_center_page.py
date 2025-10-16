from tkinter import *
from customtkinter import *
from PIL import Image
from components import sidebar_control_button
from pages.Scholar.BookCenter import sidebar

from pages.Scholar.BookCenter import Donate_book
from pages.Scholar.BookCenter import Request_book

class Page:
    def __init__(self,master,sidebar_control:sidebar.Sidebar_control):
        self.master = master
        self.current_tab = "Request"
        self.sidebar_control = sidebar_control
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              corner_radius=0)
        self.create_sidebar()  
        self.apply_page_controls()
        self.page_frame = Request_book.RequestBookPage(self.frame)
        self.page_frame.pack()


    # Working on sidebar..............................................    
    def create_sidebar(self):
        self.sidebar = sidebar.SideBar(self.frame)
        self.sidebar.pack()

        self.sidebar_control.button.bind("<Button-1>",self.sidebar_toggle)
    
    def sidebar_toggle(self,e):
        if self.sidebar.is_expanded:
            self.sidebar.collapse()
            self.sidebar.is_expanded = False

        elif not self.sidebar.is_expanded:
            self.sidebar.expand()
            self.sidebar.is_expanded = True
    # /Working on sidebar..............................................

    # Page changing controls.........................................
    def apply_page_controls(self):
        self.sidebar.request_book_btn.button.bind("<Button-1>",self.open_request_book_page)
        self.sidebar.donate_book_btn.button.bind("<Button-1>",self.open_donate_book_page)


    def open_request_book_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = Request_book.RequestBookPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Request"

    def open_donate_book_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = Donate_book.DonateBookPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Donate"


    # / Page changing controls...........................................



    # placement methods..................................................
    def pack(self):
        self.frame.pack(padx=0,pady=0,fill="both",expand=True,side="top")
    def pack_forget(self):
        self.frame.pack_forget()