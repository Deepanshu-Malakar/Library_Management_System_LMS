from tkinter import *
from customtkinter import *
from PIL import Image
from backend import doubts_logic

class AskDoubtPage:
    def __init__(self,master,student_record):
        self.student_record = student_record
        self.master = master
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              bg_color="#ffffff")
        self.doubt_show_frame = CTkFrame(self.frame,
                                         fg_color="transparent")
        


        self.doubt_show_frame.pack(side=TOP,fill="x")

        self.doubts_enter_frame = CTkFrame(self.frame,
                                           fg_color="transparent")
        
        self.entry = CTkEntry(self.doubts_enter_frame,placeholder_text="Enter your doubt")
        self.entry.grid(row=0,column=0,padx=10,pady=10)
        self.send = CTkButton(self.doubts_enter_frame,text="Send",command=self.send_doubt)
        self.send.grid(row=0,column=1)

        self.doubts_enter_frame.pack(side=BOTTOM,fill="x")

    def send_doubt(self):
        self.entry.get()

    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = "both",expand = True)
    def pack_forget(self):
        self.frame.pack_forget()