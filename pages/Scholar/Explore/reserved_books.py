from tkinter import *
from customtkinter import *
from PIL import Image

class ReservedBooksPage:
    def __init__(self,master,scholar_record):
        self.scholar_record = scholar_record
        self.master = master
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              bg_color="#ffffff")
        self.label = CTkLabel(self.frame,
                              text="Scholar reserved books")
        self.label.pack()    
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = "both",expand = True)
    def pack_forget(self):
        self.frame.pack_forget()