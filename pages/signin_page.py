from tkinter import *
from customtkinter import *
from pages.Student import Student_Dashboard
from pages.Librarian import Librarian_Dashboard

class Signin_page:
    def __init__(self,master:CTk):
        self.master = master
        self.frame = CTkFrame(self.master)
        self.username = CTkLabel(self.frame,text = "Enter Username")
        self.password = CTkLabel(self.frame,text = "Enter Password")
        self.username_entry = CTkEntry(self.frame)
        self.password_entry = CTkEntry(self.frame)
        self.submit_btn = CTkButton(self.frame,text="Sign in",command=self.click)
        self.role = CTkOptionMenu(self.frame,values=["Student","Faculty","Research Scholar","Librarian"])


        self.username.grid(row = 0 , column = 0, padx = 10 , pady = 10)
        self.username_entry.grid(row = 0 , column = 1, padx = 10, pady = 10)
        self.password.grid(row = 1 , column = 0, padx = 10, pady = 10)
        self.password_entry.grid(row = 1 , column = 1, padx = 10, pady = 10)
        self.role.grid(row = 2 , column = 0, padx = 10, pady = 10)
        self.submit_btn.grid(row = 2 , column = 1, padx = 10, pady = 10)



    # placement methods....................
    def pack(self,padx=0,pady=0,side = TOP):
        self.frame.pack(padx=padx,pady = pady , side = side)
    # // placement methods...................



    # Click Functions.........................
    def click(self):
        role = self.role.get()
        self.frame.pack_forget()

        if role == "Student":
            self.frame = Student_Dashboard.Student_Dashboard(self.master)
            self.frame.pack()
        
        elif role == "Librarian":
            self.frame = Librarian_Dashboard.Librarian_Dashboard(self.master)
            self.frame.pack()

    # // Click Functions......................