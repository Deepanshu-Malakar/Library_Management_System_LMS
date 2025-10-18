from tkinter import *
from customtkinter import *
from PIL import Image

from pages.Librarian.BookManagement import sidebar

from pages.Librarian.BookManagement import IssueBooks
from pages.Librarian.BookManagement import ReserveBooks
from pages.Librarian.BookManagement import RequestedBooks
from pages.Librarian.BookManagement import ReturnBooks
from pages.Librarian.BookManagement import AddBooks
from pages.Librarian.BookManagement import DueBooks

class Page:
    def __init__(self,master,sidebar_control:sidebar.Sidebar_control):
        self.current_tab = "Issue Books"
        self.master = master
        self.sidebar_control = sidebar_control
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              corner_radius=0)
        self.create_sidebar()
        self.apply_page_controls()
        self.page_frame = IssueBooks.HomePage(self.frame)
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
        self.sidebar.issue_books_btn.button.bind("<Button-1>",self.open_issue_books_page)
        self.sidebar.return_books_btn.button.bind("<Button-1>",self.open_return_books_page)
        self.sidebar.reserve_books_btn.button.bind("<Button-1>",self.open_reserve_books_page)
        self.sidebar.due_books_btn.button.bind("<Button-1>",self.open_due_books_page)
        self.sidebar.requested_books_btn.button.bind("<Button-1>",self.open_requested_books_page)
        self.sidebar.add_books_btn.button.bind("<Button-1>",self.open_add_books_page)

    def open_issue_books_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = IssueBooks.IssuePage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Home"

    def open_return_books_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = ReturnBooks.ReturnPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Favourites"

    def open_reserve_books_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = ReserveBooks.ReservePage(self.frame)
        self.page_frame.pack()
        self.current_tab = "History"

    def open_requested_books_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = RequestedBooks.RequestedPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Study section"

    def open_due_books_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = DueBooks.DuePage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Reserved Books"

    def open_add_books_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = AddBooks.AddPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Reserved Books"
    # / Page changing controls...........................................


    # placement methods..................................................
    def pack(self):
        self.frame.pack(padx=0,pady=0,fill="both",expand=True,side="top")
    def pack_forget(self):
        self.frame.pack_forget()
    # / placement methods.................................................