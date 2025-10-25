from customtkinter import *
from tkinter import *
# from components import colors as c
from PIL import Image
from backend import favourites_logic
from backend import reserve_book_logic
from backend import reissue_book_logic
from backend import issue_books_logic
# from backend import mysql_tables
from tkinter import messagebox

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
    def __init__(self,master:CTkFrame,logo:str,book_name:str,author:str,edition:int,user:str,issue_date,expiry_date,status):
        self.frame = CTkFrame(master=master,
                              width=360,
                              height=280,
                              fg_color=colors.book_base,
                              corner_radius=5,
                              border_color="#DAD2DF",
                              border_width=1)
        self.issue_date = issue_date
        self.expiry_date = expiry_date
        self.user = user
        self.title = book_name
        self.author = author
        self.logo_img = CTkImage(Image.open(logo),size=(180,280))
        self.edition = edition
        self.is_reissued = False
        # self.copies = copies_available
        self.status = status

        self.is_favourite = favourites_logic.check_if_favourites(self.user,self.title,self.author,self.edition)
        self.is_reserved = reserve_book_logic.check_if_book_reserved(self.user,self.title,self.author,self.edition)
        if self.status.lower() == "reissued":
            self.is_reissued = True
        elif self.status.lower() == "issued":
            self.is_reissued == False
        elif self.status.lower() == "due":
            self.is_reissued = True
        elif self.status.lower() == 'returned':
            self.is_reissued == True 
        
        
        
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


        self.issue_date_label = CTkLabel(self.frame,text=f"Issue Date : {self.issue_date}",font=("roboto",12))
        self.issue_date_label.place(x=200,y=115)

         


#     Reissue Button......................
        self.reissue_btn = CTkButton(self.frame,
                                     text="                Book Reissued" if self.is_reissued else "                ReIssue Book",
                                     font=("roboto",12,"bold"),
                                     width=180,
                                     height=40,
                                     corner_radius=0,
                                     fg_color=colors.new_button_color,
                                     hover_color=colors.new_button_color_hover,
                                     anchor="w",
                                     command=self.reissue_btn_click)
        
        self.reissue_btn_img = CTkImage(Image.open("resources/icons/reissued.png" if self.is_reissued else "resources/icons/reissue.png"),size=(17,17))

        self.reissue_btn_img_label = CTkLabel(self.frame,image=self.reissue_btn_img,text="",fg_color=colors.new_button_color,bg_color=colors.new_button_color)



        if self.is_reissued:
            self.reissue_btn.configure(state = "disabled")

        #hover effects.................................
        self.reissue_btn.bind("<Enter>",self.reissue_btn_hover)
        self.reissue_btn.bind("<Leave>",self.reissue_btn_unhover)
        
        # / hover effectss....................................

#    Reserve Button...............................................

        self.reserve_btn = CTkButton(self.frame,
                                     text="                Reserved" if self.is_reserved else "                Reserve",
                                     font=("roboto",12,"bold"),
                                     width=180,
                                     height=40,
                                     corner_radius=0,
                                     fg_color=colors.new_button_color,
                                     hover_color=colors.new_button_color_hover,
                                     anchor="w",
                                     command=self.reserve_btn_click)
        
        self.reserve_btn_img = CTkImage(Image.open("resources/icons/unreserve2.png" if self.is_reserved else "resources/icons/reserve.png"),size=(17,17))

        self.reserve_btn_img_label = CTkLabel(self.frame,image=self.reserve_btn_img,text="",fg_color=colors.new_button_color,bg_color=colors.new_button_color)



        #hover effects.................................
        self.reserve_btn.bind("<Enter>",self.reserve_btn_hover)
        self.reserve_btn.bind("<Leave>",self.reserve_btn_unhover)
        
        # / hover effectss....................................

