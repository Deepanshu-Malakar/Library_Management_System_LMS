from tkinter import *
from customtkinter import *
from PIL import Image

class AskDoubtPage:
    def __init__(self,master):
        self.master = master
        self.frame = CTkFrame(self.master,
                              fg_color="#8b8888",
                              bg_color="#ffffff")
    
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = "both",expand = True)
    def pack_forget(self):
        self.frame.pack_forget()