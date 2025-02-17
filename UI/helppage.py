from tkinter import Tk, Button, Label
from Backend.Database.database_service import User_service


class HelpPage:
    def help_page():
        """Create a help page for the application."""
        help_window = Tk()
        help_window.title("Help Page")
        help_window.geometry("800x600")

        us = User_service()
        admin_email = us.get_admin_email()

        Label(help_window, text="Help Page", font=("Arial", 20)).pack(pady=10)
        Label(help_window, text="Welcome to the Help Page", font=("Arial", 15)).pack(
            pady=10
        )
        Label(
            help_window,
            text="This is the help page for the Hospital Management System",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text=f"If you need help, please contact the system administrator at: {admin_email}",
            font=("Arial", 15),
        ).pack(pady=10)
        Button(
            help_window, text="Close", font=("Arial", 15), command=help_window.destroy
        ).pack(pady=10)
        help_window.mainloop()
