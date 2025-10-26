from tkinter import *
from customtkinter import *
from PIL import Image
import pywinstyles
from backend import mysql_tables
from backend import favourites_logic
from backend import DrawBooks
from components import book_icon
from components import search_bar
from components import category_folders
from components import colors

class FavouritesPage:
    def __init__(self,master,faculty_record):
        self.faculty_record = faculty_record
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
        self.search_bar_frame.search_btn.bind("<Button-1>",lambda e: self.apply_search_filter(self.search_bar_frame.entry.get()))
        self.search_bar_frame.entry.bind("<Return>",lambda e: self.apply_search_filter(self.search_bar_frame.entry.get()))
        self.search_bar_frame.search_options_btn.bind("<Button-1>",lambda e: self.master.focus())

    # Folder bar.................................................
        self.folder_bar = category_folders.FolderBar(self.upper_frame2)
        self.folder_bar.pack(side="left",padx=10)
        self.folder_bar.add_btn.button.configure(command=self.open_add_category_window)


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
        books = favourites_logic.get_all_favourites(self.faculty_record["faculty id"])
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
            description_list.append(book[5])
            cover_img_list.append(book[4])
        books = []
        for i in range (len(title_list)):
            title = title_list[i]
            author = author_list[i]
            edition = edition_list[i]
            copies_available = mysql_tables.get_copies_of_book(title,author,edition)
            book = book_icon.Book_icon(self.books_frame,
                                       logo=cover_img_list[i],
                                       book_name=title_list[i],
                                       author=author_list[i],
                                       edition=edition_list[i],
                                       copies_available=copies_available,
                                       favourite=False,
                                       reserved=False,
                                       user=self.faculty_record["faculty id"])
            book.description(description_list[i])
            books.append(book)
        # print(books)
        return books
# /Showing Book Functions..........................



# Search Book by Category Functions..........................
    def open_add_category_window(self):
        self.new_window = CTkToplevel(self.master)
        self.new_window.title("Add New Category")
        pywinstyles.change_header_color(self.new_window,colors.base_color)
        self.new_window.geometry(f"300x100+700+100")
        # self.new_window.geometry("400x200")
        self.new_window.resizable(False,False)
        self.new_window.grab_set()
        self.new_window.focus_set()

        # self.category_label = CTkLabel(self.new_window,
        #                       text="Category Name:",
        #                       font=("roboto",12,"bold"))
        #                     #   text_color=colors.base_color)
        # self.category_label.pack(padx=20,pady=5)
        self.option_menu = CTkComboBox(self.new_window,
                                         values=["Story Books","Philosopy","Science","Computer Science","History","Biography","Comics","Fantasy","Mystery","Romance","Horror","Mechanical Engineering","Electrical Engineering"],
                                         width=200,
                                         height=30,
                                         border_width=0,
                                        #  fg_color=colors.book_base_old,
                                         button_color=colors.base_color,
                                        #  button_hover_color=colors.folder_bg,
                                        #  text_color=colors.base_color,
                                         dropdown_fg_color=colors.book_base_old,
                                        #  dropdown_text_color=colors.base_color,
                                         dropdown_hover_color=colors.folder_bg)
        self.option_menu.pack(padx=20,pady=5)

        self.add_category_btn = CTkButton(self.new_window,
                                          text="Add Category",
                                          width=200,
                                          height=30,
                                          fg_color=colors.base_color,
                                          hover_color=colors.new_button_color,
                                          command=lambda: [self.apply_category_filter(self.option_menu.get()),self.new_window.destroy(),self.folder_bar.unclick_all_categories()])
        self.add_category_btn.pack(padx=20,pady=10)
        

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
        fav_books = favourites_logic.get_all_favourites(self.faculty_record["faculty id"])
        books_data = []
        for fav_book in fav_books:
            if fav_book[3] == category:
                books_data.append(fav_book)

        title_list = []
        author_list = []
        edition_list = []
        description_list = []
        cover_img_list = []
        for book in books_data:
            title_list.append(book[0])
            author_list.append(book[1])
            edition_list.append(book[2])
            description_list.append(book[5])
            cover_img_list.append(book[4])
        books = []
        for i in range (len(title_list)):
            title = title_list[i]
            copies_available = mysql_tables.get_copies_of_book(title,author_list[i],edition_list[i])
            book = book_icon.Book_icon(self.books_frame,
                                       logo=cover_img_list[i],
                                       book_name=title_list[i],
                                       author=author_list[i],
                                       edition=edition_list[i],
                                       copies_available=copies_available,
                                       favourite=False,
                                       reserved=False,
                                       user=self.faculty_record["faculty id"])
            book.description(description_list[i])
            books.append(book)
        return books
# / Search Book by Category Functions......................


# Search Book by Title or author Functions..........................
    def apply_search_filter(self,search_text):
        for widget in self.books_frame.winfo_children():
            widget.destroy()
        books = self.get_books_by_title_or_author(search_text)
        DrawBooks.draw_books(self.books_frame,books)
    
    def get_books_by_title_or_author(self,search_text):
        user_id = self.faculty_record["faculty id"]
        mysql_tables.cur.execute(f"select title,author,edition from favourites where user_id = '{user_id}' and (title like '%{search_text}%' or author like '%{search_text}%')")
        books = mysql_tables.cur.fetchall()

        books_data = []
        for book in books:
            mysql_tables.cur.execute("SELECT distinct title,author,edition,category,cover_img,description from books where title = %s and author = %s and edition = %s",(book[0],book[1],book[2]))
            books_data.append(mysql_tables.cur.fetchall()[0])
        # books_data = mysql_tables.cur.fetchall()
        title_list = []
        author_list = []
        edition_list = []
        description_list = []
        cover_img_list = []
        for book in books_data:
            title_list.append(book[0])
            author_list.append(book[1])
            edition_list.append(book[2])
            description_list.append(book[5])
            cover_img_list.append(book[4])
        books = []
        for i in range (len(title_list)):
            title = title_list[i]
            copies_available = mysql_tables.get_copies_of_book(title,author_list[i],edition_list[i])
            book = book_icon.Book_icon(self.books_frame,
                                       logo=cover_img_list[i],
                                       book_name=title_list[i],
                                       author=author_list[i],
                                       edition=edition_list[i],
                                       copies_available=copies_available,
                                       favourite=False,
                                       reserved=False,
                                       user=self.faculty_record["faculty id"])
            book.description(description_list[i])
            books.append(book)
        return books
    

# / Search Book by Title or author Functions.........................
    
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = "both",expand = True)
    def pack_forget(self):
        self.frame.pack_forget()