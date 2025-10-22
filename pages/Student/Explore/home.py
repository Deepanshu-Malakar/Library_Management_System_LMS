from tkinter import *
from customtkinter import *
from PIL import Image
from backend import mysql_tables
from backend import DrawBooks
from components import book_icon
from components import search_bar
from components import category_folders

class HomePage:
    def __init__(self,master):
        self.master = master
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              bg_color="#ffffff")
        
        # upper frame..............................
        self.upper_frame2 = CTkFrame(self.frame,
                                fg_color="transparent",
                                bg_color="transparent",
                                width=1920,
                                height=70,
                                border_color="#C6C6C6",
                                border_width=0,
                                corner_radius=0)
        
        self.upper_frame2.pack(padx=0,pady=0,side="top",fill="x")

        self.search_bar_frame = search_bar.SearchBar(self.upper_frame2)
        self.search_bar_frame.pack(padx=10,pady=5,side="right")

    # Folder bar.................................................
        self.folder_bar = category_folders.FolderBar(self.upper_frame2)
        self.folder_bar.pack(side="left",padx=10)


        All_category_folder = self.folder_bar.add_category("All",True)
        Story_books_category_folder = self.folder_bar.add_category("Story Books",False)
        Philosopy_books_category_folder = self.folder_bar.add_category("Philosopy",False)
        Science_category_folder = self.folder_bar.add_category("Science",False)
        computer_science_category_folder = self.folder_bar.add_category("Computer Science",False)


    # / Folder bar.....................................................
        # / upper frame.............................


        # books display frame......................
        self.books_frame = CTkScrollableFrame(self.frame,
                                                fg_color="#ffffff",
                                                scrollbar_button_color="#ffffff")
        DrawBooks.draw_books(self.books_frame,self.get_all_books())

        self.books_frame.pack(fill="both",expand=True,padx=0,pady=0)
        self.apply_category_click_functions()
        # /books display frame...........................


# Showing Book Functions..........................
        
    def get_all_books(self):
        books = mysql_tables.get_book_by_title()
        # print(books)
        title_list = []
        author_list = []
        edition_list = []
        description_list = []
        cover_img_list = []
        for book in books:
            title_list.append(book[0])
            author_list.append(book[1])
            edition_list.append(book[2])
            description_list.append(book[7])
            cover_img_list.append(book[6])
        books = []
        for i in range (len(title_list)):
            title = title_list[i]
            copies_available = mysql_tables.get_copies_of_book(title)
            book = book_icon.Book_icon(self.books_frame,
                                       logo=cover_img_list[i],
                                       book_name=title_list[i],
                                       author=author_list[i],
                                       edition=edition_list[i],
                                       copies_available=copies_available,
                                       favourite=False,
                                       reserved=False)
            book.description(description_list[i])
            books.append(book)
        # print(books)
        return books
# /Showing Book Functions..........................




# Search Book by Category Functions..........................
    def apply_category_click_functions(self):
        for category in self.folder_bar.categories:
            category.button.bind("<Button-1>",lambda e,cat=category.text: self.apply_category_filter(cat))

    def apply_category_filter(self,category):
        for widget in self.books_frame.winfo_children():
            widget.destroy()
        if category=="All":
            books = self.get_all_books()
        else:
            books = self.get_books_by_category(category)
        DrawBooks.draw_books(self.books_frame,books)

    def get_books_by_category(self,category):
        mysql_tables.cur.execute(f"""SELECT distinct title,author,edition,category,status,available,cover_img,description from books where category = '{category}';""")
        books_data = mysql_tables.cur.fetchall()
        title_list = []
        author_list = []
        edition_list = []
        description_list = []
        cover_img_list = []
        for book in books_data:
            title_list.append(book[0])
            author_list.append(book[1])
            edition_list.append(book[2])
            description_list.append(book[7])
            cover_img_list.append(book[6])
        books = []
        for i in range (len(title_list)):
            title = title_list[i]
            copies_available = mysql_tables.get_copies_of_book(title)
            book = book_icon.Book_icon(self.books_frame,
                                       logo=cover_img_list[i],
                                       book_name=title_list[i],
                                       author=author_list[i],
                                       edition=edition_list[i],
                                       copies_available=copies_available,
                                       favourite=False,
                                       reserved=False)
            book.description(description_list[i])
            books.append(book)
        return books
# / Search Book by Category Functions......................



    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = "both",expand = True)
    def pack_forget(self):
        self.frame.pack_forget()