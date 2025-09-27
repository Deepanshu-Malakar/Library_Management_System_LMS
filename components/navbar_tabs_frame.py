from tkinter import *
from customtkinter import *
from PIL import Image
from components import navbar_tabs

class NavbarTabsFrame:
    def __init_(self,master):
        self.master = master
        self.frame = CTkFrame(self.master, 
                              fg_color= "transparent",
                              bg_color= "transparent",
                              height= 20)
        self.create_frame()
        
    def create_frame(self):
        pass

# Placement Methods..................
    def pack(self,side = "right",padx = 20 , pady = 0):
        self.frame.pack(side = side , padx = padx , pady = pady)
# / Placement Methods......................
        
