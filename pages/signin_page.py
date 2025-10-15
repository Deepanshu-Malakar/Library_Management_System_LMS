from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import Image
from pages.Student import Student_Dashboard
from pages.Librarian import Librarian_Dashboard
from pages.Scholar import Scholar_Dashboard
from pages.Faculty import Faculty_Dashboard
from tkinter import messagebox

class colors:
    def __init__(self):
        self.purple = "#613287"
        self.pink = "#D0A2E9"
        self.grey = "#EAE6E6"


class Form:
    def __init__(self,master,text,hide = False):
        self.master = master
        self.text = text
        self.hide = hide
        self.frame = CTkFrame(self.master,
                              fg_color="transparent",
                              bg_color="transparent",
                              width=250,
                              height=60)
        self.create_form()
        
    def create_form(self):
        self.label = CTkLabel(self.frame,
                              text=self.text,
                              text_color=colors().purple,
                              font=("roboto",12),
                              )
        self.label.place(x=5,y=0)


        underline_width = 43
        self.underline = CTkLabel(self.frame,
                              text=underline_width*"_",
                              text_color=colors().purple,
                              font=("roboto",13),
                              )
        self.underline.place(x=5,y=37)

        self.entry = CTkEntry(self.frame,
                              show = "*" if self.hide else None,
                              text_color=colors().purple,
                              fg_color="transparent",
                              bg_color="transparent",
                              border_width=0,
                              width=220,
                              font=("roboto",12))
        self.entry.place(x=0,y=27)

    #placement methods..........
    def place(self,x,y):
        self.frame.place(x=x,y=y)
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady)
    def grid(self,row,column,padx=0,pady=0):
        self.frame.grid(row=row,column=column,padx=padx,pady=pady)

class Signup:
    def __init__(self, master, role):
        self.master = master
        self.role = role
        self.width = 2228
        self.height = 1480
        self.factor = 0.5


        self.page_frame = CTkFrame(self.master,
                                   fg_color="light blue",
                                   width=self.factor*self.width,
                                   height=self.factor*self.height)

        self.background_img = CTkImage(Image.open("resources/Background images/new background 2.png"),
                                       size=(self.factor*self.width,self.factor*self.height))
        self.background_img_label = CTkLabel(self.page_frame,
                                             text="",
                                             image=self.background_img)
        self.background_img_label.place(x=0,y=0)



        x_offest = 150
        y_offset = 190
        self.frame = CTkFrame(self.page_frame, 
                              fg_color="white",
                              bg_color=colors().pink,
                              corner_radius=20)
        self.frame.place(x = self.width*self.factor//2 - x_offest, y=self.height*self.factor//2 - y_offset)

        # Title
        self.title_label = CTkLabel(self.frame,
                                    text="Sign in to your account", 
                                    font=("roboto", 16, "bold"),
                                    text_color=colors().purple)
        self.title_label.pack(padx=60, pady=30)

        # Username
        self.username = Form(self.frame,"User ID:")
        self.username.pack()

        self.password = Form(self.frame,"Password:",hide=True)
        self.password.pack(pady=30)

        self.hide_password_btn = CTkButton(self.password.frame,
                                           text="",
                                           image=CTkImage(Image.open("resources/icons/eye off.png"),size=(20,20)),
                                           fg_color="transparent",
                                           bg_color="transparent",
                                           width=30,
                                           corner_radius=0,
                                           hover_color=colors().grey,
                                           command=self.hide_text)
        
        self.hide_password_btn.place(x=215,y=25)

        self.forgot_password_label = CTkLabel(self.frame, 
                                              text="Forgot Password?", 
                                              font=("Arial", 12, "underline"), 
                                              text_color="blue", 
                                              cursor="hand2")
        
        self.forgot_password_label.pack(anchor="e", padx=20,pady=0)
        self.forgot_password_label.bind("<Button-1>", self.forgot_password)

        self.signin_button = CTkButton(self.frame, 
                                       text="Login", 
                                       command=self.signin,
                                       width=60,
                                       fg_color=colors().purple,
                                       font=("roboto",12))
        self.signin_button.pack(pady=30)


#placement methods............................
    def pack(self, padx=0, pady=0):
        self.page_frame.pack(padx=padx, pady=pady)
#/ placement methods................................



#click functions................................
    def hide_text(self):
        if self.password.hide == False:   # if password is not hidden
            self.password.entry.configure(show = "*")
            self.hide_password_btn.configure(image = CTkImage(Image.open("resources/icons/eye off.png"),size=(20,20)))
            self.password.hide = True
        
        elif self.password.hide == True:   # if password is  hidden
            self.password.entry.configure(show = "")
            self.hide_password_btn.configure(image = CTkImage(Image.open("resources/icons/eye on.png"),size=(20,20)))
            self.password.hide = False

    def forgot_password(self, event):
        messagebox.showinfo("Forgot Password", "Password recovery instructions would be sent to your registered email.")
        
    def signin(self):
        username = self.username.entry.get()
        password = self.password.entry.get()

        
        messagebox.showinfo("Success", f"Account logged in for {username}")

        self.username.entry.delete(0, END)
        self.password.entry.delete(0, END)

        if self.role.lower() == "student":
            self.page_frame.pack_forget()
            self.frame = Student_Dashboard.Student_Dashboard(self.master,username)
            self.frame.pack()
            
        elif self.role.lower() == "librarian":
            self.page_frame.pack_forget()
            self.frame = Librarian_Dashboard.Librarian_Dashboard(self.master,username)
            self.frame.pack()
        elif self.role.lower() == "faculty":
            self.page_frame.pack_forget()
            self.frame = Faculty_Dashboard.Faculty_Dashboard(self.master,username)
            self.frame.pack()
        elif self.role.lower() == "scholar":
            self.page_frame.pack_forget()
            self.frame = Scholar_Dashboard.Scholar_Dashboard(self.master,username)
            self.frame.pack()

        # self.confirm_entry.delete(0, END)


if __name__ == "__main__":
    root = CTk()
    width = 2228
    height = 1480
    factor = 0.5
    # root = CTk(fg_color="#7F495D")
    root.geometry(f"{width*factor}x{height*factor}")
    # root.geometry("400x400")
    # root.title("Signup Page")

    signup_page = Signup(root,role="Student")
    signup_page.pack(0, 0)

    root.mainloop()