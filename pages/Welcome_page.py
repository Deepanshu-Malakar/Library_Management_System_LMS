from customtkinter import *
from tkinter import *
from PIL import Image
from pages import signin_page
import pywinstyles
set_appearance_mode("light")

class colors:
    def __init__(self):
        self.login = "#7F495D"
        self.login_hover = "#663A4A"
        self.role = "#6A3E50"

class button:
    def __init__(self,master,text,image,command):
        self.master = master
        self.width = 94
        self.height = 42
        self.image = CTkImage(Image.open(image),size=(18,18))
        self.button = CTkButton(self.master,
                                text=text,
                                image=self.image,
                                width=self.width,
                                height=self.height,
                                bg_color="#6D3F50",
                                fg_color = colors().login,
                                font= ("roboto",12),
                                corner_radius=1,
                                border_width=0,
                                hover_color=colors().login_hover,
                                command=command) 
        
    def place(self,x,y):
        self.button.place(x=x,y=y)
#/////////////////////////////////////////////////////////////////////////

class RoleButtons:
    def __init__(self,master,text,image,command,is_active = False):
        self.master = master
        self.is_active = is_active
        self.command = command

        self.frame = CTkFrame(self.master,
                              fg_color=colors().role,
                              corner_radius=0,
                              width=288,
                              height=70)
        # pywinstyles.set_opacity(self.frame,0.9)

        self.button = CTkButton(self.frame,
                                text=text,
                                image=CTkImage(Image.open(image),size=(25,25)),
                                fg_color="transparent",
                                bg_color="transparent",
                                font=("roboto",16),
                                width=100,
                                hover_color=colors().login_hover,
                                command=command)
        
        self.button.place(x=22,y=18)

        self.check_img = 'resources/icons/'+ ('unreserve2.png' if self.is_active else 'reserve.png')
        self.check_label = CTkLabel(self.frame,
                                    text="",
                                    image=CTkImage(Image.open(self.check_img),size=(30,30))
                                    )
        self.check_label.place(x = 230, y = 17)
        self.apply_hover_effects()    
        self.apply_click_effects()

    # placement methods..........................
    def place(self,x,y):
        self.frame.place(x = x, y = y)
    # placement methods..........................



    #Hover effects...............
    def apply_hover_effects(self):
        self.frame.bind("<Enter>",self.hover)
        self.frame.bind("<Leave>",self.unhover)

    def hover(self,e):
        self.frame.configure(fg_color = colors().login_hover)

    def unhover(self,e):
        self.frame.configure(fg_color = colors().role)
    # /Hover effects................


    #Click effects.............................
    def click(self,e):
        self.command()

    def apply_click_effects(self):
        self.frame.bind("<Button-1>",self.click)
    #/Click effects.............................. 

#//////////////////////////////////////////////////////////////////
class Welcome_page:
    def __init__(self,master:CTk):
        self.role = "Student"
        self.width = 2228
        self.height = 1480
        self.factor = 0.5


        self.master = master
        self.frame = CTkFrame(self.master,
                              width=self.factor*self.width,
                              height=self.factor*self.height)

        self.background_image = CTkImage(Image.open('resources/Background images/welcome page brown6.png'),
                                         size=(self.factor*self.width,self.factor*self.height))
        
        self.background_img_label = CTkLabel(self.frame,
                                             text="",
                                             image=self.background_image)
        self.background_img_label.place(x=0,y=0)

        self.login_btn =button(self.frame,
                               text="Login",
                               image="resources/icons/sign in.png",
                               command=self.login)
        
        self.signup_btn = button(self.frame,
                                 text="Sign up",
                                 image="resources/icons/new user logo.png",
                                 command=self.signup)
        
        self.login_btn.place(x = 875,y = 19)
        self.signup_btn.place(x = 983, y = 19)

        # left side..........
        self.student_role_btn = RoleButtons(self.frame,
                                            text="Student",
                                            image="resources/icons/student logo.png",
                                            command=self.student_role,
                                            is_active=True)
        self.faculty_role_btn = RoleButtons(self.frame,
                                            text="Faculty",
                                            image="resources/icons/faculty logo.png",
                                            command= self.faculty_role,
                                            is_active=False)
        
        self.librarian_role_btn = RoleButtons(self.frame,
                                            text="Librarian",
                                            image="resources/icons/StudyLight.png",
                                            command= self.librarian_role,
                                            is_active=False)
        
        self.scholar_role_btn = RoleButtons(self.frame,
                                            text="Scholar",
                                            image="resources/icons/scholar logo.png",
                                            command= self.scholar_role,
                                            is_active=False)
        
        
        self.student_role_btn.place(x=150,y=235)
        self.librarian_role_btn.place(x=150,y=310)
        self.faculty_role_btn.place(x=150,y=387)
        self.scholar_role_btn.place(x=150,y=464)
        # /left side............




    #placement methods............
    def pack(self,padx=0,pady=0,side=TOP):
        self.frame.pack(padx = padx , pady = pady , side = side)
    # // placement methods...............


    # Click functions .........................
    def login(self):
        self.frame.pack_forget()
        self.frame = signin_page.Signin_page(self.master)
        self.frame.pack()
        self.master.resizable(True,True)

    def student_role(self):
        self.role = "Student"
        self.uncheck_all_roles()
        self.student_role_btn.check_label.configure(image = CTkImage(Image.open("resources/icons/unreserve2.png"),size=(30,30)))

    def librarian_role(self):
        self.role = "Librarian"
        self.uncheck_all_roles()
        self.librarian_role_btn.check_label.configure(image = CTkImage(Image.open("resources/icons/unreserve2.png"),size=(30,30)))

    def faculty_role(self):
        self.role = "Faculty"
        self.uncheck_all_roles()
        self.faculty_role_btn.check_label.configure(image = CTkImage(Image.open("resources/icons/unreserve2.png"),size=(30,30)))

    def scholar_role(self):
        self.role = "Scholar"
        self.uncheck_all_roles()
        self.scholar_role_btn.check_label.configure(image = CTkImage(Image.open("resources/icons/unreserve2.png"),size=(30,30)))


    def uncheck_all_roles(self):
        self.student_role_btn.check_label.configure(image = CTkImage(Image.open("resources/icons/reserve.png"),size=(30,30)))
        self.faculty_role_btn.check_label.configure(image = CTkImage(Image.open("resources/icons/reserve.png"),size=(30,30)))
        self.librarian_role_btn.check_label.configure(image = CTkImage(Image.open("resources/icons/reserve.png"),size=(30,30)))
        self.scholar_role_btn.check_label.configure(image = CTkImage(Image.open("resources/icons/reserve.png"),size=(30,30)))
        print(self.role)

    def signup(self):
        pass
    # // Click functions .........................

if __name__ == "__main__":
    root = CTk()

    frame = Welcome_page(root)
    frame.pack()
    root.mainloop()