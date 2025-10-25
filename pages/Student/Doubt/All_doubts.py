from tkinter import *
from customtkinter import *
from PIL import Image

class AllDoubtsPage:
    def __init__(self,master,student_record):
        self.student_record = student_record
        self.master = master
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              bg_color="#ffffff")
        self.label = CTkLabel(self.frame,
                              text="Student All Doubts")
        self.label.pack()
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = "both",expand = True)
    def pack_forget(self):
        self.frame.pack_forget()