# Due Button....................................
        self.fine = issue_books_logic.pending_fine(self.user)
        self.due_btn = CTkButton(self.frame,
                                     text=f"                Fine = Rs {self.fine}.00 ",
                                     font=("roboto",12,"bold"),
                                     width=180,
                                     height=40,
                                     corner_radius=0,
                                     fg_color="#7C0B0B",
                                     hover_color="#5F0A0A",
                                     anchor="w",
                                     command=self.due_btn_click)
        
        self.due_btn_img = CTkImage(Image.open("resources/icons/due books light.png"),size=(17,17))

        self.due_btn_img_label = CTkLabel(self.frame,image=self.due_btn_img,text="",fg_color="#7C0B0B",bg_color="#7C0B0B")



        #hover effects.................................
        self.due_btn.bind("<Enter>",self.due_btn_hover)
        self.due_btn.bind("<Leave>",self.due_btn_unhover)
        
        # / hover effectss....................................
# Due Button....................................

        if self.status.lower() == "issued" or self.status.lower() == 'reissued':
            self.reissue_btn_img_label.place(x=200,y=190) 
            self.reissue_btn.place(x=180,y=185)
            self.expiry_date_label = CTkLabel(self.frame,text=f"Expiry Date : {self.expiry_date}",font=("roboto",12),text_color="black")
            self.expiry_date_label.place(x=200,y=150)

        elif self.status.lower() == 'returned':
            self.reserve_btn_img_label.place(x=200,y=190)
            self.reserve_btn.place(x=180,y=185)
            self.expiry_date_label = CTkLabel(self.frame,text=f"Returned On : {self.expiry_date}",font=("roboto",12),text_color="black")
            self.expiry_date_label.place(x=200,y=150)

        elif self.status.lower() == 'due':
            self.due_btn_img_label.place(x=200,y=190)
            self.due_btn.place(x=180,y=185)
            self.expiry_date_label = CTkLabel(self.frame,text=f"Expired On : {self.expiry_date}",font=("roboto",12),text_color="#9b2424")
            self.expiry_date_label.place(x=200,y=150)

# / Reserve Button.................................................




        self.favourite_btn = CTkButton(self.frame,
                                       text="                Favourites",
                                       font=("roboto",12,"bold"),
                                       width=180,
                                       height=40,
                                       corner_radius=0,
                                       fg_color=colors.new_button_color,
                                       hover_color=colors.new_button_color_hover,
                                       anchor="w",
                                       command=self.favourite_btn_click)
        
  
        self.favourite_btn_img = CTkImage(Image.open("resources/icons/unfavourite2.png" if self.is_favourite else "resources/icons/favourites.png"),size=(17,17))

        self.favourite_btn_img_label = CTkLabel(self.frame,image=self.favourite_btn_img,text="",fg_color=colors.new_button_color,bg_color=colors.new_button_color)

        self.favourite_btn_img_label.place(x=200,y=225)

        self.favourite_btn.place(x=180,y=220)

        #hover effects.................................
        self.favourite_btn.bind("<Enter>",self.favourite_btn_hover)
        self.favourite_btn.bind("<Leave>",self.favourite_btn_unhover)

        self.frame.bind("<Enter>",self.frame_hover)
        self.frame.bind("<Leave>",self.frame_unhover)
        self.title_label.bind("<Enter>",self.frame_hover)
        self.author_label.bind("<Enter>",self.frame_hover)
        # self.copies_label.bind("<Enter>",self.frame_hover)
        self.issue_date_label.bind("<Enter>",self.frame_hover)
        self.expiry_date_label.bind("<Enter>",self.frame_hover)
        self.edition_label.bind("<Enter>",self.frame_hover)
        self.logo_label.bind("<Enter>",self.frame_hover)
        self.logo_label.bind("<Leave>",self.frame_unhover)

        self.favourite_btn.bind("<Enter>",self.frame_hover)
        self.favourite_btn.bind("<Leave>",self.frame_unhover)
        self.reissue_btn.bind("<Enter>",self.frame_hover)
        self.reissue_btn.bind("<Leave>",self.frame_unhover)
        self.reserve_btn.bind("<Enter>",self.frame_hover)
        self.reserve_btn.bind("<Leave>",self.frame_unhover)
        self.due_btn.bind("<Enter>",self.frame_hover)
        self.due_btn.bind("<Leave>",self.frame_unhover)
        
        # / hover effectss....................................

        # description hover effects....
        self.logo_label.bind("<Enter>",self.show_description)
        self.logo_label.bind("<Leave>",self.hide_description)

        # / description hover effects....




