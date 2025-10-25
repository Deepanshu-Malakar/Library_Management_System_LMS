from tkinter import *
from customtkinter import *
from PIL import Image
set_appearance_mode("light")
from backend import doubts_logic
from components import colors


class Doubt:
    def __init__(self, master, doubt_id, user_id, doubt,my_id):
        self.master = master
        self.my_id = my_id
        self.doubt_id = doubt_id
        self.user_id = user_id
        self.user_name,self.role = doubts_logic.get_username_role(self.user_id)
        self.doubt = doubt
        self.solutions: list = doubts_logic.get_solutions(self.doubt_id)
        self.create_bubble()

    def create_bubble(self):
        # Main card
        self.frame = CTkFrame(
            self.master,
            fg_color="#f9fafc",
            corner_radius=20,
            border_width=2,
            border_color="#d1d5db",
        )
        self.frame.pack(padx=20, pady=15, fill="x")

        # Header
        self.header = CTkLabel(
            self.frame,
            text=f"Doubt #{self.doubt_id} — by {self.user_name} ({self.role})",
            font=("Roboto", 14, "bold"),
            text_color="#111827",
            anchor="w",
        )
        self.header.pack(padx=20, pady=(15, 5), fill="x")

        # Doubt text
        self.doubt_label = CTkLabel(
            self.frame,
            text=f"{self.doubt}",
            font=("Roboto", 13),
            wraplength=700,
            text_color="#1f2937",
            justify="left",
            anchor="w",
        )
        self.doubt_label.pack(padx=25, pady=(0, 15), fill="x")

        # Divider line
        divider = CTkFrame(self.frame, height=1, fg_color="#e5e7eb")
        divider.pack(fill="x", padx=15, pady=(0, 10))

        # Solutions section
        self.solutions_container = CTkFrame(self.frame, fg_color="transparent",height=10)
        self.solutions_container.pack(fill="x", padx=10)

        if self.solutions:
            CTkLabel(
                self.solutions_container,
                text="Solutions",
                font=("Roboto", 13, "bold"),
                text_color=colors.base_color,
                anchor="w",
            ).pack(padx=10, pady=(5, 10), fill="x")

        for solver_id, solver_name, solver_role, answer in self.solutions:
            self.add_solution(solver_id, solver_name, solver_role, answer)

        # Add entry + send button for new solution
        self.add_solution_box()

    def add_solution(self, solver_id, solver_name, solver_role, answer):
        """UI for displaying one solution"""
        solution_frame = CTkFrame(
            self.solutions_container,
            fg_color="#eef2ff",
            corner_radius=15,
        )
        solution_frame.pack(padx=25, pady=8, fill="x")

        solver_label = CTkLabel(
            solution_frame,
            text=f"🧑 {solver_name} ({solver_role}) — ID: {solver_id}",
            font=("Roboto", 12, "bold"),
            text_color="#1e3a8a",
            anchor="w",
        )
        solver_label.pack(padx=15, pady=(10, 0), fill="x")

        solution_label = CTkLabel(
            solution_frame,
            text=f"→ {answer}",
            font=("Roboto", 12),
            wraplength=650,
            justify="left",
            text_color="#111827",
            anchor="w",
        )
        solution_label.pack(padx=25, pady=(5, 10), fill="x")

    def add_solution_box(self):
        """Entry + button for posting a new solution"""
        entry_frame = CTkFrame(self.frame, fg_color="#ffffff", corner_radius=10)
        entry_frame.pack(fill="x", padx=20, pady=(15, 20))

        self.solution_entry = CTkEntry(
            entry_frame,
            placeholder_text="💬 Write your solution here...",
            width=600,
            height=45,
            font=("Roboto", 12),
        )
        self.solution_entry.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.send_button = CTkButton(
            entry_frame,
            text="Send",
            height=45,
            width=120,
            fg_color=colors.base_color,
            hover_color="#1d4ed8",
            command=self.send_solution,
        )
        self.send_button.grid(row=0, column=1, padx=10, pady=10)

    def send_solution(self):
        """Triggered when user clicks 'Send'"""
        solution_text = self.solution_entry.get().strip()
        if not solution_text:
            return

        doubts_logic.answer_doubt(self.my_id,self.doubt_id,solution_text)
        my_name,my_role = doubts_logic.get_username_role(self.my_id)
        self.add_solution(self.my_id, my_name, my_role, solution_text)
        self.solution_entry.delete(0, END)

    def pack(self):
        self.frame.pack(fill="x", padx=10, pady=10)


if __name__ == "__main__":
    root = CTk()
    root.geometry("900x600")
    root.title("Ask Doubt Page")

    # Demo data
    solutions = [
        (101, "Aman", "Student", "💧 Water is essential for all life forms."),
        (105, "Suresh", "Research Scholar", "Water (H₂O) is composed of two hydrogen atoms and one oxygen atom."),
    ]

    doubt = Doubt(root, 101, "123cs0056", "What is Water?", solutions)
    doubt.pack()

    root.mainloop()


