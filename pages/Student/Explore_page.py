from tkinter import *
from customtkinter import *
from PIL import Image
from components import sidebar_control_button
from pages.Student.Explore import Explore_sidebar

class Page:
    def __init__(self,master,sidebar_control:Explore_sidebar.Sidebar_control):
        self.master = master
        self.sidebar_control = sidebar_control
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              corner_radius=0)
        self.create_sidebar()


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


    # placement methods..................................................
    def pack(self):
        self.frame.pack(padx=0,pady=0,fill="both",expand=True,side="top")
    def pack_forget(self):
        self.frame.pack_forget()
    # / placement methods.................................................