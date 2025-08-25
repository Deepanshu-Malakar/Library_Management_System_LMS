from customtkinter import *
from tkinter import *

class color:
    def __init__(self):
        self.base_color = "#4153A3"
        self.disable_buttons = "#535769"
        self.fine = "#DF3939"
        self.sidebar = "#292B34"
        self.book_base = "#EEE8F2"
        self.new_button_color = "#1A2032"
        self.new_button_color_hover = "#090B12"

colors = color()
set_appearance_mode("light")
from PIL import Image

class Book_icon:
    def __init__(self,master:CTkFrame,logo:str,book_name:str,author:str,edition:int,copies_available,favourite:bool,reserved:bool):
        self.frame = CTkFrame(master=master,
                              width=360,
                              height=280,
                              fg_color=colors.book_base,
                              corner_radius=20,
                              border_color="#DAD2DF",
                              border_width=1)
        self.title = book_name
        self.author = author
        self.logo_img = CTkImage(Image.open(logo),size=(180,280))
        self.edition = edition
        self.copies = copies_available
        self.is_favourite = favourite
        self.is_reserved = reserved
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
        self.title_label.place(x=200,y=20)

        self.author_label = CTkLabel(self.frame,text=f"By : {self.author}",font=("roboto",12))
        self.author_label.place(x=200,y=60)

        self.edition_label = CTkLabel(self.frame,text=f"Edition : {self.edition}",font=("roboto",12))
        self.edition_label.place(x=200,y=100)

        self.copies_label = CTkLabel(self.frame,text=f"Copies Available : {self.copies}",font=("roboto",12))
        self.copies_label.place(x=200,y=140)



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

        self.reserve_btn_img_label.place(x=200,y=185)
        
        self.reserve_btn.place(x=180,y=180)

        #hover effects.................................
        self.reserve_btn.bind("<Enter>",self.reserve_btn_hover)
        self.reserve_btn.bind("<Leave>",self.reserve_btn_unhover)
        
        # / hover effectss....................................



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
        
        # / hover effectss....................................

        # description hover effects....
        self.logo_label.bind("<Enter>",self.show_description)
        self.logo_label.bind("<Leave>",self.hide_description)

        # / description hover effects....




#Hover effects funtions...

    def reserve_btn_hover(self,event):
        self.reserve_btn_img_label.configure(fg_color = colors.new_button_color_hover,bg_color = colors.new_button_color_hover)

    def reserve_btn_unhover(self,event):
        self.reserve_btn_img_label.configure(fg_color = colors.new_button_color,bg_color = colors.new_button_color)

    def favourite_btn_hover(self,event):
        self.favourite_btn_img_label.configure(fg_color = colors.new_button_color_hover,bg_color = colors.new_button_color_hover)

    def favourite_btn_unhover(self,event):
        self.favourite_btn_img_label.configure(fg_color = colors.new_button_color,bg_color = colors.new_button_color)
#/ Hover effects functions......



# Click Functions........

    def favourite_btn_click(self):
        if self.is_favourite:
            self.favourite_btn_img_label.configure(image = CTkImage(Image.open("resources/icons/favourites.png"),size=(17,17)))
            self.is_favourite = False
        else:
            self.favourite_btn_img_label.configure(image = CTkImage(Image.open("resources/icons/unfavourite2.png"),size=(17,17)))
            self.is_favourite = True

    def reserve_btn_click(self):
        if self.is_reserved:
            self.reserve_btn_img_label.configure(image = CTkImage(Image.open("resources/icons/reserve.png"),size=(17,17)))
            self.reserve_btn.configure(text="                Reserve")
            self.is_reserved = False
        else:
            self.reserve_btn_img_label.configure(image = CTkImage(Image.open("resources/icons/unreserve2.png"),size=(17,17)))
            self.reserve_btn.configure(text="                Reserved")
            self.is_reserved = True


# / Click Functions ............



# Description Functions................

    def description(self,text = "No Description"):
        self.summary = self.title + "\n\n" + text
        # for i in range(1,len(text)):
        #     if i%22 == 0:
        #         self.summary += text[i] + " -\n- "
        #     else:
        #         self.summary += text[i]
   

    def show_description(self,event):
        self.logo_label.configure(text = self.summary,image = CTkImage(Image.open("resources/Books/empty book1.png"),size=(180,280)))

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
                   copies_available=12,
                   favourite=False,
                   reserved=False)
    b1.pack(padx=10,pady=10)
    root.mainloop()