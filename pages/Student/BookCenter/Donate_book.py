from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import Image
from backend import mysql_tables
from tkinter.filedialog import askopenfilename
from components import colors
from AI import ai

class DonateBookPage:
    def __init__(self,master):
        self.master = master
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              bg_color="#ffffff")
        self.book_details_frame = CTkFrame(self.frame,
                                           fg_color="#ffffff",
                                           border_color="#EDEBEB",
                                           border_width=1)
        self.upper_frame = CTkFrame(self.book_details_frame,
                                    fg_color="transparent")
        self.heading = CTkLabel(self.upper_frame,text="Enter The Following Details",font=("roboto",12,"bold"))
        self.heading.pack(pady=10,padx=20,side="left")
        self.upper_frame.pack(side="top",pady=5,fill="x")
        
        self.left_frame = CTkFrame(self.book_details_frame,
                                   fg_color="transparent")
        self.right_frame = CTkFrame(self.book_details_frame,
                                    fg_color="transparent")
        
        
        self.title = Form(self.right_frame,"Title")
        self.author = Form(self.right_frame,"Author")
        self.edition = Form(self.right_frame,"Edition")
        # self.total_copies = Form(self.right_frame,"Total Copies")
        self.cover_img = Form(self.right_frame,"Cover Image Link")
        self.category_label = CTkLabel(self.right_frame,
                                       text="Category",
                                       font=("roboto",12))
        self.category_list = CTkComboBox(self.right_frame,
                                        width=200,
                                        values=["Story Books","Philosopy","Science","Computer Science","History","Biography","Comics","Fantasy","Mystery","Romance","Horror","Mechanical Engineering","Electrical Engineering"],
                                        font=("roboto",12),
                                        border_width=0,
                                        button_color=colors.base_color,
                                        dropdown_fg_color="#ffffff",
                                        fg_color="#F7F8FF")
        self.description = Description(self.right_frame)
        self.description.generate_description_btn.configure(command=lambda e=None: self.generate_book_description(e))


        
        self.title.grid(0)
        self.author.grid(1)
        self.edition.grid(2)
        # self.total_copies.grid(3)
        self.cover_img.grid(4)
        self.category_label.grid(row=5,column=0,padx=10,pady=5)
        self.category_list.grid(row=5,column=1,padx=10,pady=5)
        self.description.grid(row=6,pady=10)


        self.left_frame.pack(side="left",padx=5,pady=5)

        self.logo_img = CTkImage(Image.open("resources/Books/cover page.png"),size=(1.3*180,1.3*280))
        self.logo_img_label = CTkLabel(self.left_frame,text="",image=self.logo_img)
        self.logo_img_label.pack(padx=10,pady=0)

        self.change_logo_btn = CTkButton(self.left_frame,
                                         text="Upload Logo",
                                         width=1.3*180,
                                         command = self.upload_logo,
                                         fg_color=colors.base_color,
                                         corner_radius=2)
        self.change_logo_btn.pack(pady=2)
        self.right_frame.pack(side="right",padx=5,pady=5)

        self.book_details_frame.pack(padx=10,pady=100)
        # self.book_details_frame.place(x=10,y=10)

        self.add_book_btn = CTkButton(self.upper_frame,
                                      text="Donate Book",  
                                        width=100,
                                        height=40,
                                        command=self.add_book,
                                        fg_color=colors.base_color,
                                        corner_radius=2)
        self.add_book_btn.pack(padx=20,pady=10,side='right')
        # self.create_tables_frame()

    def create_tables_frame(self):
        self.tables_frame = CTkFrame(self.frame,
                                     fg_color="#F7F8FF",
                                     width=300)
        self.tables_frame.pack(side="right",padx=0,pady=0,fill="y")

# clear fields method.................................................
    def clear_fields(self):
        self.title.entry.delete(0,END)
        self.author.entry.delete(0,END)
        self.edition.entry.delete(0,END)
        # self.total_copies.entry.delete(0,END)
        self.cover_img.entry.delete(0,END)
        self.category_list.set("")
        self.description.description_entry.delete("1.0","end-1c")





