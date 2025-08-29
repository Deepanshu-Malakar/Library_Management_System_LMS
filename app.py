from tkinter import *
from customtkinter import *
import pywinstyles
from components import colors
from components import book_icon
from components import status_bar
from components import search_bar
from components import sidebar_buttons
from CTkXYFrame import * 

sidebar_color = "#292B34"
scroll_fg_color = "#484D5B"
if __name__ == "__main__":
    root = CTk(fg_color="#ffffff")
    root.geometry('1920x800')
    root.title("Library Management System")
    root.iconbitmap("resources/icons/library icon.ico")

    pywinstyles.change_header_color(root,colors.base_color)

    upper_frame = CTkFrame(root,fg_color="transparent",bg_color="transparent",width=1920,height=70,border_color="#C6C6C6",border_width=2,corner_radius=0)
    upper_frame.pack(padx=0,pady=0,side="top")

    # page1 = CTkScrollableFrame(root,fg_color="transparent",bg_color="transparent",width=1600,height=900)

# sidebar ...................................................................
    sidebar = CTkFrame(root,fg_color=sidebar_color,width=300,corner_radius=0)

    none_btn = CTkFrame(sidebar,fg_color="transparent",bg_color="transparent",height=60)
    # none_btn.grid(row=0,column=0,padx=0,pady=0)

    home_btn = sidebar_buttons.SidebarButtons(sidebar,
                                              text="Home",
                                              img_active="resources/icons/HomeDark.png",
                                              img_inactive="resources/icons/HomeLight.png",
                                              is_active=True)
    home_btn.grid(row=1,column=0,padx=0,pady=0)

    favourites_btn = sidebar_buttons.SidebarButtons(sidebar,
                                              text="Favourites",
                                              img_active="resources/icons/FavouritesDark.png",
                                              img_inactive="resources/icons/FavouritesLight.png",
                                              is_active=False)
    favourites_btn.grid(row=2,column=0,padx=0,pady=10)


    history_btn = sidebar_buttons.SidebarButtons(sidebar,
                                              text="History",
                                              img_active="resources/icons/HistoryDark.png",
                                              img_inactive="resources/icons/HistoryLight.png",
                                              is_active=False)
    history_btn.grid(row=3,column=0,padx=0,pady=10)


    study_section_btn = sidebar_buttons.SidebarButtons(sidebar,
                                              text="Study Section",
                                              img_active="resources/icons/StudyDark.png",
                                              img_inactive="resources/icons/StudyLight.png",
                                              is_active=False)
    study_section_btn.grid(row=4,column=0,padx=0,pady=10)



    reserved_books_btn = sidebar_buttons.SidebarButtons(sidebar,
                                              text="Reserved Books",
                                              img_active="resources/icons/ReservedDark.png",
                                              img_inactive="resources/icons/ReservedLight.png",
                                              is_active=False)
    reserved_books_btn.grid(row=5,column=0,padx=0,pady=10)


    sidebar.pack(padx=0,pady=0,side="left",fill="y")

# / sidebar .................................................................

    upper_frame2 = CTkFrame(root,fg_color="transparent",bg_color="transparent",width=1920,height=70,border_color="#C6C6C6",border_width=0,corner_radius=0)
    upper_frame2.pack(padx=0,pady=0,side="top",fill="x")

    search_bar_frame = search_bar.SearchBar(upper_frame2)
    search_bar_frame.pack(padx=10,pady=5,side="right")

    page1 = CTkXYFrame(root,
                       fg_color="#ffffff",
                       bg_color="#ffffff",
                       width=1920,
                       height=920,
                       scrollbar_width=12,
                       scrollbar_fg_color=scroll_fg_color,
                       scrollbar_button_color="#ffffff")
    page1.vsb.configure(fg_color = "#ffffff")
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
    status.place(x=0,y=743)

    design_Label = CTkLabel(root,fg_color="#1a2032",bg_color="#1a2032",width=305,height=5)
    pywinstyles.set_opacity(design_Label,0.8)
    design_Label.place(x=0,y=781)



    root.mainloop()