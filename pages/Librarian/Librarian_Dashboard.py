from tkinter import *
from customtkinter import *

class Librarian_Dashboard:
    def __init__(self,master):
        self.master = master
        self.frame = CTkFrame(self.master)
        self.label = CTkLabel(self.frame,text="Librarian Dashboard")
        self.label.pack()

    def pack(self):
        self.frame.pack()
