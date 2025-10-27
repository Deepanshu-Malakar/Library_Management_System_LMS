from tkinter import *
from customtkinter import *
from PIL import Image
import pywinstyles

from components import sidebar_control_button
from CTkXYFrame import * 
from components import navbar_butttons
from components import navbar_tabs
from components import status_bar
from components import user_info_card
from components import notification_bar

from pages.Librarian import book_management_page
from pages.Librarian import user_management_page
from pages.Librarian import reports_page
from pages.Librarian import Help_and_support_page

from backend import status_bar_logic




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


class Librarian_Dashboard:
    def __init__(self,master:CTk,username,user_id):
        self.current_tab = "Book Management"
        self.master = master
        self.master.state("zoomed")
        pywinstyles.change_header_color(self.master,colors().base_color)
        
        self.username = username
        self.user_id = user_id
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
        self.page_frame = book_management_page.Page(self.frame,self.sidebar_control)
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
        
        self.book_management_tab = navbar_tabs.NavbarTabs(self.navebar_tabs_frame,"Books",is_active=True)
        self.book_management_tab.grid(row=0,column=0,padx=0,pady=0)

        self.user_management_tab = navbar_tabs.NavbarTabs(self.navebar_tabs_frame,"User Management",is_active=False)   # use donate book in book center
        self.user_management_tab.grid(row=0,column=1,padx=0,pady=0)

        self.Help_tab = navbar_tabs.NavbarTabs(self.navebar_tabs_frame,"Help & Support",is_active=False)
        self.Help_tab.grid(row=0,column=3,padx=0,pady=0)

        self.reports_tab = navbar_tabs.NavbarTabs(self.navebar_tabs_frame,"Reports",is_active=False)
        self.reports_tab.grid(row=0,column=2,padx=0,pady=0)

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
        reserved_books = status_bar_logic.total_reserved_books()
        issued_books = status_bar_logic.total_issued_books()
        due_books = status_bar_logic.total_due_books()
        fine = status_bar_logic.total_pending_fine()
        self.status_bar = status_bar.StatusBar(self.frame,self.username,reserved_books,issued_books,fine,due_books)
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
        self.notification_bar = notification_bar.Notification(self.notifications.popup,self.user_id)

    def profile_click(self,e):
        self.profile.click(master=self.master,text="Your profile")
        self.profile.popup.geometry(f"270x270+{self.master.winfo_width()-380}+100")
        user_card = user_info_card.UserCard(self.profile.popup,self.user_id)
        user_card.grid(row=0,column=0,padx=0,pady=0)
    def settings_click(self,e):
        self.settings.click(master=self.master,text="Settings")

# /profile notification and settings popup..............



#tabs switch functions.....................
    def apply_click_functions(self):
        self.book_management_tab.frame.bind("<Button-1>",self.open_book_management_tab)
        self.book_management_tab.button.bind("<Button-1>",self.open_book_management_tab)

        self.user_management_tab.frame.bind("<Button-1>",self.open_user_management_tab)
        self.user_management_tab.button.bind("<Button-1>",self.open_user_management_tab)

        self.reports_tab.frame.bind("<Button-1>",self.open_reports_tab)
        self.reports_tab.button.bind("<Button-1>",self.open_reports_tab)

        self.Help_tab.frame.bind("<Button-1>",self.open_help_tab)
        self.Help_tab.button.bind("<Button-1>",self.open_help_tab)

    def unselect_all_tabs(self):
        self.book_management_tab.unselect()
        self.user_management_tab.unselect()
        self.reports_tab.unselect()
        self.Help_tab.unselect()


# / tabs switch functions...................



# tabs opening functions.................
    def open_book_management_tab(self,e):
        self.unselect_all_tabs()
        self.book_management_tab.click()
        self.page_frame.pack_forget()
        self.page_frame = book_management_page.Page(self.frame,self.sidebar_control)
        self.page_frame.pack()

    def open_user_management_tab(self,e):
        self.unselect_all_tabs()
        self.user_management_tab.click()
        self.page_frame.pack_forget()
        self.page_frame = user_management_page.Page(self.frame,self.sidebar_control)
        self.page_frame.pack()

    def open_reports_tab(self,e):
        self.unselect_all_tabs()
        self.reports_tab.click()
        self.page_frame.pack_forget()
        self.page_frame = reports_page.Page(self.frame,self.sidebar_control)
        self.page_frame.pack()

    def open_help_tab(self,e):
        self.unselect_all_tabs()
        self.Help_tab.click()
        self.page_frame.pack_forget()        
        self.page_frame = Help_and_support_page.Page(self.frame,self.sidebar_control)
        self.page_frame.pack()

# / tabs opening functions..................
    #placement methods..................................................
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = 'both',expand = True)
    # / placement methods...............................................
