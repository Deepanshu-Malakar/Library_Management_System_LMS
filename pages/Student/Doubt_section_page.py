from tkinter import *
from customtkinter import *
from PIL import Image
# from components import sidebar_control_button
from pages.Student.Doubt import sidebar

from pages.Student.Doubt import All_doubts
from pages.Student.Doubt import Ask_doubt
from pages.Student.Doubt import Leaderboard
from pages.Student.Doubt import My_doubts
from pages.Student.Doubt import Solved_by_me




class Page:
    def __init__(self,master,sidebar_control:sidebar.Sidebar_control):
        self.master = master
        self.current_tab = "All Doubts"
        self.sidebar_control = sidebar_control
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              corner_radius=0)
        self.create_sidebar()
        self.apply_page_controls()
        self.page_frame = All_doubts.AllDoubtsPage(self.frame)
        self.page_frame.pack()


    # Working on sidebar..............................................    
    def create_sidebar(self):
        self.sidebar = sidebar.SideBar(self.frame)
        self.sidebar.pack()

        self.sidebar_control.button.bind("<Button-1>",self.sidebar_toggle)
    
    def sidebar_toggle(self,e):
        if self.sidebar.is_expanded:
            self.sidebar.collapse()
            self.sidebar.is_expanded = False

        elif not self.sidebar.is_expanded:
            self.sidebar.expand()
            self.sidebar.is_expanded = True
    # /Working on sidebar..............................................

    # Page changing controls.........................................
    def apply_page_controls(self):
        self.sidebar.all_doubts_btn.button.bind("<Button-1>",self.open_all_doubts_page)
        self.sidebar.my_doubts_btn.button.bind("<Button-1>",self.open_my_doubts_page)
        self.sidebar.solved_by_me_btn.button.bind("<Button-1>",self.open_solved_by_me_page)
        self.sidebar.ask_doubt_btn.button.bind("<Button-1>",self.open_ask_doubt_page)
        self.sidebar.leaderboard_btn.button.bind("<Button-1>",self.open_leaderboard_page)

    def open_all_doubts_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = All_doubts.AllDoubtsPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "All Doubts"

    def open_my_doubts_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = My_doubts.MyDoubtsPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "My Doubts"

    def open_solved_by_me_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = Solved_by_me.SolvedByMePage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Solved by me"

    def open_ask_doubt_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = Ask_doubt.AskDoubtPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Ask Doubt"

    def open_leaderboard_page(self,e):
        self.page_frame.pack_forget()
        self.page_frame = Leaderboard.LeaderboardPage(self.frame)
        self.page_frame.pack()
        self.current_tab = "Leaderboard"
    # / Page changing controls...........................................



    # placement methods..................................................
    def pack(self):
        self.frame.pack(padx=0,pady=0,fill="both",expand=True,side="top")
    def pack_forget(self):
        self.frame.pack_forget()