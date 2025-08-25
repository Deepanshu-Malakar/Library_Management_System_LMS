from tkinter import *
from customtkinter import *
import components.book_icon as book_icon

if __name__ == "__main__":
    root = CTk()
    b1 = book_icon.Book_icon(root,"resources/Books/dr br ambedkar.jpg","Dr B.R. Ambedkar","Br ambedkar",1,12,favourite=True,reserved=False)
    b1.pack(padx=10,pady=10)
    root.mainloop()