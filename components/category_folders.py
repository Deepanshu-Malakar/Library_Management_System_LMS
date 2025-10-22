from tkinter import *
from customtkinter import *
from PIL import Image
if __name__ == "__main__":
    import colors
else:
    from components import colors

class FolderBar:
    def __init__(self,master):
        self.master = master
        self.frame = CTkFrame(self.master,
                              fg_color="transparent",
                              bg_color="transparent")
        self.add_btn = Folder(self.frame,"New Category",self,False)
        self.add_btn.button.configure(image = CTkImage(Image.open("resources/icons/add folder image.png"),size=(18,18)))
        self.add_btn.grid(row=0,column=20,padx=10,pady=5)

        self.categories = []
        self.total_categories = 0

# Add Category Function.........................
    def add_category(self,text:str,is_active:bool = False):
        category = Folder(self.frame,text,self,is_active)
        category.grid(row=0,column=self.total_categories,padx=10,pady=5)
        self.categories.append(category)
        self.total_categories+=1
        return category
 

        # self.new_window.pack()

#` Add Category Function.........................`

# Click Functions.........................
    def unclick_all_categories(self):
        for category in self.categories:
            category.unclick()
    def apply_click_functions(self,category):
        self.unclick_all_categories()
        category.click()
    def apply_category_click_functions(self):
        for category in self.categories:
            self.apply_click_functions(category)
# / Click Functions.........................
            
    
    # placement methods........
    def pack(self,padx=0,pady=0,side="left"):
        self.frame.pack(padx=padx,pady=pady,side=side)
    def place(self,x,y):
        self.frame.place(x=x,y=y)
    def grid(self,row,column,padx=0,pady=0):
        self.frame.grid(row=row,column = column , padx= padx , pady = pady)
    # / placement methods............

class Folder:
    def __init__(self,master:CTkFrame,text:str,folder_bar:FolderBar,is_active:bool=False):
        self.master = master
        self.folder_bar = folder_bar
        self.text = text
        self.is_active = is_active
        self.create_folder()
        self.apply_click_functions()
        self.apply_hover_effects()

    def create_folder(self):
        self.frame = CTkFrame(self.master,
                              fg_color="transparent",
                              bg_color="transparent",
                              border_width=0)
        self.image_filled = CTkImage(Image.open("resources/icons/filled folder2.png"),size=(18,18))
        self.image_unfilled = CTkImage(Image.open("resources/icons/unfilled folder.png"),size=(18,18))
        self.button = CTkButton(self.frame,
                                fg_color=colors.folder_bg if self.is_active else "transparent",
                                bg_color="transparent",
                                text=self.text,
                                image=self.image_filled if self.is_active else self.image_unfilled,
                                compound="left",
                                text_color=colors.base_color if self.is_active else colors.sidebar,
                                height=30,
                                width=30,
                                corner_radius=20,
                                font=("roboto",12,"bold"),
                                hover_color=colors.book_base_old,
                                command=self.click)
        self.button.pack(padx=5,pady=10)


    #hover effects..........
    def apply_hover_effects(self):
        pass
    def hover(self,event):
        pass
    def unhover(self,event):
        pass
    # / hover effects.............


    #Click Functions.............
    def apply_click_functions(self):
        pass
    def click(self):
        self.folder_bar.unclick_all_categories()
        self.button.configure(fg_color=colors.folder_bg,
                              text_color=colors.base_color,
                                image=self.image_filled)
        self.is_active = True

    def unclick(self):
        self.button.configure(fg_color="transparent",
                              text_color=colors.sidebar,
                                image=self.image_unfilled)
        self.is_active = False
    # / Click Functions...............



    #placement methods...........
    def pack(self,padx=0,pady=0,side="left"):
        self.frame.pack(padx=padx,pady=pady,side=side)
    def place(self,x,y):
        self.frame.place(x=x,y=y)
    def grid(self,row,column,padx=0,pady=0):
        self.frame.grid(row=row,column=column,padx=padx,pady=pady)
    # / placement methods.........


#/////////////////////////////////////////////////////////////////////////////////////////////////////

if __name__ == "__main__":
    root = CTk(fg_color="#FFFFFF")
    set_appearance_mode("light")
    all_btn = Folder(root,"All",True)
    all_btn.pack()
    root.mainloop()