# controller methods....................................................
    def upload_logo(self):
        file_path = askopenfilename(title="Select Cover Image",filetypes=[("Image Files","*.png *.jpg *.jpeg *.bmp")])
        if file_path!="":
            self.cover_img.entry.delete(0,END)
            self.cover_img.entry.insert(0,file_path)
            logo_img = CTkImage(Image.open(file_path),size=(1.3*180,1.3*280))
            self.logo_img_label.configure(image=logo_img)

    def check_if_book_exists(self,title,author,edition):
        mysql_tables.cur.execute("select * from books where title=%s and author=%s and edition=%s",(title,author,edition))
        result = mysql_tables.cur.fetchall()
        if len(result)>0:
            return True
        return False
    
    def update_or_retain_description(self,title,author,edition,new_description):
        if self.check_if_book_exists(title,author,edition):
            if new_description =="No Description Available":
                mysql_tables.cur.execute("select description from books where title=%s and author=%s and edition=%s",(title,author,edition))
                result = mysql_tables.cur.fetchall()
                description =  result[0][0]
                return description
            else:
                mysql_tables.cur.execute("update books set description=%s where title=%s and author=%s and edition=%s",(new_description,title,author,edition))
                mysql_tables.mydb.commit()
                return new_description
        else:
            return new_description

        
    def add_book(self):
        title = self.title.entry.get()
        author = self.author.entry.get()
        edition = self.edition.entry.get()
        # total_copies = self.total_copies.entry.get()
        cover_img = self.cover_img.entry.get()
        category = self.category_list.get()
        description = self.description.description_entry.get("1.0","end-1c")
        if title=="" or author=="" or edition==""  or category=="":
            messagebox.showerror("error","All Fields are Required")
        else:
            cover_img = cover_img if cover_img!="" else "resources/Books/cover page.png"
            description = description if description!="" else "No Description Available"
            description = self.update_or_retain_description(title,author,edition,description)
            for i in range(int(1)):
                book_id = mysql_tables.generate_book_id()
                mysql_tables.insert_book(book_id,title,author,edition,category,"Available","1",cover_img,description)
            messagebox.showinfo("Success","Book Donated Successfully, Thanks for your contribution")
            self.clear_fields()
            self.logo_img_label.configure(image=self.logo_img)


    def generate_book_description(self,e):
        title = self.title.entry.get()
        author = self.author.entry.get()
        self.description.description_entry.delete("1.0","end-1c")
        self.description.description_entry.insert("1.0","Generating Description...")
        self.description.description_entry.after(100,lambda: self.fetch_description(title,author))

    def fetch_description(self,title,author):
        prompt = f"Generate a book description for a book titled '{title}' written by '{author}' in about 2 to 3 lines. Do not mention the title or author in the description."
        try:
            description = ai.query(prompt)
        except Exception as e:
            description = "Model Unavailable. Please try again later."
        self.description.description_entry.delete("1.0","end-1c")
        self.description.description_entry.insert("1.0",description)

# / controller methods....................................................








# placement methods.......................................................
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = "both",expand = True)
    def pack_forget(self):
        self.frame.pack_forget()
#.................................................................





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
                                            border_color=colors.base_color,
                                            border_width=0,
                                            fg_color="#F7F8FF")
        self.generate_description_btn = CTkButton(self.frame,
                                                  text="Generate Description",
                                                  width=400,
                                                  fg_color=colors.base_color,
                                                  corner_radius=2)
        
        self.description_label.grid(row=0,column=0,padx=0,pady=2,columnspan=1)
        self.generate_description_btn.grid(row=2,column=0,pady=2,padx=0,columnspan=2)
        self.description_entry.grid(row=1,column=0,columnspan=2)
    
    def grid(self,row,pady=5):
        self.frame.grid(row=row,column=0,columnspan=2,padx=10,pady=pady)
    
class Form:
    def __init__(self,master,text):
        self.label = CTkLabel(master,
                              text=text,
                              fg_color="transparent",
                              font=("roboto",12))
        self.entry = CTkEntry(master,
                              width=200,
                              font=("roboto",12),
                              border_width=0,
                              fg_color="#F7F8FF")
    def grid(self,row):
        self.label.grid(row=row,column=0,padx=10,pady=5)
        self.entry.grid(row=row,column=1,padx=10,pady=5)

if __name__ == "__main__":
    root = CTk()
    root.geometry("1024x1024")
    set_appearance_mode("light")
    frame = DonateBookPage(root)
    frame.pack()
    root.mainloop()