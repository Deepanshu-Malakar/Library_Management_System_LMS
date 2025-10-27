from tkinter import *
from customtkinter import *
from PIL import Image
from backend import reports

class Page:
    def __init__(self,master,sidebar_control):
        self.master = master
        self.sidebar_control = sidebar_control
        self.frame = CTkFrame(self.master,
                              fg_color="#93ecec",
                              corner_radius=0)
        ReportsDashboard(self.frame)
        
    def pack(self):
        self.frame.pack(padx=0,pady=0,fill="both",expand=True)

    def pack_forget(self):
        self.frame.pack_forget()




from customtkinter import *
from PIL import Image
import reports  # your reports.py file


class ReportsDashboard(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#F5F6FA")  # light background
        self.pack(fill="both", expand=True)

        # 🎨 Colors
        self.sidebar_color = "#292B34"
        self.primary = "#1F6FEB"
        self.secondary = "#FFFFFF"
        self.accent = "#1F6FEB"
        self.text_color = "#2C2C2C"
        self.subtext_color = "#555555"

        self.create_ui()

    # ------------------------------------------------
    # 🧭 MAIN UI LAYOUT
    # ------------------------------------------------
    def create_ui(self):
        # Sidebar
        self.sidebar = CTkFrame(self, width=240, fg_color=self.sidebar_color, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        CTkLabel(
            self.sidebar,
            text="📊 Reports",
            font=("Roboto", 22, "bold"),
            text_color="white"
        ).pack(pady=25)

        # Sidebar Buttons
        buttons = [
            ("Available Books", "📗", self.show_available_books),
            ("Most Issued Books", "🔥", self.show_most_issued_books),
            ("User Counts", "👥", self.show_user_counts),
            ("Overdue Books", "⏰", self.show_overdue_books),
            ("System Summary", "📘", self.show_system_summary),
            ("Recent Notifications", "🔔", self.show_recent_notifications)
        ]

        for name, icon, command in buttons:
            btn = CTkButton(
                self.sidebar,
                text=f"{icon}  {name}",
                command=command,
                font=("Roboto", 15, "bold"),
                fg_color="transparent",
                hover_color="#383A45",
                text_color="white",
                corner_radius=8,
                anchor="w",
                height=40,
            )
            btn.pack(fill="x", padx=15, pady=3)

        # Main display
        self.display_frame = CTkScrollableFrame(
            self,
            fg_color=self.secondary,
            corner_radius=12,
            border_width=1,
            border_color="#E0E0E0"
        )
        self.display_frame.pack(side="right", fill="both", expand=True, padx=15, pady=15)

        self.title_label = CTkLabel(
            self.display_frame,
            text="Select a report from the left panel.",
            font=("Roboto", 20, "bold"),
            text_color=self.text_color
        )
        self.title_label.pack(pady=20)

    # ------------------------------------------------
    # 🧹 HELPERS
    # ------------------------------------------------
    def clear_display(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

    def render_card(self, title, value):
        """Display summary metric cards (for system summary)"""
        card = CTkFrame(self.display_frame, fg_color="#FFFFFF", corner_radius=12)
        card.pack(pady=10, padx=15, fill="x", ipadx=5, ipady=5)
        CTkLabel(card, text=title, font=("Roboto", 16, "bold"), text_color=self.primary).pack(anchor="w", padx=15, pady=5)
        CTkLabel(card, text=value, font=("Roboto", 18), text_color=self.text_color).pack(anchor="w", padx=15, pady=(0, 10))

    def render_table(self, headers, rows):
        """Display data in a table format"""
        if not rows:
            CTkLabel(self.display_frame, text="No data found.", font=("Roboto", 14, "italic"), text_color="#777777").pack(pady=10)
            return

        # Header row
        header_frame = CTkFrame(self.display_frame, fg_color="#E9E9E9", corner_radius=8)
        header_frame.pack(fill="x", pady=(10, 0))

        for h in headers:
            CTkLabel(header_frame, text=h, font=("Roboto", 13, "bold"), text_color=self.primary, width=20, anchor="w").pack(side="left", padx=10)

        # Data rows
        for i, row in enumerate(rows):
            bg = "#FFFFFF" if i % 2 == 0 else "#F5F6FA"
            row_frame = CTkFrame(self.display_frame, fg_color=bg)
            row_frame.pack(fill="x", pady=1)

            for value in row:
                CTkLabel(row_frame, text=str(value), font=("Roboto", 13), text_color=self.text_color, width=20, anchor="w").pack(side="left", padx=10)

    # ------------------------------------------------
    # 📈 REPORT HANDLERS
    # ------------------------------------------------
    def show_available_books(self):
        self.clear_display()
        CTkLabel(self.display_frame, text="📗 Available Books", font=("Roboto", 22, "bold"), text_color=self.primary).pack(pady=10)
        data = reports.report_available_books()
        self.render_table(["Book ID", "Title", "Author", "Edition", "Category", "Available"], data)

    def show_most_issued_books(self):
        self.clear_display()
        CTkLabel(self.display_frame, text="🔥 Most Issued Books", font=("Roboto", 22, "bold"), text_color=self.primary).pack(pady=10)
        data = reports.report_most_issued_books()
        self.render_table(["Title", "Author", "Issue Count"], data)

    def show_user_counts(self):
        self.clear_display()
        CTkLabel(self.display_frame, text="👥 User Counts", font=("Roboto", 22, "bold"), text_color=self.primary).pack(pady=10)
        data = reports.report_user_counts()
        self.render_table(["Role", "Total"], data)

    def show_overdue_books(self):
        self.clear_display()
        CTkLabel(self.display_frame, text="⏰ Overdue Books", font=("Roboto", 22, "bold"), text_color=self.primary).pack(pady=10)
        data = reports.report_overdue_books()
        self.render_table(["User ID", "Book Title", "Issue Date", "Return Date"], data)

    def show_system_summary(self):
        self.clear_display()
        CTkLabel(self.display_frame, text="📘 System Summary", font=("Roboto", 22, "bold"), text_color=self.primary).pack(pady=10)
        summary = reports.report_system_summary()

        for key, val in summary.items():
            self.render_card(key.replace("_", " ").title(), val)

    def show_recent_notifications(self):
        self.clear_display()
        CTkLabel(self.display_frame, text="🔔 Recent Notifications", font=("Roboto", 22, "bold"), text_color=self.primary).pack(pady=10)
        data = reports.report_recent_notifications()
        self.render_table(["User ID", "Message", "Date-Time"], data)


# ------------------------------------------------
# 🚀 LAUNCHER
# ------------------------------------------------
if __name__ == "__main__":
    app = CTk()
    app.title("📚 Library Reports Dashboard")
    app.geometry("1200x700")
    app._set_appearance_mode("light")  # Light Mode Enabled

    ReportsDashboard(app)
    app.mainloop()
