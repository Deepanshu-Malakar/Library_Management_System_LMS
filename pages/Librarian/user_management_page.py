from tkinter import *
from customtkinter import *
from PIL import Image

from pages.Librarian.UserManagement import sidebar

from pages.Librarian.UserManagement import register_new_user
from pages.Librarian.UserManagement import blacklist_user
from pages.Librarian.UserManagement import suspend_user
from pages.Librarian.UserManagement import user_details


class Page:
    def __init__(self,master,sidebar_control:sidebar.Sidebar_control):
        self.current_tab = "User Details"
        self.master = master
        self.sidebar_control = sidebar_control
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              corner_radius=0)
        self.create_sidebar()
        self.apply_page_controls()
        self.page_frame = user_details.UserDetailsPage(self.frame)
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
        self.sidebar.user_details_btn.button.bind("<Button-1>",self.open_user_details_page)
        self.sidebar.register_new_user_btn.button.bind("<Button-1>",self.open_register_new_user_page)
        self.sidebar.suspended_users_btn.button.bind("<Button-1>",self.open_suspended_users_page)
        self.sidebar.blacklisted_users_btn.button.bind("<Button-1>",self.open_blacklisted_users_page)


    def open_user_details_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = user_details.UserDetailsPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Home"

    def open_register_new_user_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = register_new_user.RegisterPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Favourites"

    def open_suspended_users_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = suspend_user.SuspendPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "History"

    def open_blacklisted_users_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = blacklist_user.BlacklistPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Study section"


    # / Page changing controls...........................................


    # placement methods..................................................
    def pack(self):
        self.frame.pack(padx=0,pady=0,fill="both",expand=True,side="top")
    def pack_forget(self):
        self.frame.pack_forget()
    # / placement methods.................................................