import customtkinter as ctk


class Colors:
    def __init__(self):
        self.primary = "#375C98"      # Calming blue
        self.accent = "#5A9BD4"       # Light blue for highlights
        self.light_bg = "#F8FAFC"     # soft background
        self.card_bg = "#FFFFFF"      # white for cards
        self.dark_bg = "#1E1E2F"      # dark section background
        self.text_dark = "#222222"
        self.text_light = "#FFFFFF"

class Page:
    def __init__(self,master,sidebar_control,faculty_record):
        self.faculty_record = faculty_record
        self.master = master
        self.master = master
        self.colors = Colors()
        self.sidebar_control = sidebar_control
        # ---------- MAIN FRAME ----------
        self.frame = ctk.CTkFrame(master, fg_color=self.colors.light_bg)
        self.scrollable = ctk.CTkScrollableFrame(
            self.frame,
            fg_color=self.colors.light_bg,
            corner_radius=0
        )
        self.scrollable.pack(fill="both", expand=True, padx=0, pady=0)

        # ---------- HEADER ----------
        self._add_header()

        # ---------- MAIN CONTENT ----------
        self._add_section(
            "📘 About the System",
            "Welcome to the Library Management System (LMS)!\n"
            "Students, Scholars, and Librarians can create accounts, manage books, "
            "and track their activities seamlessly.\n"
            "This guide will help you understand how to register, log in, and use key features."
        )

        self._add_account_section()

        self._add_section(
            "💻 Using the Dashboard",
            "After login:\n"
            "- Students can browse and reserve books.\n"
            "- Scholars can manage research references.\n"
            "- Librarians can oversee users and book inventories.\n\n"
            "Everything is designed for simplicity and efficiency."
        )

        # ---------- SUPPORT AREA ----------
        self._add_support_section()

    # ==============================================================
    # =============== UI COMPONENTS ================================
    # ==============================================================

    def _add_header(self):
        title = ctk.CTkLabel(
            self.scrollable,
            text="📚 Help & Support Center",
            font=("Segoe UI Semibold", 28),
            text_color=self.colors.primary
        )
        title.pack(pady=(25, 8))

        subtitle = ctk.CTkLabel(
            self.scrollable,
            text="Your guide to using the Library Management System effectively",
            font=("Segoe UI", 14),
            text_color="#555555"
        )
        subtitle.pack(pady=(0, 25))

    def _add_section(self, title, content):
        section = ctk.CTkFrame(
            self.scrollable,
            fg_color=self.colors.card_bg,
            corner_radius=12
        )
        section.pack(pady=12, padx=25, fill="x")

        header = ctk.CTkLabel(
            section,
            text=title,
            font=("Segoe UI Semibold", 18),
            text_color=self.colors.primary,
            anchor="w"
        )
        header.pack(padx=20, pady=(15, 5), anchor="w")

        body = ctk.CTkLabel(
            section,
            text=content,
            font=("Segoe UI", 13),
            text_color=self.colors.text_dark,
            justify="left",
            wraplength=800
        )
        body.pack(padx=20, pady=(0, 15), anchor="w")

    def _add_account_section(self):
        section = ctk.CTkFrame(
            self.scrollable,
            fg_color=self.colors.card_bg,
            corner_radius=12
        )
        section.pack(pady=12, padx=25, fill="x")

        header = ctk.CTkLabel(
            section,
            text="👤 Creating an Account",
            font=("Segoe UI Semibold", 18),
            text_color=self.colors.primary,
            anchor="w"
        )
        header.pack(padx=20, pady=(15, 5), anchor="w")

        steps = [
            ("👤", "Student Signup – Enter Student ID, Name, Department, and Enrollment Year."),
            ("📚", "Scholar Signup – Includes Research Topic and Enrollment Date."),
            ("🛎️", "Librarian Signup – Requires Employee ID and Shift Details."),
            ("✅", "Once successful, you’ll see a green 'Signup Successful' message below.")
        ]

        for emoji, text in steps:
            row = ctk.CTkFrame(section, fg_color=self.colors.card_bg)
            row.pack(anchor="w", fill="x", padx=20, pady=3)
            ctk.CTkLabel(row, text=emoji, font=("Segoe UI", 13)).pack(side="left", padx=(0, 8))
            ctk.CTkLabel(
                row,
                text=text,
                font=("Segoe UI", 13),
                text_color=self.colors.text_dark,
                justify="left",
                wraplength=780
            ).pack(side="left")

    def _add_support_section(self):
        bottom = ctk.CTkFrame(
            self.scrollable,
            fg_color=self.colors.dark_bg,
            corner_radius=0
        )
        bottom.pack(pady=(30, 0), fill="both", expand=True)

        header = ctk.CTkLabel(
            bottom,
            text="Support & Assistance",
            font=("Segoe UI Semibold", 26),
            text_color=self.colors.text_light
        )
        header.pack(pady=(25, 15))

        columns = ctk.CTkFrame(bottom, fg_color=self.colors.dark_bg)
        columns.pack(fill="x", padx=30, pady=15)

        # Columns
        self._add_dark_column(columns, "🛠️ Troubleshooting",
                              "• Password not matching\n"
                              "• Invalid phone number\n"
                              "• DOB format: DD/MM/YYYY\n"
                              "• Form not submitting\n"
                              "• App freezing").grid(row=0, column=0, padx=10, sticky="nsew")

        self._add_dark_column(columns, "❓ FAQs", "", is_faq=True).grid(row=0, column=1, padx=10, sticky="nsew")

        self._add_dark_column(columns, "📞 Contact Us",
                              "Email: library@iiitdmk.in\n"
                              "Phone: +91 76867-76858\n"
                              "Hours: Mon–Sat | 9 AM – 5 PM").grid(row=0, column=2, padx=10, sticky="nsew")

        columns.grid_columnconfigure((0, 1, 2), weight=1)

    def _add_dark_column(self, parent, title, content, is_faq=False):
        colors = self.colors
        frame = ctk.CTkFrame(parent, fg_color=colors.dark_bg)
        ctk.CTkLabel(
            frame,
            text=title,
            font=("Segoe UI Semibold", 16),
            text_color=colors.text_light,
            anchor="w"
        ).pack(pady=(10, 5), padx=10, anchor="w")

        if is_faq:
            faqs = {
                "Can I change my password later?": "Yes. Go to My Account > Change Password.",
                "Mistake in DOB?": "Edit your profile in the dashboard.",
                "Forgot password?": "Use the Forgot Password link to reset via email.",
                "Can librarians view user info?": "Yes, but only necessary details.",
                "Why did my registration fail?": "Missing fields, invalid email, or weak password."
            }
            for q, a in faqs.items():
                self._add_faq(frame, q, a)
        else:
            ctk.CTkLabel(
                frame,
                text=content,
                font=("Segoe UI", 13),
                text_color=colors.text_light,
                justify="left",
                wraplength=250
            ).pack(pady=(0, 10), padx=10, anchor="w")
        return frame

    def _add_faq(self, parent, question, answer):
        colors = self.colors
        container = ctk.CTkFrame(parent, fg_color=colors.dark_bg)
        container.pack(fill="x", padx=5, pady=2)

        ans_label = ctk.CTkLabel(
            container,
            text=answer,
            font=("Segoe UI", 12),
            text_color="#EAEAEA",
            justify="left",
            wraplength=250
        )
        ans_label.pack_forget()

        def toggle():
            if ans_label.winfo_viewable():
                ans_label.pack_forget()
                btn.configure(text=f"➕ {question}")
            else:
                ans_label.pack(padx=15, pady=(0, 5), anchor="w")
                btn.configure(text=f"➖ {question}")

        btn = ctk.CTkButton(
            container,
            text=f"➕ {question}",
            font=("Segoe UI", 12),
            fg_color="#2F2F40",
            hover_color="#3A3A50",
            text_color="white",
            corner_radius=6,
            anchor="w",
            command=toggle
        )
        btn.pack(fill="x")
        
    def pack(self):
        self.frame.pack(padx=0,pady=0,fill="both",expand=True)

    def pack_forget(self):
        self.frame.pack_forget()