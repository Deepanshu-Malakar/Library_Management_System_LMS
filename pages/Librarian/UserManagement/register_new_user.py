from tkinter import *
from customtkinter import *
from PIL import Image
from backend import register_users
from tkinter import messagebox
from components import colors as c
set_appearance_mode("light")

class colors:
    def __init__(self):
        self.purple = "#613287"
        self.pink = "#D0A2E9"
        self.grey = "#EAE6E6"
        self.base_color = c.new_button_color# "#4153A3"


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
                              text_color=colors().base_color,
                            #   text_color="black",
                              font=("roboto",12,"bold"),
                              )
        self.label.place(x=5,y=0)


        underline_width = 43
        self.underline = CTkLabel(self.frame,
                              text=underline_width*"_",
                              text_color=colors().base_color,
                            #   text_color="black",
                              font=("roboto",13,"bold"),
                              )
        self.underline.place(x=5,y=37)

        self.entry = CTkEntry(self.frame,
                              show = "*" if self.hide else None,
                              text_color=colors().base_color,
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










class RegisterPage:
    def __init__(self,master):
        self.master = master
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              bg_color="#ffffff")
        self.create_register_user_frame()

    def create_register_user_frame(self):
        self.register_user_frame = CTkFrame(self.frame,
                                            fg_color="transparent",
                                            border_width=1,
                                            border_color="#ededed")
        self.title_label = CTkLabel(self.register_user_frame,
                                    text="Enter Details of User",
                                    font=("roboto",16,"bold"))
        self.title_label.pack(pady=10,padx=20)

        self.user_id = Form(self.register_user_frame,"User ID")
        self.user_id.pack(pady=10,padx=20)

        self.email = Form(self.register_user_frame,"Email")
        self.email.pack(pady=10,padx=20)

        self.role = CTkComboBox(self.register_user_frame,
                                values=["Student","Faculty","Scholar","Librarian"],
                                width=240,
                                fg_color="#f5f8ff",
                                dropdown_fg_color="#ffffff",
                                border_width=0,
                                text_color=colors().base_color,
                                dropdown_text_color=colors().base_color,
                                button_hover_color="#173957")
        self.role.pack(pady=10,padx=20)

        self.register_btn = CTkButton(self.register_user_frame,
                                      text="Register",
                                      command=self.register_user,
                                      fg_color=colors().base_color,
                                      height=40)
        self.register_btn.pack(pady=10,padx=20)
        self.register_user_frame.pack(padx=10,pady=100)
        

    # Click Functions.................................
    def register_user(self):
        user_id = self.user_id.entry.get()
        email = self.email.entry.get()
        role = self.role.get()
        if user_id == "" or email == "" or role == "":
            messagebox.showerror("Empty Fields","Fill All the information")
            return False

        user_exist = register_users.check_if_user_exist(user_id)
        if user_exist:
            messagebox.showerror("Error","User Already Exist")
        else:
            register_users.insert_user(user_id,email,role)
            messagebox.showinfo("Success","User Added Successfully")
    # /Click Functiond...................................    


    # Placement methods..................................

        
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = "both",expand = True)
    def pack_forget(self):
        self.frame.pack_forget()
    # /Placement methods....................................


if __name__ == "__main__":
    root = CTk()
    root.geometry("800x800")
    frame = RegisterPage(root)
    frame.pack()
    root.mainloop()