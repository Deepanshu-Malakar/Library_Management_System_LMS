from tkinter import *
from PIL import Image
from customtkinter import *
import pywinstyles
from components import colors
from components import book_icon
from components import status_bar
from components import search_bar
from components import sidebar_buttons
from components import sidebar
from CTkXYFrame import * 
from components import navbar_butttons
sidebar_color = "#292B34"
scroll_fg_color = "#484D5B"
if __name__ == "__main__":
    root = CTk(fg_color="#ffffff")
    root.geometry('1920x800')
    root.state("zoomed")
    root.title("Your Personal Library")
    root.iconbitmap("resources/icons/library icon.ico")

    pywinstyles.change_header_color(root,colors.base_color)

    upper_frame = CTkFrame(root,
                           fg_color=colors.navbar,
                           bg_color=colors.navbar,
                           width=1920,
                           height=70,
                           border_color="#C6C6C6",
                           border_width=2,
                           corner_radius=0)
    
# Navbar ......................................................
    
    navbar_buttons_frame = CTkFrame(upper_frame,
                                    fg_color="transparent",
                                    bg_color="transparent")
    

    profile = navbar_butttons.NavbarButtons(navbar_buttons_frame,"resources/icons/profile.png")
    profile.pack(side="right",padx=10,pady=0)

    settings = navbar_butttons.NavbarButtons(navbar_buttons_frame,"resources/icons/settings.png")
    settings.pack(side="right",padx=10,pady=0)


    notifications = navbar_butttons.NavbarButtons(navbar_buttons_frame,"resources/icons/notifications.png")
    notifications.pack(side="right",padx=10,pady=0)

    navbar_buttons_frame.pack(side="right",padx=0,pady=5)

# / Navbar................................................................


    upper_frame.pack(padx=0,pady=0,side="top",fill="x")
    # page1 = CTkScrollableFrame(root,fg_color="transparent",bg_color="transparent",width=1600,height=900)

# sidebar ...................................................................

    sidebar_frame = sidebar.SideBar(root) 
    sidebar_control = sidebar.Sidebar_control(upper_frame,sidebar=sidebar_frame)
    sidebar_control.pack(side="left",padx=0,pady=2)

    your_personal_lib_img = CTkImage(Image.open("resources/icons/your personal library logo3.png"),size=(240,60))
    your_personal_lib_label = CTkLabel(upper_frame,text="",image=your_personal_lib_img)
    your_personal_lib_label.pack(side="left",padx=100,pady=2)



