from tkinter import *
from customtkinter import *
from PIL import Image
import pywinstyles

if __name__ == "__main__":
    import colors
else:
    from components import colors

class SearchBar:
    def __init__(self,master:any):
        self.master = master
        self.frame = CTkFrame(master,
                              fg_color="transparent",
                              border_width=2,
                              border_color=colors.book_base)
        
        self.search_options_img = CTkImage(Image.open("resources/icons/search options.png"),size=(32,32))
        self.search_options_btn = CTkButton(self.frame,
                                             text="",
                                             image=self.search_options_img,
                                             fg_color="transparent",
                                             bg_color="transparent",
                                             hover_color=colors.book_base,
                                             width=20,
                                             command=self.options_btn_click)
        self.search_options_btn.grid(row=0,column=0,padx=5,pady=5)

        self.entry = CTkEntry(self.frame,
                              placeholder_text="Search Book by Name or Author",
                              border_color="#ffffff",
                              fg_color="transparent",
                              bg_color="transparent",
                              width=200)
        self.entry.grid(row=0,column=1,padx=0,pady=5)

        self.search_btn_img = CTkImage(Image.open("resources/icons/search icon.png"),size=(32,32))
        self.search_btn = CTkButton(self.frame,
                                             text="",
                                             image=self.search_btn_img,
                                             fg_color="transparent",
                                             bg_color="transparent",
                                             hover_color=colors.book_base,
                                             width=20,
                                             command=self.search_btn_click)
        self.search_btn.grid(row=0,column=2,padx=5,pady=5)


# placement methods...........
    def pack(self,padx=0,pady=0,side="top"):
        self.frame.pack(padx=padx,pady=pady,side=side)
    def place(self,x,y):
        self.frame.place(x=x,y=y)
    def grid(self,row,column,padx=0,pady=0,rowspan=1,columnspan=1):
        self.frame.grid(row=row,column=column,padx=padx,pady=pady,rowspan=rowspan,columnspan=columnspan)
# / placement methods..............


# styling methods...........
    def set_transparency(self,opacity:1):
        pywinstyles.set_opacity(self.frame,opacity)
# / styling methods..........


# click functions.............
    def search_btn_click(self):
        pass
    def options_btn_click(self):
        pass
# / click functions.............

if __name__ == "__main__":
    set_appearance_mode("light")
    root = CTk(fg_color="#ffffff")
    root.geometry("200x200")
    searchbar = SearchBar(root)
    searchbar.place(x=10,y=10)
    root.mainloop()