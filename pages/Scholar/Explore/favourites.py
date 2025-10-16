from tkinter import *
from customtkinter import *
from PIL import Image

class FavouritesPage:
    def __init__(self,master):
        self.master = master
        self.frame = CTkFrame(self.master,
                              fg_color="#8d1e1e",
                              bg_color="#ffffff")
        self.label = CTkLabel(self.frame,
                              text="Scholar Favourites")
        self.label.pack()    
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = "both",expand = True)
    def pack_forget(self):
        self.frame.pack_forget()