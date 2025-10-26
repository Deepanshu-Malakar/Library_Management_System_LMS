from tkinter import *
from customtkinter import *
from backend import doubts_logic
set_appearance_mode("light")
from tkinter import messagebox
from components import colors

class UserCard:
    def __init__(self, master, user_id):
        self.user_id = user_id
        self.master = master
        self.role = doubts_logic.get_username_role(self.user_id)[1]

        # Main frame (slightly wider)
        self.frame = CTkFrame(
            self.master,
            fg_color="#ffffff",
            corner_radius=15,
            border_color="#e5e7eb",
            border_width=2,
            width=360,
            height=340,
        )

        # Accent color based on role
        self.role_colors = {
            "student": colors.new_button_color,#"#2563eb",
            "faculty": "#16a34a",
            "scholar": "#7e22ce",
            "librarian": "#f97316",
        }
        accent = self.role_colors.get(self.role.lower(), "#6b7280")

        # Backend logic (unchanged)
        if self.role.lower() == "student":
            doubts_logic.cur.execute(
                "select student_id,first_name,last_name,phone_no,DOB,gender,email,department from students where student_id = %s",
                (self.user_id,),
            )
            self.data = doubts_logic.cur.fetchall()
            if len(self.data) == 0:
                self.frame = CTkFrame(self.master,border_color="#e5e7eb")
                self.label = CTkLabel(self.frame,text=f"User ID {self.user_id} {self.role} has not signed up" )
                self.label.pack(padx=10,pady=10)
                return
            self.data = self.data[0]
            self.record = {
                "Role": "Student",
                "Student ID": self.data[0],
                "First Name": self.data[1],
                "Last Name": self.data[2],
                "Phone Number": self.data[3],
                "DOB (yyyy/mm/dd)": self.data[4],
                "Gender": self.data[5],
                "Email": self.data[6],
                "Department": self.data[7],
            }

        elif self.role.lower() == "faculty":
            doubts_logic.cur.execute(
                "select faculty_id,first_name,last_name,phone_no,DOB,gender,email,department from faculty where faculty_id = %s",
                (self.user_id,),
            )
            self.data = doubts_logic.cur.fetchall()
            if len(self.data) == 0:
                self.frame = CTkFrame(self.master,border_color="#e5e7eb")
                self.label = CTkLabel(self.frame,text=f"User ID {self.user_id} {self.role} has not signed up" )
                self.label.pack(padx=10,pady=10)
                return
            self.data = self.data[0]
            self.record = {
                "Role": "Faculty",
                "Faculty ID": self.data[0],
                "First Name": self.data[1],
                "Last Name": self.data[2],
                "Phone Number": self.data[3],
                "DOB (yyyy/mm/dd)": self.data[4],
                "Gender": self.data[5],
                "Email": self.data[6],
                "Department": self.data[7],
            }

        elif self.role.lower() == "librarian":
            doubts_logic.cur.execute(
                "select lib_id,first_name,last_name,phone_no,DOB,gender,email from librarian where lib_id = %s",
                (self.user_id,),
            )
            self.data = doubts_logic.cur.fetchall()
            if len(self.data) == 0:
                self.frame = CTkFrame(self.master,border_color="#e5e7eb")
                self.label = CTkLabel(self.frame,text=f"User ID {self.user_id} {self.role} has not signed up" )
                self.label.pack(padx=10,pady=10)
                return
            self.data = self.data[0]
            self.record = {
                "Role": "Librarian",
                "Librarian ID": self.data[0],
                "First Name": self.data[1],
                "Last Name": self.data[2],
                "Phone Number": self.data[3],
                "DOB (yyyy/mm/dd)": self.data[4],
                "Gender": self.data[5],
                "Email": self.data[6],
            }

        elif self.role.lower() == "scholar":
            doubts_logic.cur.execute(
                "select scholar_id,first_name,last_name,phone_no,DOB,gender,email,topic from scholars where student_id = %s",
                (self.user_id,),
            )
            self.data = doubts_logic.cur.fetchall()
            if len(self.data) == 0:
                self.frame = CTkFrame(self.master,border_color="#e5e7eb")
                self.label = CTkLabel(self.frame,text=f"User ID {self.user_id} {self.role} has not signed up" )
                self.label.pack(padx=10,pady=10)
                return
            self.data = self.data[0]
            self.record = {
                "Role": "Research Scholar",
                "Scholar ID": self.data[0],
                "First Name": self.data[1],
                "Last Name": self.data[2],
                "Phone Number": self.data[3],
                "DOB (yyyy/mm/dd)": self.data[4],
                "Gender": self.data[5],
                "Email": self.data[6],
                "Topic": self.data[7],
            }

        self.create_user(accent)

    def create_user(self, accent):
        # Header bar
        header = CTkFrame(self.frame, fg_color=accent, height=60, corner_radius=5)
        header.pack(fill="x", pady=(0, 5))

        CTkLabel(
            header,
            text=f"{self.record['First Name']} {self.record['Last Name']}",
            font=("Roboto", 14, "bold"),
            text_color="white",
        ).pack(pady=(6, 0))
        CTkLabel(
            header,
            text=self.record["Role"],
            font=("Roboto", 12),
            text_color="#f3f4f6",
        ).pack(pady=(0, 5))

        # Scrollable frame for all details
        body_canvas = CTkFrame(self.frame, fg_color="transparent", height=220)
        body_canvas.pack(fill="both", expand=True, padx=10, pady=(0, 5))

        for label, value in self.record.items():
            if label in ["Role", "First Name", "Last Name"]:
                continue
            row = CTkFrame(body_canvas, fg_color="transparent")
            row.pack(anchor="w", pady=2, fill="x")

            CTkLabel(
                row,
                text=f"{label}: ",
                font=("Roboto", 12, "bold"),
                text_color="#374151",
                width=120,
                anchor="w",
            ).pack(side="left")

            CTkLabel(
                row,
                text=str(value),
                font=("Roboto", 12),
                text_color="#1f2937",
                wraplength=200,
                anchor="w",
            ).pack(side="left")

        # Footer with Send Solution entry + button
    #     footer = CTkFrame(self.frame, fg_color="transparent")
    #     footer.pack(fill="x", padx=10, pady=(0, 8))

    #     self.solution_entry = CTkEntry(
    #         footer,
    #         placeholder_text="Write your solution...",
    #         width=220,
    #         height=30,
    #         border_color="#d1d5db",
    #         corner_radius=8,
    #     )
    #     self.solution_entry.pack(side="left", padx=(0, 10))

    #     send_btn = CTkButton(
    #         footer,
    #         text="Send",
    #         width=80,
    #         height=30,
    #         fg_color=accent,
    #         hover_color="#334155",
    #         corner_radius=8,
    #         font=("Roboto", 12, "bold"),
    #         command=self.send_solution,
    #     )
    #     send_btn.pack(side="left")

    # def send_solution(self):
    #     solution = self.solution_entry.get().strip()
    #     if not solution:
    #         messagebox.showerror("Error", "Please enter your solution first!")
    #         return
    #     # You can call backend logic here if needed
    #     messagebox.showinfo("Success", f"Solution sent: {solution}")
    #     self.solution_entry.delete(0, END)

    def grid(self, row=0, column=0, padx=10, pady=10):
        self.frame.grid(row=row, column=column, padx=padx, pady=pady, sticky="n")


# ---------------- DEMO ----------------
if __name__ == "__main__":
    root = CTk()
    root.geometry("1100x700")
    root.title("User Cards Display")

    container = CTkFrame(root, fg_color="#f8fafc")
    container.pack(fill="both", expand=True, padx=20, pady=20)

    # demo grid layout for multiple cards
    for i in range(6):
        card = UserCard(container, "123cs0056")
        card.grid(row=i // 3, column=i % 3, padx=20, pady=20)

    root.mainloop()
