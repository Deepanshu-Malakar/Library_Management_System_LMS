import customtkinter as ctk

class Colors:
    def __init__(self):
        self.purple = "#613287"
        self.purple = "#375C98"
        self.white = "#FFFFFF"
        self.light_bg = "#F3F3F3"  # subtle background for top sections
        self.dark_bg = "#2E2E2E"   # dark grey for bottom half
        self.black = "#000000"

class HelpSupportWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("light")
        self.title("Help & Support - Library Management System")
        self.geometry("950x800")
        colors = Colors()

        # ---------- MAIN SCROLLABLE FRAME ----------
        self.scrollable = ctk.CTkScrollableFrame(
            self,
            fg_color=colors.white,
            corner_radius=0
        )
        self.scrollable.pack(padx=0, pady=0, fill="both", expand=True)

        # ---------- HEADER ----------
        title = ctk.CTkLabel(
            self.scrollable,
            text="📚 Library Management System – Help & Support",
            font=("Roboto", 26, "bold"),
            text_color=colors.purple
        )
        title.pack(pady=(15, 10))

        subtitle = ctk.CTkLabel(
            self.scrollable,
            text="Find everything you need to use your account efficiently.",
            font=("Roboto", 14),
            text_color=colors.black
        )
        subtitle.pack(pady=(0, 25))

        # ---------- TOP SECTIONS ----------
        self.add_section("📘 About the System",
            "Welcome to the Library Management System (LMS)!\n"
            "Here, Students, Scholars, and Librarians can create accounts, \n"
            "manage their library activities, and access digital services seamlessly.\n"
            "This page helps you understand how to register, log in, and manage your account."
        )

        self.add_account_section()

        self.add_section("💻 Using the Website",
            "Once logged in:\n"
            "- Students can browse, borrow, and return books.\n"
            "- Scholars can manage research materials and view advanced collections.\n"
            "- Librarians can manage users, books, and transaction records.\n\n"
            "Everything is accessible from your dashboard."
        )

        # ---------- BOTTOM HALF ----------
        bottom_frame = ctk.CTkFrame(
            self.scrollable,
            fg_color=colors.dark_bg,
            corner_radius=0
        )
        bottom_frame.pack(pady=(30, 30), fill="both", expand=True)

        bottom_title = ctk.CTkLabel(
            bottom_frame,
            text="Support & Assistance",
            font=("Roboto", 30, "bold"),
            text_color=colors.white
        )
        bottom_title.pack(pady=(20, 15))

        columns_frame = ctk.CTkFrame(
            bottom_frame,
            fg_color=colors.dark_bg,
            corner_radius=0
        )
        columns_frame.pack(fill="x", padx=25)

        # --- Three columns ---
        self.add_dark_column(columns_frame, "🛠️ Troubleshooting", 
            "Passwords not matching\nPhone number invalid\nDOB format: DD/MM/YYYY\nForm won’t submit\nApp not responding"
        ).grid(row=0, column=0, padx=10, sticky="nsew")

        self.add_dark_column(columns_frame, "❓ FAQs", "", is_faq=True).grid(row=0, column=1, padx=10, sticky="nsew")

        self.add_dark_column(columns_frame, "📞 Contact Us", 
            "Email: library@iiitdmk.in\nPhone: +91 76867-76858\nWorking Hours: Mon–Sat | 9 AM – 5 PM"
        ).grid(row=0, column=2, padx=10, sticky="nsew")

        columns_frame.grid_columnconfigure(0, weight=1)
        columns_frame.grid_columnconfigure(1, weight=1)
        columns_frame.grid_columnconfigure(2, weight=1)

    # ---------- FUNCTIONS ----------
    def add_section(self, title, content):
        colors = Colors()
        section = ctk.CTkFrame(self.scrollable, fg_color=colors.light_bg, corner_radius=12)
        section.pack(pady=10, padx=25, fill="x", expand=True)

        header = ctk.CTkLabel(section, text=title, font=("Roboto", 18, "bold"),
                              text_color=colors.purple, anchor="w")
        header.pack(padx=15, pady=(10,5), anchor="w")

        body = ctk.CTkLabel(section, text=content, font=("Roboto", 13),
                            justify="left", wraplength=800, text_color=colors.black)
        body.pack(padx=15, pady=(0,15), anchor="w")

    def add_account_section(self):
        colors = Colors()
        section = ctk.CTkFrame(self.scrollable, fg_color=colors.light_bg, corner_radius=12)
        section.pack(pady=10, padx=25, fill="x", expand=True)

        header = ctk.CTkLabel(section, text="👤 Creating an Account", font=("Roboto", 18, "bold"),
                              text_color=colors.purple, anchor="w")
        header.pack(padx=15, pady=(10,5), anchor="w")

        # ---------- ACCOUNT STEPS WITH EMOJIS (NO NUMBERS) ----------
        self.add_emoji_step(section, "👤", "Student Signup – Enter Student ID, Name, Department, Enrollment Year.\nUse valid email & 10-digit phone. Password must be 8+ chars with letters & numbers.")
        self.add_emoji_step(section, "📚", "Scholar Signup – Similar to students but includes Research Topic & Enrollment Date.")
        self.add_emoji_step(section, "🛎️", "Librarian Signup – Requires Employee ID, Job Title & Shift Timing.\nLibrarians manage books, track issued books, and oversee users.")
        self.add_emoji_step(section, "✅", "You will see 'Signup Successful' message in green text on the bottom of the page once the registration is complete")

    def add_emoji_step(self, parent, emoji, text):
        frame = ctk.CTkFrame(parent, fg_color=Colors().light_bg, corner_radius=0)
        frame.pack(anchor="w", padx=15, pady=3, fill="x")
        emoji_label = ctk.CTkLabel(frame, text=emoji, font=("Roboto",13))
        emoji_label.pack(side="left", padx=(0,5))
        text_label = ctk.CTkLabel(frame, text=text, font=("Roboto",13),
                                   text_color=Colors().black, justify="left", wraplength=800)
        text_label.pack(side="left")

    def add_dark_column(self, parent, title, content, is_faq=False):
        colors = Colors()
        frame = ctk.CTkFrame(parent, fg_color=colors.dark_bg, corner_radius=0)
        header = ctk.CTkLabel(frame, text=title, font=("Roboto", 16, "bold"),
                              text_color=colors.white, anchor="w")
        header.pack(pady=(10,5), padx=5, anchor="w")

        if is_faq:
            faqs = {
                "Can I change my password later?": "Yes. Go to My Account > Change Password.",
                "Mistake in DOB?": "Yes. You can edit your profile in the dashboard.",
                "Forget password?": "Use Forgot Password on the login page to reset via email.",
                "Can librarians see user details?": "Yes, but only limited info needed for managing records.",
                "Why did my registration fail?": "Likely due to missing fields, invalid email, or weak password."
            }
            for q,a in faqs.items():
                self.add_faq(frame, q, a)
        else:
            body = ctk.CTkLabel(frame, text=content, font=("Roboto", 12),
                                justify="left", wraplength=250, text_color=colors.white)
            body.pack(pady=(0,10), padx=5, anchor="w")
        return frame

    def add_faq(self, parent, question, answer):
        colors = Colors()
        container = ctk.CTkFrame(parent, fg_color=colors.dark_bg, corner_radius=0)
        container.pack(fill="x", padx=5, pady=2)

        ans_label = ctk.CTkLabel(container, text=answer, font=("Roboto",12),
                                 text_color=colors.white, justify="left", wraplength=240)
        ans_label.pack_forget()  # initially hidden

        def toggle():
            if ans_label.winfo_viewable():
                ans_label.pack_forget()
                btn.configure(text=f"+ {question}")
            else:
                ans_label.pack(padx=10, pady=(0,5), anchor="w")
                btn.configure(text=f"- {question}")

        btn = ctk.CTkButton(container, text=f"+ {question}", font=("Roboto",12),
                             fg_color="#444444", hover_color="#555555",
                             command=toggle, anchor="w")
        btn.pack(fill="x")

if __name__ == "__main__":
    app = HelpSupportWindow()
    app.mainloop()
