from tkinter import *
from customtkinter import *
from components import book_icon

if __name__ == "__main__":
    root = CTk(fg_color="#ffffff")
    b1 = book_icon.Book_icon(root,"resources/Books/dr br ambedkar.jpg","Dr B.R. Ambedkar","Br ambedkar",1,12,favourite=True,reserved=False)
    b1.grid(row=0,column=0,padx=10,pady=10)

    b2 = book_icon.Book_icon(root,"resources/Books/Brief History of time.jpg","Brief History of Time","Stephen Hawkings",2,9,favourite=False,reserved=True)
    b2.grid(row=0,column=1,padx=10,pady=10)

    b3 = book_icon.Book_icon(root,"resources/Books/home in a hundred places.png","Home in a Hundred Places","Unknown",1,6,favourite=False,reserved=False)
    b3.grid(row=0,column=2,padx=10,pady=10)

    root.mainloop()