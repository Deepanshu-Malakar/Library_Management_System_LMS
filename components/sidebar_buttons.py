from tkinter import *
from customtkinter import *
import pywinstyles
from PIL import Image

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
class SidebarButtons:
    def __init__(self,master,text:str,img_active:str,img_inactive,is_active = False):
        self.master = master
        self.is_active = is_active
        self.text = text
        self.img_active = img_active
        self.img_inactive = img_inactive
        self.create_button()
    
    def create_button(self):
        self.frame = CTkFrame(self.master,
                              fg_color=colors.book_base if self.is_active else colors.sidebar,
                              bg_color=colors.book_base if self.is_active else colors.sidebar,
                              width=200,
                              height=100,
                              border_width=0)
        
        self.image = CTkImage(Image.open(self.img_active if self.is_active else self.img_inactive),size=(24,24))

        self.image_label = CTkLabel(self.frame,
                                    text="",
                                    image=self.image,
                                    fg_color="transparent",
                                    bg_color="transparent")
        
        self.image_label.grid(padx=10,pady=20,row=0,column=0)
        self.button = CTkButton(self.frame,
                                text=self.text,
                                text_color=colors.sidebar if self.is_active else colors.book_base,
                                fg_color="transparent",
                                bg_color="transparent",
                                width=110,
                                font=("roboto",12,"bold"),
                                anchor="w",
                                hover_color=colors.new_button_color_hover,
                                state="disable" if self.is_active else "enable",
                                command=self.click,
                                cursor = "hand2")
        self.button.grid(padx=5,pady=20,row=0,column=1)

        
        self.triangle_img = CTkImage(Image.open("resources/icons/sidebar_triangle.png"),size=(20,60))
        self.triangle_img_label = CTkLabel(self.frame,
                                           text="",
                                           image=self.triangle_img,
                                           fg_color="transparent",
                                           bg_color="transparent")

        self.triangle_img_label.grid(padx=0,pady=0,row=0,column=2)

        self.apply_hover_effects()
        self.apply_click_functions()
    


    # Hover effects....................
    def apply_hover_effects(self):
        self.frame.bind("<Enter>",self.button_hover)
        self.frame.bind("<Leave>",self.button_unhover)
        self.button.bind("<Enter>",self.button_hover)
        self.button.bind("<Leave>",self.button_unhover)
        self.image_label.bind("<Enter>",self.button_hover)
        self.image_label.bind("<Leave>",self.button_unhover)

    def button_hover(self,event):
        self.frame.configure(fg_color = colors.new_button_color_hover if not self.is_active else colors.book_base)

    def button_unhover(self,event):
        self.frame.configure(fg_color = colors.sidebar if not self.is_active else colors.book_base)
    # / Hover effects...............



    # Click Functions.................
    def apply_click_functions(self):
        # self.frame.bind("<Button-1>",self.click)
        # self.image_label.bind("<Button-1>",self.click)
        pass

    def click(self):
        print(self.text+" pressed ")
        if self.is_active:
            pass
        else:
            self.is_active = True
            self.frame.configure(fg_color = colors.book_base,bg_color = colors.book_base)
            self.button.configure(text_color = colors.new_button_color)
            self.image_label.configure(image=CTkImage(Image.open(self.img_active),size=(24,24)))
    # / Click Functons.................



    # placement methods.......
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady)

    def place(self,x,y):
        self.frame.place(x=x,y=y)

    def grid(self,row,column,padx=0,pady=0):
        self.frame.grid(row=row,column=column,padx=padx,pady=pady)
    # / placement methods.........


if __name__ == "__main__":
    root = CTk(fg_color="#ffffff")
    set_appearance_mode("light")
    root.geometry("300x200")
    sidebar = CTkFrame(root,fg_color=colors.sidebar,corner_radius=0)

    home_btn = SidebarButtons(sidebar,"Home","resources/icons/HomeDark.png","resources/icons/HomeLight.png",True)
    home_btn.pack()

    sidebar.pack(padx=0,pady=0,fill="y",side="left")
    root.mainloop()