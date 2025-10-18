from tkinter import *
from customtkinter import *
from components import sidebar_buttons
from PIL import Image

class color:
    def __init__(self):
        self.base_color = "#4153A3"
        self.disable_buttons = "#535769"
        self.fine = "#DF3939"
        self.sidebar = "#292B34"
        self.book_base_old = "#EEE8F2"
        self.book_base = "#ffffff"
        self.new_button_color = "#1A2032"
        self.new_button_color_hover = "#090B12"
        self.book_hover = "#1A2032"
        self.old_hover = "#C0BEC2"

colors = color()
class SideBar:
    def __init__(self,master):
        self.master = master
        self.frame = CTkFrame(master,fg_color=colors.sidebar,width=300,corner_radius=0,bg_color=colors.sidebar)

        self.request_book_btn = sidebar_buttons.SidebarButtons(self.frame,
                                                text="Suggest Book",
                                                img_active="resources/icons/HomeDark.png",
                                                img_inactive="resources/icons/HomeLight.png",
                                                is_active=True)
        self.request_book_btn.grid(row=1,column=0,padx=0,pady=0)

        self.donate_book_btn = sidebar_buttons.SidebarButtons(self.frame,
                                                text="Donate Book",
                                                img_active="resources/icons/FavouritesDark.png",
                                                img_inactive="resources/icons/FavouritesLight.png",
                                                is_active=False)
        self.donate_book_btn.grid(row=2,column=0,padx=0,pady=10)



# placement functions...................
    def pack(self):
        self.frame.pack(padx=0,pady=0,side="left",fill="y")

        self.is_expanded = True
        self.apply_click_functions()
# / placement functions...................

# Click Functions...............
    def apply_click_functions(self):
        self.request_book_btn.button.configure(command = self.request_book_btn_click)
        self.donate_book_btn.button.configure(command = self.donate_book_btn_click)


    def unselect_all(self):
        self.request_book_btn.unselect()
        self.donate_book_btn.unselect()


    def request_book_btn_click(self):
        self.unselect_all()
        self.request_book_btn.click()

    def donate_book_btn_click(self):
        self.unselect_all()
        self.donate_book_btn.click()


# / Click Functions .................



# Expand and collapse functions................
    def collapse(self):
        self.frame.configure(width=0)
        self.request_book_btn.grid_forget()
        self.donate_book_btn.grid_forget()


    def expand(self):
        self.request_book_btn.grid(row=1,column=0,padx=0,pady=0)
        self.donate_book_btn.grid(row=2,column=0,padx=0,pady=10)

# /Expand and collapse functions...............


#........................................................................................................

class Sidebar_control:
    def __init__(self,master:any,sidebar:SideBar,user_name):
        self.master = master
        self.sidebar = sidebar
        self.frame = CTkFrame(self.master,
                              fg_color="transparent",
                              bg_color="transparent",
                              border_color="#ffffff",
                              border_width=0,
                              corner_radius=0)
        
        self.button = CTkButton(self.frame,
                                text="",
                                fg_color="transparent",
                                bg_color="transparent",
                                image=CTkImage(Image.open("resources/icons/sidebar control.png"),size=(24,24)),
                                hover_color= colors.book_base_old,
                                border_width=0,
                                border_color="#ffffff",
                                width=30,
                                corner_radius=0,
                                command=self.click)
        self.button.pack(padx=5,pady=10,side="left")

        self.label = CTkLabel(self.frame,
                              text=f"Hi {user_name}",
                              fg_color="transparent",
                              bg_color="transparent",
                              font=("roboto",14,"bold"),
                              text_color=colors.sidebar,
                            #   image=CTkImage(Image.open("resources/icons/Hii.png"),size=(24,24)),
                              compound="left")
        self.label.pack(padx=5,pady=10,side="left")



    
    # click functions...............
    # def click(self):
    #     if self.sidebar.is_expanded:
    #         self.collapse()
    #         self.sidebar.is_expanded = False
        
    #     else:
    #         self.expand()
    #         self.sidebar.is_expanded = True

    # def semi_collapse(self):
    #     self.sidebar.home_btn.button.configure(text="",width=5)
    #     self.sidebar.favourites_btn.button.configure(text="",width=5)
    #     self.sidebar.history_btn.button.configure(text="",width=5)
    #     self.sidebar.reserved_books_btn.button.configure(text="",width=5)
    #     self.sidebar.study_section_btn.button.configure(text="",width=5)
        
    # def collapse(self):
    #     self.sidebar.frame.configure(width=0)
    #     self.sidebar.home_btn.grid_forget()
    #     self.sidebar.favourites_btn.grid_forget()
    #     self.sidebar.history_btn.grid_forget()
    #     self.sidebar.study_section_btn.grid_forget()
    #     self.sidebar.reserved_books_btn.grid_forget()

    # def expand(self):
    #     self.sidebar.home_btn.grid(row=1,column=0,padx=0,pady=0)
    #     self.sidebar.favourites_btn.grid(row=2,column=0,padx=0,pady=10)
    #     self.sidebar.history_btn.grid(row=3,column=0,padx=0,pady=0)
    #     self.sidebar.study_section_btn.grid(row=4,column=0,padx=0,pady=10)
    #     self.sidebar.reserved_books_btn.grid(row=5,column=0,padx=0,pady=0)
    # / Click functions..............



    # placement methods...........
    def pack(self,padx=0,pady=0,side="left"):
        self.frame.pack(padx=padx,pady=pady,side=side)
    
    def place(self,x,y):
        self.frame.place(x=x,y=y)
    
    def grid(self,row,column,padx=0,pady=0):
        self.frame.grid(row=row,column=column,padx=padx,pady = pady)

    # / placement methods..............
