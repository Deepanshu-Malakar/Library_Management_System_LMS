from tkinter import *
from customtkinter import *
from PIL import Image

class AddPage:
    def __init__(self,master):
        self.master = master
        self.frame = CTkFrame(self.master,
                              fg_color="#ffffff",
                              bg_color="#ffffff")
        self.label = CTkLabel(self.frame,
                              text="Librarian Add book")
        self.label.pack()    

        self.book_details_frame = CTkFrame(self.frame,
                                           fg_color="transparent",
                                           border_color="#000000")
    def pack(self,padx=0,pady=0):
        self.frame.pack(padx=padx,pady=pady,fill = "both",expand = True)
    def pack_forget(self):
        self.frame.pack_forget()

if __name__ == "__main__":
    root = CTk()
    root.geometry("1024x1024")
    set_appearance_mode("light")
    frame = AddPage(root)
    frame.pack()
    root.mainloop()