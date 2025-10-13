from tkinter import *
from customtkinter import *

class Student_Dashboard:
    def __init__(self,master:CTk):
        self.master = master
        self.frame = CTkFrame(self.master)
        self.label = CTkLabel(self.frame,text="Student Dashboard")
        self.label.pack()

    def pack(self):
        self.frame.pack()
