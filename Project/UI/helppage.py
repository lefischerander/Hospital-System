from tkinter import Tk, Button, Label
from Database.database_service import User_service


class HelpPage:
    def help_page_from_home():
        """Create a help page for the application."""
        help_window = Tk()
        help_window.title("Help Page")
        help_window.geometry("800x600")

        """Get the admin email from the database"""
        us = User_service()
        admin_email = us.get_admin_email()

        """The help page text"""
        Label(
            help_window, 
            text="Help Page", 
            font=("Arial", 20)
        ).pack(pady=10)
        Label(
            help_window, 
            text="Welcome to the Help Page", 
            font=("Arial", 20)
        ).pack(pady=10)
        Label(
            help_window,
            text="This is the help page for the Hospital Management System",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to Login, please click on the 'Login' button and provide the necessary information in the given fields.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to Reset your Password, please click on the 'Reset Password' button and provide the necessary information in the given fields.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to Exit the application, please click on the 'Exit' button or close the window.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text=f"If you need more help, please contact the system administrator at: {admin_email}",
            font=("Arial", 15),
        ).pack(pady=10)
        Button(
            help_window, text="Close", font=("Arial", 15), command=help_window.destroy
        ).pack(pady=10)
        help_window.mainloop()

    def help_page_from_actions_doctor():
        """Create a help page for the application. Specifically for doctors."""
        help_window = Tk()
        help_window.title("Doctor Help Page")
        help_window.geometry("800x600")

        """Get the admin email from the database"""
        us = User_service()
        admin_email = us.get_admin_email()

        """The help page text"""
        Label(
            help_window, 
            text="Help Page", 
            font=("Arial", 20)
        ).pack(pady=10)
        Label(
            help_window, text="Welcome to the Help Page for Doctors", font=("Arial", 20)
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to view the data of a patient, please click on the 'View Patients Data' button.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to analyze patients data, please click on the 'View Patient Analysis' button.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to create a Diagnosis Report, please click on the 'Create Diagnosis Report' button.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to view the patients age distribution, please click on the 'Patient Age Distribution' button.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to view the average length of stay of patients, please click on the 'Average Length of Hospital Stays' button.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to view your profile, please click on the 'View Profile' button.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to change your password, please click on the 'Change Password' button.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to Logout, please click on the 'Logout' button or close the window.",
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

    def help_page_from_actions_patients():
        """Create a help page for the application. Specifically for patients."""
        help_window = Tk()
        help_window.title("Doctor Help Page")
        help_window.geometry("800x600")

        """Get the admin email from the database"""
        us = User_service()
        admin_email = us.get_admin_email()

        """The help page text"""
        Label(
            help_window, 
            text="Help Page", 
            font=("Arial", 20)
        ).pack(pady=10)
        Label(
            help_window,
            text="Welcome to the Help Page for Patients",
            font=("Arial", 20),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to view your diagnosis, please click on the 'View your Diagnosis' button.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to view your profile, please click on the 'View Profile' button.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to change your password, please click on the 'Change Password' button.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to Logout, please click on the 'Logout' button or close the window.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text=f"If you need help, please contact the system administrator at: {admin_email}",
            font=("Arial", 15),
        ).pack(pady=10)
        Button(
            help_window, 
            text="Close", 
            font=("Arial", 15), 
            command=help_window.destroy
        ).pack(pady=10)
        help_window.mainloop()

    def help_page_from_actions_admin():
        """Create a help page for the application. Specifically for admins."""
        help_window = Tk()
        help_window.title("Doctor Help Page")
        help_window.geometry("800x600")

        """Get the admin email from the database"""
        us = User_service()
        admin_email = us.get_admin_email()

        """The help page text"""
        Label(
            help_window, 
            text="Help Page", 
            font=("Arial", 20)
        ).pack(pady=10)
        Label(
            help_window, 
            text="Welcome to the Help Page for Admins", 
            font=("Arial", 20)
        ).pack(pady=10)
        Label(
            help_window, 
            text="What are you doing here?", 
            font=("Arial", 15)
        ).pack(pady=10)
        Label(
            help_window,
            text="You are the admin, you know everything!",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window, 
            text="Do you really need help?", 
            font=("Arial", 15)
        ).pack(pady=10)
        Label(
            help_window, 
            text="Are you bored?", 
            font=("Arial", 15)
        ).pack(pady=10)
        Label(
            help_window,
            text="I guess you can click on the 'Close' button now.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window, 
            text="Are you still here?", 
            font=("Arial", 15)
        ).pack(pady=10)
        Label(
            help_window,
            text="Ok, I will stop now. Here is your help page.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to change your password, please click on the 'Change Password' button.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="If you want to Logout, please click on the 'Logout' button or close the window.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="What you don't even know the email of the system administrator?",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text="I don't even know how you managed to become an admin.",
            font=("Arial", 15),
        ).pack(pady=10)
        Label(
            help_window,
            text=f"If you need help, please contact a more competent system administrator at: {admin_email}",
            font=("Arial", 15),
        ).pack(pady=10)
        Button(
            help_window, 
            text="Close", 
            font=("Arial", 15), 
            command=help_window.destroy
        ).pack(pady=10)
        help_window.mainloop()
