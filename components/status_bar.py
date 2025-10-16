from tkinter import *
from customtkinter import *
import pywinstyles

class color:
    def __init__(self):
        self.base_color = "#4153A3"
        self.base_color2 = "#7477DD"
        self.dark_base = "#1A2032"
        self.dark_base2 = "#3D3E43"
        self.disable_buttons = "#535769"
        self.fine = "#DF3939"
        self.sidebar = "#292B34"
        self.book_base = "#EEE8F2"
        self.new_button_color = "#1A2032"
        self.new_button_color_hover = "#090B12"
        self.book_hover = "#1A2032"
        self.old_hover = "#C0BEC2"

colors = color()


class StatusBar:
    def __init__(self,master:CTkFrame,username:str,reserved_books:int = 0, issued_books:int = 0, outstanding_fines:int = 0,due_books:int = 0):
        self.username = username
        self.reserved_books = reserved_books
        self.issued_books = issued_books
        self.outstandingfines = outstanding_fines
        self.due_books = due_books
        self.master = master
        self.create_status_bar()
        
    def create_status_bar(self):
        self.frame = CTkFrame(self.master,
                              fg_color=colors.base_color,
                              bg_color=colors.base_color,
                              width=1920,
                              height=30)
        # pywinstyles.set_opacity(self.frame,0.8)



        self.username_label = CTkLabel(self.frame ,
                                       text= self.username,
                                       fg_color="transparent",
                                       bg_color="transparent",
                                       text_color="white",
                                       font=("roboto",12,"bold"))
        self.username_label.pack(padx=30,pady=5,side="left")

        self.issued_books_label = CTkLabel(self.frame ,
                                       text= f"Books Issued = {self.issued_books}",
                                       fg_color="transparent",
                                       bg_color="transparent",
                                       text_color="white",
                                       font=("roboto",12,"bold"))
        self.issued_books_label.pack(padx=30,pady=5,side="left")

        self.reserved_books_label = CTkLabel(self.frame ,
                                       text= f"Books Reserved = {self.reserved_books}",
                                       fg_color="transparent",
                                       bg_color="transparent",
                                       text_color="white",
                                       font=("roboto",12,"bold"))
        self.reserved_books_label.pack(padx=30,pady=5,side="left")

        self.outstanding_fines_label = CTkLabel(self.frame ,
                                       text= f"Outstanding Fines = {self.outstandingfines}",
                                       fg_color="transparent",
                                       bg_color="transparent",
                                       text_color="white",
                                       font=("roboto",12,"bold"))
        self.outstanding_fines_label.pack(padx=30,pady=5,side="left")

        self.due_books_label = CTkLabel(self.frame ,
                                       text= f"Due Books = {self.due_books}",
                                       fg_color="transparent",
                                       bg_color="transparent",
                                       text_color="white",
                                       font=("roboto",12,"bold"))
        self.due_books_label.pack(padx=30,pady=5,side="left")

        self.credits_label = CTkLabel(self.frame ,
                                       text= f"@ Your Personal Library - An app created by Group-13",
                                       fg_color="transparent",
                                       bg_color="transparent",
                                       text_color="white",
                                       width=700,
                                       justify = "right",
                                       font=("roboto",12,"bold"))
        self.credits_label.pack(padx=30,pady=5,side="right")

        self.design_frame = CTkFrame(self.frame,
                                     fg_color=colors.base_color2,
                                     bg_color=colors.base_color2,
                                     height=17,
                                     width=4000)
        self.design_frame.place(x=0,y=0)
        pywinstyles.set_opacity(self.design_frame,0.3)





#placement methods ...........
    def pack(self,padx = 0,pady = 0):
        self.frame.pack(padx=padx,pady=pady,fill='x',side='bottom')

    def place(self,x=0,y=760):
        self.frame.place(x=x,y=y)
# / placement methods ..................




if __name__ == "__main__":
    print("hello")
    set_appearance_mode("light")
    root = CTk()
    status_bar = StatusBar(root,'Deepanshu',1,1,0,0)
    status_bar.place(x=0,y=10)

    root.mainloop()