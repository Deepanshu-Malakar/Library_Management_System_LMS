from tkinter import *
from customtkinter import *
from PIL import Image

class AddPage:
    def __init__(self,master):
        self.master = master
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              bg_color="#ffffff")
 
        self.book_details_frame = CTkFrame(self.frame,
                                           fg_color="transparent",
                                           border_color="#9D9D9D",
                                           border_width=0)
        self.upper_frame = CTkFrame(self.book_details_frame,
                                    fg_color="transparent")
        self.heading = CTkLabel(self.upper_frame,text="Enter The Following Details",font=("roboto",12,"bold"))
        self.heading.pack(pady=5)
        self.upper_frame.pack(side="top",pady=5)
        
        self.left_frame = CTkFrame(self.book_details_frame,
                                   fg_color="transparent")
        self.right_frame = CTkFrame(self.book_details_frame,
                                    fg_color="transparent")
        
        
        self.title = Form(self.right_frame,"Title")
        self.author = Form(self.right_frame,"Author")
        self.edition = Form(self.right_frame,"Edition")
        self.total_copies = Form(self.right_frame,"Total Copies")
        self.cover_img = Form(self.right_frame,"Cover Image Link")
        self.category_label = CTkLabel(self.right_frame,
                                       text="Category",
                                       font=("roboto",12))
        self.category_list = CTkComboBox(self.right_frame,
                                        width=200,
                                        values=["Story Books",
                                                "Mechanical Engineering",
                                                "Electrical Engineering",
                                                "Computer Science",
                                                "Maths",
                                                "Chemistry",
                                                "Philosopy",
                                                "Science"],
                                        font=("roboto",12))
        self.description = Description(self.right_frame)


        
        self.title.grid(0)
        self.author.grid(1)
        self.edition.grid(2)
        self.total_copies.grid(3)
        self.cover_img.grid(4)
        self.category_label.grid(row=5,column=0,padx=10,pady=5)
        self.category_list.grid(row=5,column=1,padx=10,pady=5)
        self.description.grid(row=6)


        self.left_frame.pack(side="left",padx=5,pady=5)

        self.logo_img = CTkImage(Image.open("resources/Books/cover page.png"),size=(1.1*180,1.1*280))
        self.logo_img_label = CTkLabel(self.left_frame,text="",image=self.logo_img)
        self.logo_img_label.pack(padx=10,pady=0)

        self.change_logo_btn = CTkButton(self.left_frame,text="Upload Logo",width=198)
        self.change_logo_btn.pack(pady=2)
        self.right_frame.pack(side="right",padx=5,pady=5)

        self.book_details_frame.pack(padx=20,pady=50)
        

    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = "both",expand = True)
    def pack_forget(self):
        self.frame.pack_forget()

class Description:
    def __init__(self,master):
        self.frame = CTkFrame(master,
                              fg_color="transparent")
        
        self.description_label = CTkLabel(self.frame,
                                          text="Description",
                                          font=("roboto",12))
        
        self.description_entry = CTkTextbox(self.frame,
                                            font=("roboto",12),
                                            width=400,
                                            height=100,
                                            border_color="#9D9D9D",
                                            border_width=1)
        self.description_label.grid(row=0,column=0,pady=0,columnspan=2)
        self.description_entry.grid(row=1,column=0,columnspan=2)
    
    def grid(self,row):
        self.frame.grid(row=row,column=0,columnspan=2,padx=10,pady=5)
    
class Form:
    def __init__(self,master,text):
        self.label = CTkLabel(master,
                              text=text,
                              fg_color="transparent",
                              font=("roboto",12))
        self.entry = CTkEntry(master,
                              width=200,
                              font=("roboto",12))
    def grid(self,row):
        self.label.grid(row=row,column=0,padx=10,pady=5)
        self.entry.grid(row=row,column=1,padx=10,pady=5)

if __name__ == "__main__":
    root = CTk()
    root.geometry("1024x1024")
    set_appearance_mode("light")
    frame = AddPage(root)
    frame.pack()
    root.mainloop()