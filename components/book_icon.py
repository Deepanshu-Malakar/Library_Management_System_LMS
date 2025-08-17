from customtkinter import *
from tkinter import *
import colors

set_appearance_mode("light")
from PIL import Image

class Book_icon:
    def __init__(self,master:CTkFrame,logo:str,book_name:str,author:str,edition:int,copies_available,favourite:bool,reserved:bool):
        self.frame = CTkFrame(master=master,width=360,height=280,fg_color=colors.book_base)
        self.title = book_name
        self.author = author
        self.logo_img = CTkImage(Image.open(logo),size=(180,280))
        self.edition = edition
        self.copies = copies_available
        self.is_favourite = favourite
        self.is_reserved = reserved
        self.create_book()

    def create_book(self):
        self.logo_label = CTkLabel(self.frame,text="",image=self.logo_img)
        # self.logo_label.grid(row=0,column=0,padx=0,pady=0,rowspan = 7)
        self.logo_label.place(x=0,y=0)

        self.title_label = CTkLabel(self.frame,text=self.title,font=("roboto",12,"bold"))
        # self.title_label.grid(row=0,column=1,padx=10,pady=5)
        self.title_label.place(x=200,y=20)

        self.author_label = CTkLabel(self.frame,text=f"By : {self.author}",font=("roboto",12))
        # self.author_label.grid(row=1,column=1,padx=10,pady=5)
        self.author_label.place(x=200,y=60)

        self.edition_label = CTkLabel(self.frame,text=f"Edition : {self.edition}",font=("roboto",12))
        # self.edition_label.grid(row=2,column=1,padx=10,pady=5)
        self.edition_label.place(x=200,y=100)

        self.copies_label = CTkLabel(self.frame,text=f"Copies Available : {self.copies}",font=("roboto",12))
        # self.copies_label.grid(row=3,column=1,padx=10,pady=5)
        self.copies_label.place(x=200,y=140)

        self.reserve_btn = CTkButton(self.frame,
                                     text="      Unreserve" if self.is_reserved else "      Reserve",
                                     font=("roboto",12,"bold"),
                                     width=180,
                                     height=40,
                                     corner_radius=0,
                                     fg_color=colors.base_color,
                                     image=CTkImage(Image.open("resources/icons/reserve.png"),size=(15,15)),compound="left",
                                     hover_color=colors.disable_buttons,
                                     anchor="w")
        # self.reserve_btn.grid(row=4,column=1,padx=0,pady=0)
        self.reserve_btn.place(x=180,y=180)

        self.favourite_btn = CTkButton(self.frame,
                                       text="      Favourites",
                                       font=("roboto",12,"bold"),
                                       width=180,
                                       height=40,
                                       corner_radius=0,
                                       fg_color=colors.base_color,
                                       image=CTkImage(Image.open("resources/icons/favourites.png"),size=(15,15)),compound="left",
                                       hover_color=colors.disable_buttons,
                                       anchor="w")
        # self.favourite_btn.grid(row=5,column=1,padx=0,pady=0)
        self.favourite_btn.place(x=180,y=220)
    
    
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady)
    
    
    def place(self,x,y):
        self.frame.place(x=x,y=y)

    def grid(self,row,column,padx=0,pady=0):
        self.frame.grid(row=row,column=column,padx=padx,pady=pady)

if __name__ == "__main__":
    root = CTk(fg_color="#ffffff")

    b1 = Book_icon(root,logo="resources/Books/harry potter1.jpg",
                   book_name="Harry Potter and the Philosopher's Stone",
                   author="J.K. Rowlings",
                   edition=1,
                   copies_available=12,
                   favourite=False,
                   reserved=False)
    b1.pack(padx=10,pady=10)
    root.mainloop()