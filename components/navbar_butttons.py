from tkinter import *
from customtkinter import *
from PIL import Image
from components import colors

class NavbarButtons:
    def __init__(self,master:CTkFrame,image):
        self.master = master
        self.image = image
        self.create_button()

    def create_button(self):
        self.frame = CTkFrame(self.master,
                              fg_color=colors.navbar,
                              bg_color=colors.navbar,
                              border_width=0)
        self.button = CTkButton(self.frame,
                                text="",
                                image=CTkImage(Image.open(self.image),size=(24,24)),
                                fg_color="transparent",
                                bg_color="transparent",
                                hover_color=colors.book_base_old,
                                width=20,
                                height=50,
                                corner_radius=5)
        self.button.pack()       
    
    #click effects........................
    def click(self,master,text):
        self.popup = CTkToplevel(master,fg_color="#ffffff")
        self.popup.geometry("500x500")
        self.popup.title(text)
        # self.popup.focus()
        self.popup.transient(master)     # keeps it on top of master
        self.popup.attributes("-topmost", True)  # brings it above all windows
        self.popup.focus_force()
        self.popup.grab_set()
    #/click effects.......................... 

    # placement methods.........
    def pack(self,padx=0,pady=0,side="left"):
        self.frame.pack(padx=padx,pady=pady,side=side)
    def place(self,x,y):
        self.frame.place(x=x,y=y)
    def grid(self,row,column,padx=0,pady=0):
        self.frame.grid(row=row,column=column,padx=padx,pady=pady)
    # / placement methods...........