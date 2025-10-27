import customtkinter as ctk
import tkinter as tk
from backend import register_users
from backend import mysql_tables
from tkinter import messagebox

class colors:
    def __init__(self):
        self.purple = "#613287"
        self.pink = "#D0A2E9"
        self.grey = "#EAE6E6"

class Form:
    def __init__(self, master, text, hide=False, is_dob=False, is_phone=False, max_length=None):
        self.master = master
        self.text = text
        self.hide = hide
        self.is_dob = is_dob 
        self.is_phone = is_phone
        self.max_length = max_length
        
        self.frame = ctk.CTkFrame(self.master,
                                  fg_color="transparent",
                                  bg_color="transparent",
                                  width=250,
                                  height=65)
        self.create_form()

    def create_form(self):
        self.label = ctk.CTkLabel(self.frame,
                                  text=self.text,
                                  text_color=colors().purple,
                                  font=("roboto", 12),
                                  )
        self.label.place(x=5, y=0)
        
        self.entry_var = tk.StringVar() 
        vcmd = None
        
        # Validation Command (vcmd)
        if self.is_dob:
            vcmd = self.master.register(self.validate_dob_input) 
        
        elif self.is_phone:
             vcmd = self.master.register(self.validate_phone_input) 
        
        elif self.max_length is not None:
             vcmd = self.master.register(self.validate_generic_max_length)
             
        # Entry Widget
        if vcmd:
            self.entry = ctk.CTkEntry(self.frame,
                                  show="*" if self.hide else None,
                                  text_color=colors().purple,
                                  fg_color="white",             
                                  bg_color="transparent",
                                  border_width=2,              
                                  border_color=colors().purple, 
                                  corner_radius=5,              
                                  height=30,                    
                                  width=220,
                                  font=("roboto", 12),
                                  textvariable=self.entry_var, 
                                  validate='key', 
                                  validatecommand=(vcmd, '%S', '%P')) 
        else:
            self.entry = ctk.CTkEntry(self.frame,
                                  show="*" if self.hide else None,
                                  text_color=colors().purple,
                                  fg_color="white",            
                                  bg_color="transparent",
                                  border_width=2,              
                                  border_color=colors().purple, 
                                  corner_radius=5,              
                                  height=30,                   
                                  width=220,
                                  font=("roboto", 12),
                                  textvariable=self.entry_var) 

        if self.is_dob:
            self.entry.bind("<KeyRelease>", self.format_dob_on_key_release)
            
        self.entry.place(x=0, y=25)
    
    # Validation Checks
    def validate_generic_max_length(self, S, P):
        if self.max_length is not None and len(P) > self.max_length:
            return False
        return True
        
    def validate_phone_input(self, S, P):
        if not S.isdigit() and S != '':
            return False
        if len(P) > 10:
            return False
        return True
        
    def validate_dob_input(self, S, P):
        if not S.isdigit() and S != '':
            return False
        if len(P) > 10:
            return False
        return True
        
    def format_dob_on_key_release(self, event):
        if event.keysym in ('BackSpace', 'Delete', 'Left', 'Right', 'Tab'):
            return
            
        current_text = self.entry_var.get()
        cleaned = "".join(c for c in current_text if c.isdigit())
        if len(cleaned) > 8:
            cleaned = cleaned[:8]
        
        formatted = ""
        
        if len(cleaned) >= 4:
            formatted += cleaned[0:4] + "/"
        else:
            formatted += cleaned
            
        if len(cleaned) >= 6:
            formatted += cleaned[4:6] + "/"
        elif len(cleaned) > 4:
            formatted += cleaned[4]
            
        if len(cleaned) > 6:
            formatted += cleaned[6:8]

        if formatted.endswith('/') and len(formatted.replace('/', '')) < len(cleaned):
            if len(formatted) == 4 and len(cleaned) == 5:
                formatted = formatted[:-1]
            elif len(formatted) == 8 and len(cleaned) == 6:
                formatted = formatted[:-1]

        self.entry_var.set(formatted)
        try:
            self.entry.icursor(len(formatted))
        except:
             pass 
        
    def get_entry(self):
        return self.entry

    def place(self, x, y):
        self.frame.place(x=x, y=y)
        
    def pack(self, padx=0, pady=0, side=tk.TOP, fill=tk.NONE, expand=False):
        self.frame.pack(padx=padx, pady=pady, side=side, fill=fill, expand=expand)

    def grid(self, row, column, padx=0, pady=0, sticky=""):
        self.frame.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)


