from tkinter import *
from customtkinter import *
import pywinstyles
from components import colors
from components import book_icon

if __name__ == "__main__":
    root = CTk(fg_color="#ffffff")
    root.title("Library Management System")
    root.iconbitmap("resources/icons/library icon.ico")

    pywinstyles.change_header_color(root,colors.base_color)


    b1 = book_icon.Book_icon(root,"resources/Books/dr br ambedkar.jpg","Dr B.R. Ambedkar","Br ambedkar",1,12,favourite=True,reserved=False)

    b1.description("It reflects the social struggles he faced as a child and student.\nThrough these incidents, Ambedkar exposes the harsh realities of untouchability in India.\nThe book shows his resolve to fight for equality and justice for all")

    b1.grid(row=0,column=0,padx=10,pady=10)



    b2 = book_icon.Book_icon(root,"resources/Books/Brief History of time.jpg","Brief History of Time","Stephen Hawkings",2,9,favourite=False,reserved=True)

    b2.description("A Brief History of Time by Stephen Hawking explores the mysteries of the universe in simple language.\nIt explains the Big Bang, black holes, space-time, and the nature of time.\nThe book makes complex physics understandable for general readers.\nIt reflects Hawking’s search for a unified theory and humanity’s place in the cosmos.")

    b2.grid(row=0,column=1,padx=10,pady=10)

    b3 = book_icon.Book_icon(root,"resources/Books/home in a hundred places.png","Home in a Hundred Places","Unknown",1,6,favourite=False,reserved=False)
    b3.grid(row=0,column=2,padx=10,pady=10)

    root.mainloop()