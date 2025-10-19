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
        self.button_width = 130

        self.issue_books_btn = sidebar_buttons.SidebarButtons(self.frame,
                                                text="Issue Books",
                                                img_active="resources/icons/issue book dark.png",
                                                img_inactive="resources/icons/issue book light.png",
                                                is_active=True)
        self.issue_books_btn.grid(row=1,column=0,padx=0,pady=0)
        self.issue_books_btn.button.configure(width=self.button_width)

        self.return_books_btn = sidebar_buttons.SidebarButtons(self.frame,
                                                text="Return Books",
                                                img_active="resources/icons/return book dark.png",
                                                img_inactive="resources/icons/return book light.png",
                                                is_active=False)
        self.return_books_btn.grid(row=2,column=0,padx=0,pady=10)
        self.return_books_btn.button.configure(width=self.button_width)


        self.reserve_books_btn = sidebar_buttons.SidebarButtons(self.frame,
                                                text="Reserve Books",
                                                img_active="resources/icons/ReservedDark.png",
                                                img_inactive="resources/icons/ReservedLight.png",
                                                is_active=False)
        self.reserve_books_btn.grid(row=3,column=0,padx=0,pady=0)
        self.reserve_books_btn.button.configure(width=self.button_width)


        self.due_books_btn = sidebar_buttons.SidebarButtons(self.frame,
                                                text="Due Books",
                                                img_active="resources/icons/due books dark.png",
                                                img_inactive="resources/icons/due books light.png",
                                                is_active=False)
        self.due_books_btn.grid(row=4,column=0,padx=0,pady=10)
        self.due_books_btn.button.configure(width=self.button_width)



        self.requested_books_btn = sidebar_buttons.SidebarButtons(self.frame,
                                                text="Requested Books",
                                                img_active="resources/icons/request book dark.png",
                                                img_inactive="resources/icons/request book light.png",
                                                is_active=False)
        self.requested_books_btn.grid(row=5,column=0,padx=0,pady=0)
        self.requested_books_btn.button.configure(width=self.button_width)

        self.add_books_btn = sidebar_buttons.SidebarButtons(self.frame,
                                                text="Add Books",
                                                img_active="resources/icons/add book dark.png",
                                                img_inactive="resources/icons/add book light.png",
                                                is_active=False)
        self.add_books_btn.grid(row=6,column=0,padx=0,pady=10)
        self.add_books_btn.button.configure(width=self.button_width)




# placement functions...................
    def pack(self):
        self.frame.pack(padx=0,pady=0,side="left",fill="y")

        self.is_expanded = True
        self.apply_click_functions()
# / placement functions...................

# Click Functions...............
    def apply_click_functions(self):
        self.issue_books_btn.button.configure(command = self.issue_books_btn_click)
        self.return_books_btn.button.configure(command = self.return_books_btn_click)
        self.reserve_books_btn.button.configure(command = self.reserve_books_btn_click)
        self.requested_books_btn.button.configure(command = self.requested_books_btn_click)
        self.due_books_btn.button.configure(command = self.due_books_btn_click)
        self.add_books_btn.button.configure(command = self.add_books_btn_click)

    def unselect_all(self):
        self.issue_books_btn.unselect()
        self.return_books_btn.unselect()
        self.reserve_books_btn.unselect()
        self.requested_books_btn.unselect()
        self.due_books_btn.unselect()
        self.add_books_btn.unselect()

    def issue_books_btn_click(self):
        self.unselect_all()
        self.issue_books_btn.click()

    def return_books_btn_click(self):
        self.unselect_all()
        self.return_books_btn.click()

    def reserve_books_btn_click(self):
        self.unselect_all()
        self.reserve_books_btn.click()

    def requested_books_btn_click(self):
        self.unselect_all()
        self.requested_books_btn.click()

    def due_books_btn_click(self):
        self.unselect_all()
        self.due_books_btn.click()

    def add_books_btn_click(self):
        self.unselect_all()
        self.add_books_btn.click()
# / Click Functions .................



# Expand and collapse functions................
    def collapse(self):
        self.frame.configure(width=0)
        self.issue_books_btn.grid_forget()
        self.return_books_btn.grid_forget()
        self.reserve_books_btn.grid_forget()
        self.requested_books_btn.grid_forget()
        self.due_books_btn.grid_forget()
        self.add_books_btn.grid_forget()

    def expand(self):
        self.issue_books_btn.grid(row=1,column=0,padx=0,pady=0)
        self.return_books_btn.grid(row=2,column=0,padx=0,pady=10)
        self.reserve_books_btn.grid(row=3,column=0,padx=0,pady=0)
        self.requested_books_btn.grid(row=5,column=0,padx=0,pady=10)
        self.due_books_btn.grid(row=4,column=0,padx=0,pady=0)
        self.add_books_btn.grid(row=6,column=0,padx=0,pady=0)
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
