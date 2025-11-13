from customtkinter import *
print("Loading 10%")
from tkinter import *
print("Loading 20%")
from pages import Welcome_page
print("Loading 30%")
import pywinstyles
print("Loading 40%")
from backend import mysql_tables
print("Loading 50%")
from backend import issue_books_logic
print("Loading 60%")


mysql_tables.create_tables()
print("Loading 70%")
issue_books_logic.mark_as_due_book()
print("Loading 80%")
set_appearance_mode("light")
if __name__ == "__main__":
    # mysql_tables.create_tables()

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