#Hover effects funtions...

    def reissue_btn_hover(self,event):
        self.reissue_btn_img_label.configure(fg_color = colors.new_button_color_hover,bg_color = colors.new_button_color_hover)

    def reissue_btn_unhover(self,event):
        self.reissue_btn_img_label.configure(fg_color = colors.new_button_color,bg_color = colors.new_button_color)

    def favourite_btn_hover(self,event):
        self.favourite_btn_img_label.configure(fg_color = colors.new_button_color_hover,bg_color = colors.new_button_color_hover)

    def favourite_btn_unhover(self,event):
        self.favourite_btn_img_label.configure(fg_color = colors.new_button_color,bg_color = colors.new_button_color)

    def frame_hover(self,event):
        self.frame.configure(border_color = colors.base_color,border_width=1.5)

    def frame_unhover(self,event):
        self.frame.configure(border_color = "#DAD2DF",border_width = 1)

    def reserve_btn_hover(self,event):
        self.reserve_btn_img_label.configure(fg_color = colors.new_button_color_hover,bg_color = colors.new_button_color_hover)

    def reserve_btn_unhover(self,event):
        self.reserve_btn_img_label.configure(fg_color = colors.new_button_color,bg_color = colors.new_button_color)

    def due_btn_hover(self,event):
        self.due_btn_img_label.configure(fg_color = "#5F0A0A",bg_color = "#5F0A0A")

    def due_btn_unhover(self,event):
        self.due_btn_img_label.configure(fg_color = "#7C0B0B",bg_color = "#7C0B0B")


#/ Hover effects functions......



# Click Functions........

    def favourite_btn_click(self):
        if self.is_favourite:
            self.favourite_btn_img_label.configure(image = CTkImage(Image.open("resources/icons/favourites.png"),size=(17,17)))
            favourites_logic.delete_from_favourites(self.user,self.title,self.author,self.edition)
            self.is_favourite = False
        else:
            self.favourite_btn_img_label.configure(image = CTkImage(Image.open("resources/icons/unfavourite2.png"),size=(17,17)))
            favourites_logic.add_to_favourites(self.user,self.title,self.author,self.edition)
            self.is_favourite = True

    def reissue_btn_click(self):
        if self.is_reissued:

            self.reissue_btn_img_label.configure(image = CTkImage(Image.open("resources/icons/reissued.png"),size=(17,17)))
            self.reissue_btn.configure(text="                Re Issued")
            self.is_reissued = True
            self.reissue_btn.configure(state = "disabled")

        else:
            if (reissue_book_logic.reissue_book(self.user,self.title,self.author,self.edition)):
                self.reissue_btn_img_label.configure(image = CTkImage(Image.open("resources/icons/reissued.png"),size=(17,17)))
                self.reissue_btn.configure(text="                Re Issued")
                self.is_reissued = True
                self.reissue_btn.configure(state = "disabled")
                self.expiry_date = reissue_book_logic.get_expiry_date_reissued(self.user,self.title,self.author,self.edition)
                self.expiry_date_label.configure(text=f"Expiry Date : {self.expiry_date}")

    def reserve_btn_click(self):
        if self.is_reserved:
            if not reserve_book_logic.unreserve_book(self.user,self.title,self.author,self.edition):
                messagebox.showerror("Cant UnReserve","You cannot unreserve this book")
                return
            self.reserve_btn_img_label.configure(image = CTkImage(Image.open("resources/icons/reserve.png"),size=(17,17)))
            self.reserve_btn.configure(text="                Reserve")
            self.is_reserved = False

        else:
            if not reserve_book_logic.reserve_book(self.user,self.title,self.author,self.edition):
                messagebox.showerror("Can't reserve book","Not enough copies available to reserve")
                return
            self.reserve_btn_img_label.configure(image = CTkImage(Image.open("resources/icons/unreserve2.png"),size=(17,17)))
            self.reserve_btn.configure(text="                Reserved")
            self.is_reserved = True

    
    def due_btn_click(self):
        pass


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
                   user="123cs0056",
                   issue_date="10-10-2025",
                   expiry_date="10-10-2025",
                   status="due")
    b1.pack(padx=10,pady=10)
    root.mainloop()