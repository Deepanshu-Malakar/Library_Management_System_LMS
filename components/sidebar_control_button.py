from tkinter import *
from customtkinter import *
from PIL import Image

class colors:
    def __init__(self):
        self.base_color = "#4153A3"
        self.disable_buttons = "#535769"
        self.fine = "#DF3939"
        self.sidebar = "#292B34"
        self.book_base_old = "#EEE8F2"
        self.navbar = "#FFFFFF"
        self.navbar_hover = "#ECF3FE"

        # self.book_base = "#EEE8F2"
        self.book_base = "#ffffff"
        self.new_button_color = "#1A2032"
        self.new_button_color_hover = "#090B12"
        self.book_hover = "#1A2032"
        self.old_hover = "#C0BEC2"


        self.folder_bg = "#C7CEE9"
        self.folder_filled = "#5165AA"

class Sidebar_control:
    def __init__(self,master:any,username):
        self.master = master
        self.frame = CTkFrame(self.master,
                              fg_color="transparent",
                              bg_color="transparent",
                              border_color="#ffffff",
                              border_width=0,
                              corner_radius=0)
        
        self.button = CTkButton(self.frame,
                                text="",
                                fg_color="transparent",
                                bg_color="transparent",
                                image=CTkImage(Image.open("resources/icons/sidebar control.png"),size=(24,24)),
                                hover_color= colors().book_base_old,
                                border_width=0,
                                border_color="#ffffff",
                                width=30,
                                corner_radius=0)
                                # command=self.click)
        self.button.pack(padx=5,pady=10,side="left")

        self.label = CTkLabel(self.frame,
                              text=username,
                              fg_color="transparent",
                              bg_color="transparent",
                              font=("roboto",14,"bold"),
                              text_color=colors().sidebar,
                            #   image=CTkImage(Image.open("resources/icons/Hii.png"),size=(24,24)),
                              compound="left")
        self.label.pack(padx=5,pady=10,side="left")



    
    # click functions...............
    # def click(self):
    #     if self.sidebar.is_expanded:
    #         self.collapse()
    #         self.sidebar.is_expanded = False
        
    #     else:
    #         self.expand()
    #         self.sidebar.is_expanded = True

    # def semi_collapse(self):
    #     self.sidebar.home_btn.button.configure(text="",width=5)
    #     self.sidebar.favourites_btn.button.configure(text="",width=5)
    #     self.sidebar.history_btn.button.configure(text="",width=5)
    #     self.sidebar.reserved_books_btn.button.configure(text="",width=5)
    #     self.sidebar.study_section_btn.button.configure(text="",width=5)
        
    # def collapse(self):
    #     self.sidebar.frame.configure(width=0)
    #     self.sidebar.home_btn.grid_forget()
    #     self.sidebar.favourites_btn.grid_forget()
    #     self.sidebar.history_btn.grid_forget()
    #     self.sidebar.study_section_btn.grid_forget()
    #     self.sidebar.reserved_books_btn.grid_forget()

    # def expand(self):
    #     self.sidebar.home_btn.grid(row=1,column=0,padx=0,pady=0)
    #     self.sidebar.favourites_btn.grid(row=2,column=0,padx=0,pady=10)
    #     self.sidebar.history_btn.grid(row=3,column=0,padx=0,pady=0)
    #     self.sidebar.study_section_btn.grid(row=4,column=0,padx=0,pady=10)
    #     self.sidebar.reserved_books_btn.grid(row=5,column=0,padx=0,pady=0)
    # # / Click functions..............



    # placement methods...........
    def pack(self,padx=0,pady=0,side="left"):
        self.frame.pack(padx=padx,pady=pady,side=side)
    
    def place(self,x,y):
        self.frame.place(x=x,y=y)
    
    def grid(self,row,column,padx=0,pady=0):
        self.frame.grid(row=row,column=column,padx=padx,pady = pady)

    # / placement methods..............