# / sidebar .................................................................

    upper_frame2 = CTkFrame(root,fg_color="transparent",bg_color="transparent",width=1920,height=70,border_color="#C6C6C6",border_width=0,corner_radius=0)
    upper_frame2.pack(padx=0,pady=0,side="top",fill="x")

    search_bar_frame = search_bar.SearchBar(upper_frame2)
    search_bar_frame.pack(padx=10,pady=5,side="right")

    page1 = CTkScrollableFrame(root,
                       fg_color="#ffffff",
                       bg_color="#ffffff",
                       width=1920,
                       height=920,
                       scrollbar_button_color="#ffffff")

    b1 = book_icon.Book_icon(page1,"resources/Books/dr br ambedkar.jpg","Dr B.R. Ambedkar","Br ambedkar",1,12,favourite=True,reserved=False)

    b1.description("It reflects the social struggles he faced as a child and student.\nThrough these incidents, Ambedkar exposes the harsh realities of untouchability in India.\nThe book shows his resolve to fight for equality and justice for all")

    b1.grid(row=0,column=0,padx=10,pady=10)



    b2 = book_icon.Book_icon(page1,"resources/Books/Brief History of time.jpg","Brief History of Time","Stephen Hawkings",2,9,favourite=False,reserved=True)

    b2.description("A Brief History of Time by Stephen Hawking explores the mysteries of the universe in simple language.\nIt explains the Big Bang, black holes, space-time, and the nature of time.\nThe book makes complex physics understandable for general readers.\nIt reflects Hawking’s search for a unified theory and humanity’s place in the cosmos.")

    b2.grid(row=0,column=1,padx=10,pady=10)

    b3 = book_icon.Book_icon(page1,"resources/Books/home in a hundred places.png","Home in a Hundred Places","Unknown",1,6,favourite=False,reserved=False)

    b3.description("Home in a Hundred Places is a reflective book that explores the meaning of belonging, identity, and the search for home across diverse landscapes.\nThrough vivid storytelling and personal experiences, the author weaves together journeys of displacement, adaptation, and rootedness.\nIt highlights how home is not just a physical space but an emotional and cultural connection found in many places.")

    b3.grid(row=0,column=2,padx=10,pady=10)

    b4 = book_icon.Book_icon(page1,"resources/Books/abraham silberschatz operating system.jpg",
                             "Operating System Concepts","Abraham Silberschatz",1,6,favourite=False,reserved=False)

    b4.description("Home in a Hundred Places is a reflective book that explores the meaning of belonging, identity, and the search for home across diverse landscapes.\nThrough vivid storytelling and personal experiences, the author weaves together journeys of displacement, adaptation, and rootedness.\nIt highlights how home is not just a physical space but an emotional and cultural connection found in many places.")

    b4.grid(row=0,column=3,padx=10,pady=10)

    b5 = book_icon.Book_icon(page1,"resources/Books/forozon.jpeg",
                             "Computer Networks","Abraham Silberschatz",1,6,favourite=False,reserved=False)

    b5.description("Home in a Hundred Places is a reflective book that explores the meaning of belonging, identity, and the search for home across diverse landscapes.\nThrough vivid storytelling and personal experiences, the author weaves together journeys of displacement, adaptation, and rootedness.\nIt highlights how home is not just a physical space but an emotional and cultural connection found in many places.")

    b5.grid(row=1,column=0,padx=10,pady=10)



    b6 = book_icon.Book_icon(page1,"resources/Books/Jungle Book.jpg",
                             "Jungle Book","Abraham Silberschatz",1,6,favourite=False,reserved=False)

    b6.description("Home in a Hundred Places is a reflective book that explores the meaning of belonging, identity, and the search for home across diverse landscapes.\nThrough vivid storytelling and personal experiences, the author weaves together journeys of displacement, adaptation, and rootedness.\nIt highlights how home is not just a physical space but an emotional and cultural connection found in many places.")

    b6.grid(row=1,column=1,padx=10,pady=10)



    b7 = book_icon.Book_icon(page1,"resources/Books/Life of my Imagination.jpg",
                             "Life of my Imagination","Rishabh Sharda",1,6,favourite=False,reserved=False)

    b7.description("Home in a Hundred Places is a reflective book that explores the meaning of belonging, identity, and the search for home across diverse landscapes.\nThrough vivid storytelling and personal experiences, the author weaves together journeys of displacement, adaptation, and rootedness.\nIt highlights how home is not just a physical space but an emotional and cultural connection found in many places.")

    b7.grid(row=1,column=2,padx=10,pady=10)



    b8 = book_icon.Book_icon(page1,"resources/Books/nirmala.png",
                             "Nirmalar","Munshi Premchand",1,6,favourite=True,reserved=False)

    b8.description("Home in a Hundred Places is a reflective book that explores the meaning of belonging, identity, and the search for home across diverse landscapes.\nThrough vivid storytelling and personal experiences, the author weaves together journeys of displacement, adaptation, and rootedness.\nIt highlights how home is not just a physical space but an emotional and cultural connection found in many places.")

    b8.grid(row=1,column=3,padx=10,pady=10)



    b9 = book_icon.Book_icon(page1,"resources/Books/Theory of everything.jpg",
                             "Theory of Everything","Stephen Hawkings",1,6,favourite=False,reserved=False)

    b9.description("Home in a Hundred Places is a reflective book that explores the meaning of belonging, identity, and the search for home across diverse landscapes.\nThrough vivid storytelling and personal experiences, the author weaves together journeys of displacement, adaptation, and rootedness.\nIt highlights how home is not just a physical space but an emotional and cultural connection found in many places.")

    b9.grid(row=2,column=0,padx=10,pady=10)



    b10 = book_icon.Book_icon(page1,"resources/Books/the invisible man.jpg",
                             "The invisible Man","H.G. Wells",1,6,favourite=False,reserved=False)

    b10.description("Home in a Hundred Places is a reflective book that explores the meaning of belonging, identity, and the search for home across diverse landscapes.\nThrough vivid storytelling and personal experiences, the author weaves together journeys of displacement, adaptation, and rootedness.\nIt highlights how home is not just a physical space but an emotional and cultural connection found in many places.")

    b10.grid(row=2,column=1,padx=10,pady=10)



    b11 = book_icon.Book_icon(page1,"resources/Books/the canterville ghost.jpg",
                             "the Canterville Ghost","Oliver",1,6,favourite=False,reserved=False)

    b11.description("Home in a Hundred Places is a reflective book that explores the meaning of belonging, identity, and the search for home across diverse landscapes.\nThrough vivid storytelling and personal experiences, the author weaves together journeys of displacement, adaptation, and rootedness.\nIt highlights how home is not just a physical space but an emotional and cultural connection found in many places.")

    b11.grid(row=2,column=2,padx=10,pady=10)


    b12 = book_icon.Book_icon(page1,logo="resources/Books/harry potter1.jpg",
                   book_name="Harry Potter and the Philosopher's Stone",
                   author="J.K. Rowlings",
                   edition=1,
                   copies_available=12,
                   favourite=False,
                   reserved=False)
    b12.grid(row=2,column=3,padx=10,pady=10)

    page1.pack(padx=0,pady=0)

    status = status_bar.StatusBar(root,username="Deepanshu",reserved_books=1,issued_books=1)
    status.place(x=0,y=755)

    # design_Label = CTkLabel(root,fg_color="#1a2032",bg_color="#1a2032",width=200,height=5)
    # pywinstyles.set_opacity(design_Label,0.8)
    # design_Label.place(x=0,y=781)



    root.mainloop()