from tkinter import *
from customtkinter import *
from PIL import Image
from AI import ai

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

        # Chat area (scrollable)
        self.chat_canvas = CTkCanvas(self.frame, bg="#f5f7fb", highlightthickness=0)
        self.scrollbar = CTkScrollbar(self.frame, orientation="vertical", command=self.chat_canvas.yview)
        self.scrollable_frame = CTkFrame(self.chat_canvas, fg_color="#f5f7fb")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.chat_canvas.configure(
                scrollregion=self.chat_canvas.bbox("all")
            )
        )

        self.chat_window = self.chat_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.chat_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.chat_canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=(20, 0), pady=(0, 10))
        self.scrollbar.pack(side=RIGHT, fill=Y, padx=(0, 20), pady=(0, 10))

        # User input area
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

    def send_query(self):
        query = self.user_entry.get().strip()
        if not query:
            return
        
        # Display user message
        user_message_frame = CTkFrame(self.scrollable_frame, fg_color="#d7ebff", corner_radius=15)
        user_label = CTkLabel(user_message_frame, text=query, justify="right", wraplength=600, text_color="#000000")
        user_label.pack(padx=10, pady=10)
        user_message_frame.pack(anchor="e", padx=20, pady=5)

        self.user_entry.delete(0, END)

        # Display AI placeholder
        ai_message_frame = CTkFrame(self.scrollable_frame, fg_color="#ffffff", corner_radius=15)
        ai_label = CTkLabel(ai_message_frame, text="💭 Thinking...", justify="left", wraplength=600, text_color="#444444")
        ai_label.pack(padx=10, pady=10)
        ai_message_frame.pack(anchor="w", padx=20, pady=5)

        # Update UI before fetching response
        self.frame.update_idletasks()

        # Generate AI response
        prompt = f"You are a friendly professor explaining to a college student. Keep your response simple, clear, and slightly conversational. Donot write long answers. Question: {query}"
        answer = ai.query(prompt)

        ai_label.configure(text=answer)

        # Auto-scroll to bottom
        self.chat_canvas.yview_moveto(1)

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
