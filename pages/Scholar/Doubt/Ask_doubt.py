from tkinter import *
from customtkinter import *
from PIL import Image
from backend import doubts_logic
from components import colors

class AskDoubtPage:
    def __init__(self,master,scholar_record):
        self.scholar_record = scholar_record
        self.master = master
        self.frame = CTkFrame(
            self.master,
            fg_color="#f8f9fd",
            bg_color="#f8f9fd"
        )

        # ----- HEADER -----
        self.header_frame = CTkFrame(
            self.frame,
            fg_color=colors.base_color,
            corner_radius=0,
            height=60
        )
        self.header_label = CTkLabel(
            self.header_frame,
            text="💭 Ask a Doubt",
            text_color="white",
            font=("Roboto", 20, "bold")
        )
        self.header_label.pack(pady=10)
        self.header_frame.pack(fill="x")

        # ----- SCROLLABLE DOUBT DISPLAY -----
        self.scroll_canvas = Canvas(
            self.frame,
            bg="#f8f9fd",
            highlightthickness=0
        )
        self.scroll_canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar = Scrollbar(
            self.frame,
            orient=VERTICAL,
            command=self.scroll_canvas.yview
        )
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.doubt_show_frame = CTkFrame(
            self.scroll_canvas,
            fg_color="transparent"
        )
        self.scroll_canvas.create_window((0, 0), window=self.doubt_show_frame, anchor="nw")

        self.doubt_show_frame.bind(
            "<Configure>",
            lambda e: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all"))
        )

        # ----- DOUBT INPUT AREA -----
        self.doubts_enter_frame = CTkFrame(
            self.frame,
            fg_color="#ffffff",
            border_color="#e5e5e5",
            border_width=1,
            corner_radius=15
        )

        self.entry = CTkEntry(
            self.doubts_enter_frame,
            width=700,
            height=50,
            placeholder_text="💬 Type your doubt here...",
            border_width=0,
            fg_color="#f1f3ff",
            corner_radius=10,
            font=("Roboto", 13)
        )
        self.entry.grid(row=0, column=0, padx=15, pady=15)

        self.send = CTkButton(
            self.doubts_enter_frame,
            text="Send",
            command=self.send_doubt,
            width=100,
            height=45,
            fg_color=colors.base_color,
            hover_color="#3a5deb",
            font=("Roboto", 13, "bold"),
            corner_radius=8
        )
        self.send.grid(row=0, column=1, padx=10, pady=15)

        self.doubts_enter_frame.pack(side=BOTTOM, fill="x", pady=10, padx=10)

    # ----- FUNCTIONALITY -----
    def send_doubt(self):
        doubt = self.entry.get()
        if doubt.strip() == "":
            return
        user_id = self.scholar_record["scholar id"]
        doubts_logic.insert_doubt(user_id, doubt)

        user_name, role = doubts_logic.get_username_role(user_id)
        self.display_doubt_card(user_id, user_name, role, doubt)
        self.entry.delete(0, END)

    def display_doubt_card(self, user_id, user_name, role, doubt):
        doubt_frame = CTkFrame(
            self.doubt_show_frame,
            fg_color="#ffffff",
            corner_radius=10,
            border_color="#dfe3f0",
            border_width=1
        )

        user_details_label = CTkLabel(
            doubt_frame,
            text=f"🧑 {user_name} ({role})",
            font=("Roboto", 13, "bold"),
            text_color="#3b3b3b"
        )
        user_details_label.grid(row=0, column=0, sticky="w", padx=15, pady=(10, 5))

        doubt_label = CTkLabel(
            doubt_frame,
            text=f"❝ {doubt} ❞",
            wraplength=700,
            justify="left",
            font=("Roboto", 12),
            text_color="#333333"
        )
        doubt_label.grid(row=1, column=0, sticky="w", padx=15, pady=(0, 10))

        doubt_frame.pack(padx=20, pady=10, anchor="w", fill="x")

    # ----- PACK / UNPACK -----
    def pack(self, padx=0, pady=0):
        self.frame.pack(padx=padx, pady=pady, fill="both", expand=True)

    def pack_forget(self):
        self.frame.pack_forget()


# ----- TEST MODE -----
if __name__ == "__main__":
    root = CTk()
    root.geometry("950x700")
    frame = AskDoubtPage(root, {"student id": 1})
    frame.pack()
    root.mainloop()