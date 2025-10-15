from tkinter import messagebox, END
from customtkinter import *

class StudentSignup(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="white")
        
        # This guard flag is the key to preventing the infinite loop
        self._is_formatting_dob = False

        # Title
        self.title_label = CTkLabel(self, text="Student Signup", 
                                    font=("Arial", 20, "bold"), text_color="black")
        self.title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        # Fields for a Student
        fields = ["Student ID", "Name", "Department", "Phone No", "Email", "Date of Birth (YYYY-MM-DD)", "Gender", "Password", "Confirm Password"]
        self.entries = {}

        for i, field in enumerate(fields):
            label = CTkLabel(self, text=field, font=("Arial", 15), text_color="black")
            label.grid(row=i+1, column=0, sticky="w", padx=20, pady=5)
            
            if field == "Gender":
                entry = CTkOptionMenu(self, 
                                      values=["Select Gender", "Male", "Female", "Other"],
                                      fg_color="black",
                                      button_color="black",
                                      button_hover_color="#333333",
                                      text_color="white")
                entry.set("Select Gender")
            elif field == "Date of Birth (YYYY-MM-DD)":
                entry = CTkEntry(self,
                                 fg_color="black",
                                 text_color="white",
                                 border_color="#333333",
                                 placeholder_text="YYYY/MM/DD")
                entry.bind("<KeyRelease>", self.format_dob_on_keypress)
            elif "Password" in field:
                entry = CTkEntry(self, 
                                 show="*",
                                 fg_color="black",
                                 text_color="white",
                                 border_color="#333333")
            else:
                entry = CTkEntry(self,
                                 fg_color="black",
                                 text_color="white",
                                 border_color="#333333")
                
            entry.grid(row=i+1, column=1, sticky="ew", padx=20, pady=5)
            self.entries[field] = entry

        # Sign Up button
        self.signup_button = CTkButton(self, text="Sign Up", command=self.signup, fg_color="#437EDF", hover_color="#1D63FA")
        self.signup_button.grid(row=len(fields)+1, column=0, columnspan=2, pady=20)
        
        self.grid_columnconfigure(1, weight=1)

    def format_dob_on_keypress(self, event):
        # If the function is already running, exit immediately to prevent a loop.
        if self._is_formatting_dob:
            return
        
        try:
            self._is_formatting_dob = True
            
            entry = self.entries["Date of Birth (YYYY-MM-DD)"]
            current_text = entry.get()
            
            digits = "".join(filter(str.isdigit, current_text))[:8]
            
            formatted_text = ""
            if len(digits) > 0:
                formatted_text = digits[:4]
            if len(digits) > 4:
                formatted_text = f"{digits[:4]}/{digits[4:6]}"
            if len(digits) > 6:
                formatted_text = f"{digits[:4]}/{digits[4:6]}/{digits[6:]}"

            entry.delete(0, END)
            entry.insert(0, formatted_text)
            entry.icursor(END)
        finally:
            self._is_formatting_dob = False

    def signup(self):
        values = {field: entry.get() for field, entry in self.entries.items()}
        
        slid_key = "Student ID (SLID)"
        if slid_key in values:
            values[slid_key] = values[slid_key].lower()

        if values.get("Gender") == "Select Gender":
            messagebox.showerror("Error", "Please select a Gender")
            return
            
        for field, value in values.items():
            if not value:
                messagebox.showerror("Error", f"{field} is required")
                return
        
        if values["Password"] != values["Confirm Password"]:
            messagebox.showerror("Error", "Passwords do not match")
            return
        
        messagebox.showinfo("Success", f"Student account created for {values['Name']}")

        for entry in self.entries.values():
            if isinstance(entry, CTkEntry):
                entry.delete(0, END)

if __name__ == "__main__":
    root = CTk()
    root.geometry("500x550")
    root.title("Student Signup Page")

    # This creates the signup form
    signup_page = StudentSignup(root)
    
    # This places the form in the window so you can see it
    signup_page.pack(padx=20, pady=20, expand=True, fill="both")

    root.mainloop()