class LibrarianSignupApp(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        # self.title("Librarian Signup")
        # self.geometry("700x850") 
        # ctk.set_appearance_mode("System")

        self.main_frame = ctk.CTkFrame(self, 
                                       fg_color="white", 
                                       corner_radius=15,
                                       border_width=2,
                                       border_color=colors().purple)
        self.main_frame.pack(padx=50, pady=50, fill="y") 
        
        self.title_label = ctk.CTkLabel(self.main_frame,
                                        text="LIBRARIAN REGISTRATION",
                                        font=("roboto", 24, "bold"),
                                        text_color=colors().purple)
        self.title_label.pack(pady=20)
        
        # Form Layout
        self.form_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.form_frame.pack(padx=20, pady=10, fill="x")
        
        self.form_frame.columnconfigure(0, weight=1)
        self.form_frame.columnconfigure(1, weight=1)

        # Row 0: Employee ID (Left) and Name (Right)
        self.employee_id = Form(self.form_frame, text="Employee ID:", max_length=50) 
        self.employee_id.grid(row=0, column=0, padx=30, pady=15, sticky="w")
        
        self.name = Form(self.form_frame, text="Full Name:")
        self.name.grid(row=0, column=1, padx=30, pady=15, sticky="w")

        # Row 1: Email (Left) and Phone No. (Right)
        self.email = Form(self.form_frame, text="Email:", max_length=50)
        self.email.grid(row=1, column=0, padx=30, pady=15, sticky="w")
        
        self.phone = Form(self.form_frame, text="Phone No.:", is_phone=True)
        self.phone.grid(row=1, column=1, padx=30, pady=15, sticky="w")

        # Row 2: Gender (Left) and DOB (Right)
        self.gender_label = ctk.CTkLabel(self.form_frame, text="Gender:", text_color=colors().purple, font=("roboto", 12))
        self.gender_label.grid(row=2, column=0, padx=30, pady=(15, 0), sticky="w")
        self.gender_combo = ctk.CTkComboBox(self.form_frame, 
                                            values=["Male", "Female", "Other"],
                                            dropdown_fg_color="white",
                                            dropdown_text_color="black", 
                                            border_color=colors().purple,
                                            button_color=colors().purple,
                                            width=220,
                                            height=30, # Added height for visual alignment
                                            state="readonly")
        self.gender_combo.set("Select Gender")
        self.gender_combo.grid(row=2, column=0, padx=30, pady=(40, 15), sticky="w")
        
        self.dob = Form(self.form_frame, text="Date of Birth (YYYY/MM/DD):", is_dob=True)
        self.dob.grid(row=2, column=1, padx=30, pady=15, sticky="w") 

        # Row 3: Job Title (Left) and Shift Timing (Right)
        self.job_title_label = ctk.CTkLabel(self.form_frame, text="Job Title:", text_color=colors().purple, font=("roboto", 12))
        self.job_title_label.grid(row=3, column=0, padx=30, pady=(15, 0), sticky="w")
        self.job_title_combo = ctk.CTkComboBox(self.form_frame, 
                                            values=["Head Librarian", "Cataloger", "Circulation Desk", "Reference Staff"],
                                            dropdown_fg_color="white",
                                            dropdown_text_color="black", 
                                            border_color=colors().purple,
                                            button_color=colors().purple,
                                            width=220,
                                            height=30,
                                            state="readonly")
        self.job_title_combo.set("Select Job Title")
        self.job_title_combo.grid(row=3, column=0, padx=30, pady=(40, 15), sticky="w")
        
        self.shift_timing_label = ctk.CTkLabel(self.form_frame, text="Shift Timing:", text_color=colors().purple, font=("roboto", 12))
        self.shift_timing_label.grid(row=3, column=1, padx=30, pady=(15, 0), sticky="w")
        self.shift_timing_combo = ctk.CTkComboBox(self.form_frame, 
                                            values=["Shift 1(9:00-13:00)", "Afternoon (14:00-22:00)", "Night (22:00-06:00)"],
                                            dropdown_fg_color="white",
                                            dropdown_text_color="black", 
                                            border_color=colors().purple,
                                            button_color=colors().purple,
                                            width=220,
                                            height=30,
                                            state="readonly")
        self.shift_timing_combo.set("Select Shift")
        self.shift_timing_combo.grid(row=3, column=1, padx=30, pady=(40, 15), sticky="w")
        

        # Row 4: Password (Left) and Confirm Password (Right)
        self.password = Form(self.form_frame, text="Password:", hide=True)
        self.password.grid(row=4, column=0, padx=30, pady=15, sticky="w")
        
        self.confirm_password = Form(self.form_frame, text="Confirm Password:", hide=True)
        self.confirm_password.grid(row=4, column=1, padx=30, pady=15, sticky="w")

        # Submit Button
        self.submit_button = ctk.CTkButton(self.main_frame, 
                                           text="Signup",
                                           command=self.submit_form,
                                           fg_color=colors().purple,
                                           hover_color=colors().pink,
                                           text_color="white",
                                           font=("roboto", 16, "bold"),
                                           width=200,
                                           height=40)
        self.submit_button.pack(pady=30) 

        # Message Label for Errors/Success
        self.message_label = ctk.CTkLabel(self.main_frame, text="", text_color="red")
        self.message_label.pack(pady=5)


    def submit_form(self):
        self.message_label.configure(text="")
        
        data = {
            "Employee ID": self.employee_id.get_entry().get(),
            "Full Name": self.name.get_entry().get(),
            "Email": self.email.get_entry().get(),
            "Phone No.": self.phone.get_entry().get(),
            "Date of Birth": "".join(c for c in self.dob.get_entry().get() if c.isdigit()), 
            "Job Title": self.job_title_combo.get(),
            "Shift Timing": self.shift_timing_combo.get(),
            "Gender": self.gender_combo.get(),
            "Password": self.password.get_entry().get(),
            "Confirm Password": self.confirm_password.get_entry().get()
        }
        
        unfilled_combo_defaults = ["Select Job Title", "Select Shift", "Select Gender"] 

        # Mandatory Field Validation
        missing_fields = []
        for key, value in data.items():
            if not value.strip():
                missing_fields.append(key)
            # Check for unfilled comboboxes
            elif key in ["Job Title", "Shift Timing", "Gender"] and value in unfilled_combo_defaults:
                missing_fields.append(key)

        if missing_fields:
            error_message = f"Error: Please fill all mandatory fields. Missing: {', '.join(missing_fields)}"
            self.message_label.configure(text=error_message, text_color="red")
            return
            
        # Ph.No. must be atleast 10 digits
        phone_no = data["Phone No."].strip()
        if len(phone_no) != 10:
             self.message_label.configure(text="Error: Phone No. must be 10 digits.", text_color="red")
             return
            
        #Password Match
        if data["Password"] != data["Confirm Password"]:
            self.message_label.configure(text="Error: Passwords are NOT confirmed. They do not match!", text_color="red")
            return
            
        # Password must be atleast 8 characters long
        password = data["Password"]
        if len(password) < 8 or not any(c.isdigit() for c in password) or not any(c.isalpha() for c in password):
            self.message_label.configure(text="Error: Password must be at least 8 characters and contain both letters and numbers.", text_color="red")
            return

        # Check for valid user.............
        if not register_users.check_if_user_exist(data["Employee ID"]):
            messagebox.showerror("Error","User Invalid")
            return
        
        # check if already registered.........
        lib_id = data["Employee ID"]
        register_users.cur.execute(f"select * from librarian where lib_id = '{lib_id}'")
        user_exist = register_users.cur.fetchall()
        if len(user_exist)>0:
            messagebox.showerror("Error","Librarian Already Registered")
            return
        
        # email does not match...........
        register_users.cur.execute(f"select email,role from users where user_id = '{lib_id}'")
        email,role = register_users.cur.fetchall()[0]

        if email != data["Email"]:
            messagebox.showerror("Error","Email does not match")
            return
        
        if role.lower() != 'librarian':
            messagebox.showerror("Error","User is not a Librarian")
            return
        
        first_name = data["Full Name"].split()[0]
        if len(data["Full Name"]) > 0:
            last_name = data["Full Name"].split()[1]
        else:
            last_name = ""

        mysql_tables.insert_librarian(data["Employee ID"],first_name,last_name,data["Phone No."],data["Date of Birth"],"M" if data["Gender"].lower() == 'male' else "F",
                                      data["Email"],data["Password"])

        messagebox.showinfo("Success","Librarian registered successfully")        

        # If all checks pass
        success_message = f"Signup Successful for Librarian: {data['Full Name']}!"
        self.message_label.configure(text=success_message, text_color="green")
        print("Librarian Data Submitted:", data)

if __name__ == "__main__":
    app = LibrarianSignupApp()
    app.mainloop()
