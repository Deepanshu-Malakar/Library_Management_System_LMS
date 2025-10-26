from tkinter import *
from customtkinter import *
from PIL import Image
import pywinstyles

from components import sidebar_control_button
from CTkXYFrame import * 
from components import navbar_butttons
from components import navbar_tabs
from components import status_bar

from pages.Faculty import Explore_page
from pages.Faculty import Book_center_page
from pages.Faculty import Help_and_support_page

class colors:
    def __init__(self):
        self.base_color = "#4153A3"
        self.disable_buttons = "#535769"
        self.fine = "#DF3939"
        self.sidebar = "#292B34"
        self.book_base_old = "#EEE8F2"
        self.navbar = "#FFFFFF"
        self.navbar_hover = "#ECF3FE"

        # self.book_base = "#EEE8F2"
        self.book_base = "#ffffff"
        self.new_button_color = "#1A2032"
        self.new_button_color_hover = "#090B12"
        self.book_hover = "#1A2032"
        self.old_hover = "#C0BEC2"


        self.folder_bg = "#C7CEE9"
        self.folder_filled = "#5165AA"



class Faculty_Dashboard:
    def __init__(self,master:CTk,faculty_record):
        self.current_tab = "Explore"
        self.master = master
        self.master.state("zoomed")
        pywinstyles.change_header_color(self.master,colors().base_color)
        
        self.faculty_record = faculty_record
        self.username = faculty_record["faculty id"]
        self.frame = CTkFrame(self.master,
                              corner_radius=0)
        self.create_dashboard()
        self.apply_popup_effects()
        self.apply_click_functions()
        

    def create_dashboard(self):
        self.upper_frame = CTkFrame(self.frame,
                            fg_color=colors().navbar,
                            bg_color=colors().navbar,
                            width=1920,
                            height=70,
                            #    border_color="#C6C6C6",
                            border_color=colors().book_base_old, 
                            border_width=2,
                            corner_radius=0)
        self.upper_frame.pack(padx=0,pady=0,side="top",fill="x")   
        self.create_navbar()
        self.create_status_bar()
        self.page_frame = Explore_page.Page(self.frame,self.sidebar_control,self.faculty_record)
        self.page_frame.pack()
            
    def create_navbar(self):
        # profile settings and notifications...............
        self.navbar_buttons_frame = CTkFrame(self.upper_frame,
                                        fg_color="transparent",
                                        bg_color="transparent")
        

        self.profile = navbar_butttons.NavbarButtons(self.navbar_buttons_frame,"resources/icons/profile.png")
        self.profile.pack(side="right",padx=10,pady=0)

        self.settings = navbar_butttons.NavbarButtons(self.navbar_buttons_frame,"resources/icons/settings.png")
        self.settings.pack(side="right",padx=10,pady=0)


        self.notifications = navbar_butttons.NavbarButtons(self.navbar_buttons_frame,"resources/icons/notifications.png")
        self.notifications.pack(side="right",padx=10,pady=0)

        self.navbar_buttons_frame.pack(side="right",padx=0,pady=5)
        # /profile settings and notifications..............



    # Explore, book center, doubt section and help tabs....................
        self.navebar_tabs_frame = CTkFrame(self.upper_frame,
                                fg_color="transparent",
                                bg_color="transparent",
                                height=20)
        
        self.explore_tab = navbar_tabs.NavbarTabs(self.navebar_tabs_frame,"Explore",is_active=True)
        self.explore_tab.grid(row=0,column=0,padx=0,pady=0)

        self.Book_center_tab = navbar_tabs.NavbarTabs(self.navebar_tabs_frame,"Book Center",is_active=False)   # use donate book in book center
        self.Book_center_tab.grid(row=0,column=1,padx=0,pady=0)

        self.Help_tab = navbar_tabs.NavbarTabs(self.navebar_tabs_frame,"Help & Support",is_active=False)
        self.Help_tab.grid(row=0,column=3,padx=0,pady=0)


        self.navebar_tabs_frame.pack(side="right",padx=20,pady=0)

    # / Explore, book center, doubt section and help tabs....................


    # Hi username , library logo and sidebar controller
        # sidebar_frame = sidebar.SideBar(self.frame) 
        self.sidebar_control = sidebar_control_button.Sidebar_control(self.upper_frame,f"Greetings {self.username} Sir")
        self.sidebar_control.pack(side="left",padx=0,pady=2)

        self.your_personal_lib_img = CTkImage(Image.open("resources/icons/your personal library logo3.png")
                                              ,size=(240*0.9,60*0.9))
        
        self.your_personal_lib_label = CTkLabel(self.upper_frame,
                                                text="",
                                                image=self.your_personal_lib_img)
        
        self.your_personal_lib_label.pack(side="left",padx=100,pady=2)

    def create_status_bar(self):
        self.status_bar = status_bar.StatusBar(self.frame,self.username,0,0,0,0)
        self.status_bar.pack()

# profile notification and settings popup..............
    def apply_popup_effects(self):
        self.notifications.frame.bind("<Button-1>",self.notifications_click)
        self.notifications.button.bind("<Button-1>",self.notifications_click)
        
        self.profile.frame.bind("<Button-1>",self.profile_click)
        self.profile.button.bind("<Button-1>",self.profile_click)

        self.settings.frame.bind("<Button-1>",self.settings_click)
        self.settings.button.bind("<Button-1>",self.settings_click)

    def notifications_click(self,e):
        self.notifications.click(master=self.master,text="Notifications")
    def profile_click(self,e):
        self.profile.click(master=self.master,text="Your profile")
    def settings_click(self,e):
        self.settings.click(master=self.master,text="Settings")

# /profile notification and settings popup..............

#tabs switch functions.....................
    def apply_click_functions(self):
        self.explore_tab.frame.bind("<Button-1>",self.open_explore_tab)
        self.explore_tab.button.bind("<Button-1>",self.open_explore_tab)

        self.Book_center_tab.frame.bind("<Button-1>",self.open_bookcenter_tab)
        self.Book_center_tab.button.bind("<Button-1>",self.open_bookcenter_tab)

        self.Help_tab.frame.bind("<Button-1>",self.open_help_tab)
        self.Help_tab.button.bind("<Button-1>",self.open_help_tab)

    def unselect_all_tabs(self):
        self.explore_tab.unselect()
        self.Book_center_tab.unselect()
        self.Help_tab.unselect()


# / tabs switch functions...................



# tabs opening functions.................
    def open_explore_tab(self,e):
        self.unselect_all_tabs()
        self.explore_tab.click()
        self.page_frame.pack_forget()
        self.page_frame = Explore_page.Page(self.frame,self.sidebar_control,self.faculty_record)
        self.page_frame.pack()

    def open_bookcenter_tab(self,e):
        self.unselect_all_tabs()
        self.Book_center_tab.click()
        self.page_frame.pack_forget()
        self.page_frame = Book_center_page.Page(self.frame,self.sidebar_control,self.faculty_record)
        self.page_frame.pack()

    def open_help_tab(self,e):
        self.unselect_all_tabs()
        self.Help_tab.click()
        self.page_frame.pack_forget()        
        self.page_frame = Help_and_support_page.Page(self.frame,self.sidebar_control,self.faculty_record)
        self.page_frame.pack()

# / tabs opening functions..................
    #placement methods..................................................
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = 'both',expand = True)
    # / placement methods...............................................
    