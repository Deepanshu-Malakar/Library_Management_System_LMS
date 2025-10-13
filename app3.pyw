from customtkinter import *
from tkinter import *
from pages import Welcome_page
import pywinstyles

set_appearance_mode("light")
if __name__ == "__main__":

    width = 2228
    height = 1480
    factor = 0.5
    root = CTk(fg_color="#7F495D")
    root.geometry(f"{width*factor}x{height*factor}")
    root.resizable(False,False)
    
    root.title("Your Personal Library")
    root.iconbitmap("resources/icons/library icon.ico")
    pywinstyles.change_header_color(root,"#4F2D39")
    pywinstyles.change_border_color(root,"#4F2D39")
    # root.state("zoomed")
    pages_frame = Welcome_page.Welcome_page(root)
    pages_frame.pack()

    root.mainloop()