from tkinter import Tk, Button, messagebox, Label, Entry, Toplevel, Frame, RIGHT
from Database.login import AuthSystem
from Backend.user import User
from UI.actions_ui import ActionsUI
from UI.helppage import HelpPage
import sys

global_username = None
global_password = None


def run():
    def home_action():
        root.deiconify()

    def login_action():
        """Create a login window to authenticate users."""
        global global_username, global_password
        root.withdraw()
        auth = AuthSystem()
        login_window = Toplevel(root)
        login_window.title("Login")
        login_window.geometry("300x400")

        def on_closing():
            """This method is responsible for handling the window close event"""
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                login_window.destroy()
                sys.exit()

        login_window.protocol("WM_DELETE_WINDOW", on_closing)

        Label(login_window, text="Username:").pack(pady=5)
        username_entry = Entry(login_window)
        username_entry.pack(pady=5)

        Label(login_window, text="Password:").pack(pady=5)
        password_entry = Entry(login_window, show="*")
        password_entry.pack(pady=5)

        def submit_login():
            """Submit the login form and authenticate the user."""
            global global_username
            username = username_entry.get()
            password = password_entry.get()
            global_username = username
            hash_password = User.hash_password(password)
            auth.login(username, hash_password)
            if not auth.logged_in:
                messagebox.showerror("Login Error", "Invalid username or password")
                global_username = None
                login_action()
                login_window.destroy()
            else:
                user_role = auth.users[0][2]
                if user_role == "Doctor":
                    ActionsUI.doktor_actions(global_username)
                    login_window.destroy()
                elif user_role == "Patient":
                    ActionsUI.patient_actions(global_username)
                    login_window.destroy()
                elif user_role == "Admin":
                    ActionsUI.admin_actions(global_username)
                    login_window.destroy()
                else:
                    messagebox.showerror("No role given\n")
                    root.deiconify()
                    login_window.destroy()

        def cancel_login():
            login_window.destroy()
            root.deiconify()

        button_frame = Frame(login_window)
        button_frame.pack(pady=10)

        submit_button = Button(button_frame, text="Submit", command=submit_login)
        submit_button.pack(side=RIGHT, padx=5)

        cancel_button = Button(button_frame, text="Cancel", command=cancel_login)
        cancel_button.pack(side=RIGHT, padx=5)

    def reset_password():
        """This method is responsible for changing the password of the user"""
        root.withdraw()
        auth = AuthSystem()
        change_password_window = Toplevel(root)
        change_password_window.title("Change Password")
        change_password_window.geometry("500x300")

        change_password_window.protocol("WM_DELETE_WINDOW", root.deiconify)

        Label(change_password_window, text="Username:").pack(pady=5)
        username_entry = Entry(change_password_window)
        username_entry.pack(pady=5)

        Label(change_password_window, text="Old Password:").pack(pady=5)
        password_entry = Entry(change_password_window, show="*")
        password_entry.pack(pady=5)

        Label(change_password_window, text="New Password:").pack(pady=5)
        new_password_entry = Entry(change_password_window, show="*")
        new_password_entry.pack(pady=5)

        Label(change_password_window, text="Confirm New Password:").pack(pady=5)
        confirm_new_password_entry = Entry(change_password_window, show="*")
        confirm_new_password_entry.pack(pady=5)

        def submit_change_password():
            """This method is responsible for submitting the new password"""
            username = username_entry.get()
            old_password = password_entry.get()
            new_password = new_password_entry.get()
            confirm_new_password = confirm_new_password_entry.get()
            hash_password = User.hash_password(old_password)
            if auth.reset_password(
                username, hash_password, new_password, confirm_new_password
            ):
                change_password_window.destroy()
                root.deiconify()
            else:
                reset_password()
                change_password_window.destroy()

        def cancel_change_password():
            """This method is responsible for cancelling the password change"""
            change_password_window.destroy()
            root.deiconify()

        button_frame = Frame(change_password_window)
        button_frame.pack(pady=10)

        submit_button = Button(
            button_frame, text="Submit", command=submit_change_password
        )
        submit_button.pack(side=RIGHT, padx=5)

        cancel_button = Button(
            button_frame, text="Cancel", command=cancel_change_password
        )
        cancel_button.pack(side=RIGHT, padx=5)

    def exit_action():
        root.quit()

    # Main program
    root = Tk()
    root.title("Hospital Management")
    root.geometry("800x600")

    def on_closing():
        """This method is responsible for handling the window close event"""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
            sys.exit()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    login_button = Button(root, text="Login", command=login_action)
    login_button.pack(pady=10)

    reset_password_button = Button(root, text="Reset Password", command=reset_password)
    reset_password_button.pack(pady=10)

    exit_button = Button(root, text="Exit", command=exit_action)
    exit_button.pack(pady=10)

    help_button = Button(root, text="Help", command=HelpPage.help_page_from_home)
    help_button.pack(pady=10)

    root.mainloop()
