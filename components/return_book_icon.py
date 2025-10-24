from customtkinter import *
from tkinter import *
# from components import colors as c
from PIL import Image
from backend import issue_books_logic
# from backend import issue_books_logic
# from backend import mysql_tables
# from tkinter import messagebox

class color:
    def __init__(self):
        self.base_color = "#4153A3"
        self.disable_buttons = "#535769"
        self.fine = "#DF3939"
        self.sidebar = "#292B34"
        # self.book_base = "#EEE8F2"
        self.book_base = "#ffffff"
        self.new_button_color = "#1A2032"
        self.new_button_color_hover = "#090B12"
        self.book_hover = "#1A2032"
        self.old_hover = "#C0BEC2"

colors = color()
set_appearance_mode("light")


class Book_icon:
    def __init__(self,master:CTkFrame,logo:str,book_name:str,author:str,edition:int,borrower_id,issue_date,expiry_date):#,user:str):
        self.master = master
        self.borrower_id = borrower_id
        self.frame = CTkFrame(master=master,
                              width=360,
                              height=280,
                              fg_color=colors.book_base,
                              corner_radius=5,
                              border_color="#DAD2DF",
                              border_width=1)
        self.issue_date = issue_date
        self.expiry_date = expiry_date
        self.title = book_name
        self.author = author
        self.logo_img = CTkImage(Image.open(logo),size=(180,280))
        self.edition = edition
        # self.is_favourite = favourites_logic.check_if_favourites(self.user,self.title,self.author,self.edition)
        # self.is_reserved = reserve_book_logic.check_if_book_reserved(self.user,self.title,self.author,self.edition)
        self.create_book()
        self.description()

    def create_book(self):
        self.logo_label = CTkLabel(self.frame,
                                   text="",
                                   image=self.logo_img,
                                   font=("roboto",12),
                                   wraplength=160,
                                   justify="center")
        self.logo_label.place(x=0,y=0)

        title = self.title if len(self.title)<=22 else self.title[:20]+".."
        self.title_label = CTkLabel(self.frame,text=title,font=("roboto",12,"bold"))
        self.title_label.place(x=200,y=10)

        self.author_label = CTkLabel(self.frame,text=f"By : {self.author}",font=("roboto",12))
        self.author_label.place(x=200,y=45)

        self.edition_label = CTkLabel(self.frame,text=f"Edition : {self.edition}",font=("roboto",12))
        self.edition_label.place(x=200,y=80)

        self.borrower_id_label = CTkLabel(self.frame,text=f"Borrower Id : {self.borrower_id}",font=("roboto",12))
        self.borrower_id_label.place(x=200,y=115)

        self.Issue_date_label = CTkLabel(self.frame,text=f"Issue Date : {self.issue_date}",font=("roboto",12))
        self.Issue_date_label.place(x=200,y=150)

        self.expiry_date_label = CTkLabel(self.frame,text=f"Expiry Date : {self.expiry_date}",font=("roboto",12))
        self.expiry_date_label.place(x=200,y=185)


        self.return_btn = CTkButton(self.frame,
                                       text="                Return Book",
                                       font=("roboto",12,"bold"),
                                       width=180,
                                       height=40,
                                       corner_radius=0,
                                       fg_color=colors.new_button_color,
                                       hover_color=colors.new_button_color_hover,
                                       anchor="w",
                                       command=self.return_btn_click)
        
  
        self.return_btn_img = CTkImage(Image.open("resources/icons/return book light.png"),size=(17,17))

        self.return_btn_img_label = CTkLabel(self.frame,image=self.return_btn_img,text="",fg_color=colors.new_button_color,bg_color=colors.new_button_color)

        self.return_btn_img_label.place(x=200,y=225)

        self.return_btn.place(x=180,y=220)

        #hover effects.................................
        self.return_btn.bind("<Enter>",self.return_btn_hover)
        self.return_btn.bind("<Leave>",self.return_btn_unhover)

        self.frame.bind("<Enter>",self.frame_hover)
        self.frame.bind("<Leave>",self.frame_unhover)
        self.title_label.bind("<Enter>",self.frame_hover)
        self.author_label.bind("<Enter>",self.frame_hover)
        self.Issue_date_label.bind("<Enter>",self.frame_hover)
        self.expiry_date_label.bind("<Enter>",self.frame_hover)
        self.edition_label.bind("<Enter>",self.frame_hover)
        self.logo_label.bind("<Enter>",self.frame_hover)
        self.logo_label.bind("<Leave>",self.frame_unhover)

        self.return_btn.bind("<Enter>",self.frame_hover)
        self.return_btn.bind("<Leave>",self.frame_unhover)
 
        
        # / hover effectss....................................

        # description hover effects....
        self.logo_label.bind("<Enter>",self.show_description)
        self.logo_label.bind("<Leave>",self.hide_description)

        # / description hover effects....




#Hover effects funtions...

    def return_btn_hover(self,event):
        self.return_btn_img_label.configure(fg_color = colors.new_button_color_hover,bg_color = colors.new_button_color_hover)

    def return_btn_unhover(self,event):
        self.return_btn_img_label.configure(fg_color = colors.new_button_color,bg_color = colors.new_button_color)

    def frame_hover(self,event):
        self.frame.configure(border_color = colors.base_color,border_width=1.5)

    def frame_unhover(self,event):
        self.frame.configure(border_color = "#DAD2DF",border_width = 1)
#/ Hover effects functions......



# Click Functions........

    def return_btn_click(self):
        issue_books_logic.return_book(self.borrower_id,self.title,self.author,self.edition)
        # user_id = self.borrower_id_entry.get()
        # if user_id == "":
        #     messagebox.showerror("Error","Borrower ID cannot be null")
        #     return
        # if(issue_books_logic.issue_book(user_id,self.title,self.author,self.edition)):
        #     self.copies = mysql_tables.get_copies_of_book(self.title,self.author,self.edition)
        #     self.copies_label.configure(text=f"Copies Available : {self.copies}")
        #     self.borrower_id_entry.delete(0,END)
        #     self.master.focus()

        




# / Click Functions ............



# Description Functions................

    def description(self,text = "No Description"):
        self.summary = self.title + "\n\n" + text


    def show_description(self,event):
        self.logo_label.configure(text = self.summary,image = CTkImage(Image.open("resources/Books/empty book4.jpg"),size=(180,280)))

    def hide_description(self,event):
        self.logo_label.configure(text = "",image = self.logo_img)

# / Description Functions..............



# Placement methods....
    
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady)
    
    def place(self,x,y):
        self.frame.place(x=x,y=y)

    def grid(self,row,column,padx=0,pady=0):
        self.frame.grid(row=row,column=column,padx=padx,pady=pady)

# /Placement methods....

if __name__ == "__main__":
    root = CTk(fg_color="#ffffff")

    b1 = Book_icon(root,logo="resources/Books/harry potter1.jpg",
                   book_name="Harry Potter and the Philosopher's Stone",
                   author="J.K. Rowlings",
                   edition=1,
                   borrower_id="123cs0056",
                   issue_date="20-11-2022",
                   expiry_date="27-11-2022")
                #    user='123cs0056')
    b1.pack(padx=10,pady=10)
    root.mainloop()