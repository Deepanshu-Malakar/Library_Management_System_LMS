from tkinter import *
from customtkinter import *
import pywinstyles

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

class Scholar_Dashboard:
    def __init__(self,master:CTk,username):
        self.master = master
        self.master.state("zoomed")
        pywinstyles.change_header_color(self.master,colors().base_color)
        
        self.username = username
        self.frame = CTkFrame(self.master,
                              corner_radius=0)
        self.label = CTkLabel(self.frame,text="Scholar Dashboard")
        self.label.pack()

    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = 'both',expand = True) 