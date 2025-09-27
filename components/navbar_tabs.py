from tkinter import *
from customtkinter import *
from PIL import *
from components import colors

class NavbarTabs:
    def __init__(self,master,text,is_active=False):
        self.master = master
        self.text = text
        self.is_active = is_active
        self.create_tab()
        self.apply_hover_effects()

    def create_tab(self):
        self.frame = CTkFrame(self.master,
                              fg_color= "transparent",
                              bg_color= "transparent",
                              corner_radius=0)
        
        self.button = CTkButton(self.frame,
                                text=self.text,
                                fg_color="transparent",
                                bg_color="transparent",
                                text_color = colors.base_color if self.is_active else colors.sidebar,
                                font=("roboto",12,"bold"),
                                hover_color=colors.book_base_old,
                                width=150)
        self.button.grid(row=0,column=0,padx=5,pady=10)

        self.underline = CTkLabel(self.frame,
                                  fg_color="transparent",
                                  text="_________________",
                                  width=50,
                                  height=1,
                                  text_color=colors.base_color if self.is_active else colors.book_base)
        self.underline.place(x=30,y=36)

# placement methods................
    def pack(self,padx=0,pady=0,fill="left"):
        self.frame.pack(padx=padx,pady=pady,fill=fill)
    def place(self,x,y):
        self.frame.place(x=x,y=y)
    def grid(self,row,column,padx=0,pady=0):
        self.frame.grid(row=row,column=column,padx=padx,pady=pady)
# / placement methods.................


# Hover effects............
    def apply_hover_effects(self):
        self.frame.bind("<Enter>",self.hover)
        self.frame.bind("<Leave>",self.unhover)
        self.button.bind("<Enter>",self.hover)
        self.button.bind("<Leave>",self.unhover)
    def hover(self,event):
        self.frame.configure(fg_color = colors.book_base_old,bg_color = colors.book_base)
    def unhover(self,event):
        self.frame.configure(fg_color = "transparent",bg_color = "transparent")

# / Hover effects.............


# Click Effects...................
    def unselect(self):
        self.is_active = False
        self.button.configure(text_color = colors.sidebar)
        self.underline.configure(text_color = colors.book_base)

    def click(self):
        self.is_active = True
        self.button.configure(text_color = colors.base_color)
        self.underline.configure(text_color = colors.base_color)
# / Click Effects....................