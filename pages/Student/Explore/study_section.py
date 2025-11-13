from tkinter import *
from customtkinter import *
from PIL import Image
from AI import ai
from AI import chat_bot

class StudySectionPage:
    def __init__(self, master, student_record):
        self.student_record = student_record
        self.master = master
        set_appearance_mode("light")

        # Main frame
        self.frame = CTkFrame(self.master, fg_color="#f5f7fb")
        self.frame.pack(fill="both", expand=True)

        # Header
        self.header = CTkLabel(
            self.frame,
            text="📚 Study Assistant",
            font=("Arial Rounded MT Bold", 24),
            text_color="#333333"
        )
        self.header.pack(pady=(20, 10))

        # ----------------------- Chat Area -----------------------
        self.chat_canvas = CTkCanvas(
            self.frame, bg="#f5f7fb", highlightthickness=0
        )
        self.scrollbar = CTkScrollbar(
            self.frame, orientation="vertical", command=self.chat_canvas.yview
        )

        self.scrollable_frame = CTkFrame(self.chat_canvas, fg_color="#f5f7fb")

        self.chat_window = self.chat_canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor="nw"
        )

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.chat_canvas.configure(
                scrollregion=self.chat_canvas.bbox("all")
            )
        )

        self.chat_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.chat_canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=(20, 0), pady=(0, 10))
        self.scrollbar.pack(side=RIGHT, fill=Y, padx=(0, 20), pady=(0, 10))

        # Chat bubble width auto-adjust
        self.chat_canvas.bind("<Configure>", self.update_wraplength)

        self.current_wrap = 400  # default until resized

        # ----------------------- Input Area -----------------------
        self.user_frame = CTkFrame(self.frame, fg_color="#ffffff", corner_radius=20)
        self.user_frame.pack(side=BOTTOM, fill=X, padx=20, pady=(5, 20))

        self.user_entry = CTkEntry(
            self.user_frame,
            width=500,
            height=50,
            placeholder_text="Ask your question here...",
            corner_radius=15,
            border_color="#d1d9e6",
            border_width=1,
            font=("Arial", 14)
        )
        self.user_entry.grid(row=0, column=0, padx=(20, 10), pady=15)

        self.send_button = CTkButton(
            self.user_frame,
            text="Send",
            command=self.send_query,
            width=100,
            height=45,
            fg_color="#4e8cff",
            hover_color="#357ae8",
            corner_radius=15,
            font=("Arial Bold", 14)
        )
        self.send_button.grid(row=0, column=1, padx=10, pady=15)

    # ------------------------------------------------------------
    # Update bubble wrap length dynamically
    # ------------------------------------------------------------
    def update_wraplength(self, event):
        width = self.chat_canvas.winfo_width()
        self.current_wrap = int(width * 0.65)  # bubbles take only 65% of width

    # ------------------------------------------------------------
    # Send Query
    # ------------------------------------------------------------
    def send_query(self):
        query = self.user_entry.get().strip()
        if not query:
            return

        wrap = self.current_wrap

        # USER BUBBLE (Right)
        user_frame = CTkFrame(self.scrollable_frame, fg_color="#d7ebff", corner_radius=15)
        user_label = CTkLabel(
            user_frame,
            text=query,
            justify="left",
            wraplength=wrap,
            text_color="#000"
        )
        user_label.pack(padx=12, pady=10)
        user_frame.pack(anchor="e", padx=20, pady=6)

        self.user_entry.delete(0, END)

        # AI BUBBLE (Left)
        ai_frame = CTkFrame(self.scrollable_frame, fg_color="#ffffff", corner_radius=15)
        ai_label = CTkLabel(
            ai_frame,
            text="💭 Thinking...",
            justify="left",
            wraplength=wrap,
            text_color="#444"
        )
        ai_label.pack(padx=12, pady=10)
        ai_frame.pack(anchor="w", padx=20, pady=6)

        self.frame.update_idletasks()

        # AI response
        prompt = (
            f"You are a friendly professor explaining to a college student. "
            f"Keep your response simple, clear, and slightly conversational. "
            f"Do not write long answers. Question: {query}"
        )
        answer = chat_bot.query(prompt)

        ai_label.configure(text=answer)

        # Auto-scroll to bottom
        self.chat_canvas.after(50, lambda: self.chat_canvas.yview_moveto(1))

    # ------------------------------------------------------------
    def pack(self, padx=0, pady=0):
        self.frame.pack(padx=padx, pady=pady, fill="both", expand=True)

    def pack_forget(self):
        self.frame.pack_forget()



if __name__ == "__main__":
    root = CTk()
    root.geometry("950x700")
    page = StudySectionPage(root, 12)
    page.pack()
    root.mainloop()
