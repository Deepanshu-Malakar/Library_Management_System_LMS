from tkinter import *
from customtkinter import *
from PIL import Image
from components import doubt_bubble
from backend import doubts_logic

class MyDoubtsPage:
    def __init__(self,master,student_record):
        self.student_record = student_record
        self.master = master
        self.frame = CTkScrollableFrame(self.master,
                              fg_color="#ffffff",
                              bg_color="#ffffff")
        self.show_doubts()
    def show_doubts(self):
        doubts = doubts_logic.get_my_doubts(self.student_record["student id"])
        for doubt in doubts:
            doubt_icon = doubt_bubble.Doubt(self.frame,doubt[0],doubt[1],doubt[2],self.student_record["student id"])
            doubt_icon.pack()
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = "both",expand = True)
    def pack_forget(self):
        self.frame.pack_forget()