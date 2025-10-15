from tkinter import *
from customtkinter import *
from PIL import Image

class Page:
    def __init__(self,master,sidebar_control):
        self.master = master
        self.sidebar_control = sidebar_control
        self.frame = CTkFrame(self.master,
                              fg_color="#9a3b3b",
                              corner_radius=0)
        
    def pack(self):
        self.frame.pack(padx=0,pady=0,fill="both",expand=True)

    def pack_forget(self):
        self.frame.pack_forget()