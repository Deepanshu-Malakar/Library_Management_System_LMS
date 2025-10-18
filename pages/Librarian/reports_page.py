from tkinter import *
from customtkinter import *
from PIL import Image

class Page:
    def __init__(self,master,sidebar_control:Explore_sidebar.Sidebar_control):
        self.current_tab = "Home"
        self.master = master
        self.sidebar_control = sidebar_control
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              corner_radius=0)
        self.create_sidebar()
        self.apply_page_controls()
        self.page_frame = home.HomePage(self.frame)
        self.page_frame.pack()

    # Working on sidebar..............................................    
    def create_sidebar(self):
        self.sidebar = Explore_sidebar.SideBar(self.frame)
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
        self.sidebar.home_btn.button.bind("<Button-1>",self.open_home_page)
        self.sidebar.favourites_btn.button.bind("<Button-1>",self.open_favourites_page)
        self.sidebar.history_btn.button.bind("<Button-1>",self.open_history_page)
        self.sidebar.study_section_btn.button.bind("<Button-1>",self.open_study_section_page)
        self.sidebar.reserved_books_btn.button.bind("<Button-1>",self.open_reserved_books_page)

    def open_home_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = home.HomePage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Home"

    def open_favourites_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = favourites.FavouritesPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Favourites"

    def open_history_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = history.HistoryPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "History"

    def open_study_section_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = study_section.StudySectionPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Study section"

    def open_reserved_books_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = reserved_books.ReservedBooksPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Reserved Books"
    # / Page changing controls...........................................


    # placement methods..................................................
    def pack(self):
        self.frame.pack(padx=0,pady=0,fill="both",expand=True,side="top")
    def pack_forget(self):
        self.frame.pack_forget()
    # / placement methods.................................................