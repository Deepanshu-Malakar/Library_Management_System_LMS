from tkinter import *
from customtkinter import *
from backend import notifications_logic


class Notification:
    def __init__(self, master, user_id):
        self.master = master
        self.user_id = user_id
        self.create_notifications()

    def create_notifications(self):
        # Clear previous notifications (if any)
        for widget in self.master.winfo_children():
            widget.destroy()

        # Fetch latest 4 notifications
        self.notifications = notifications_logic.get_latest_notifications(self.user_id)

        # If no notifications
        if not self.notifications:
            CTkLabel(self.master, text="No notifications yet.", font=("Arial", 13)).pack(pady=10)
            return

        # Create frames for each notification
        for msg, timestamp in self.notifications:
            formatted_time = timestamp.strftime("%d-%m-%Y %H:%M:%S")

            frame = CTkFrame(self.master, corner_radius=5,border_width=1,fg_color="#f3f2f2")
            frame.pack(fill="x", pady=5, padx=10)

            CTkLabel(frame, text=formatted_time, font=("Arial", 11, "italic"), text_color="gray").pack(anchor="w", padx=10, pady=(5, 0))
            CTkLabel(frame, text=msg, font=("Arial", 13), wraplength=250, justify="left").pack(anchor="w", padx=10, pady=5)

    def refresh_notification(self):
        """Clear all existing notifications and redraw updated ones."""
        # Simply re-run the creation logic
        self.create_notifications()

