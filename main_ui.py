# from test_class_actions import Actions
from tkinter import Tk, Button, messagebox, Label, Entry, Toplevel, Frame, RIGHT
from test_class_login import AuthSystem
from user_test import User
from actions_ui import ActionsUI
from helppage import HelpPage

global_username = None
global_password = None


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
        messagebox.showinfo("Globalusername", f"Username: {global_username}")
        hash_password = User.hash_password(password)
        auth.login(username, hash_password)
        if not auth.logged_in:
            messagebox.showerror("Login Error", "Invalid username or password")
            global_username = None
            login_action()
            login_window.destroy()
        else:
            user_role = auth.users[0][4]
            if user_role == "Doctor":
                ActionsUI.doktor_actions(global_username)
                login_window.destroy()
            elif user_role == "Patient":
                ActionsUI.patient_actions(global_username)
                login_window.destroy()
            elif user_role == "admin":
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


def reset_password_action():
    """Create a reset password window to reset the user's password."""
    root.withdraw()
    auth = AuthSystem()
    reset_password_window = Toplevel(root)
    reset_password_window.title("Reset Password")

    Label(reset_password_window, text="Username:").pack(pady=5)
    username_entry = Entry(reset_password_window)
    username_entry.pack(pady=5)

    Label(reset_password_window, text="Old Password:").pack(pady=5)
    password_entry = Entry(reset_password_window, show="*")
    password_entry.pack(pady=5)

    Label(reset_password_window, text="New Password:").pack(pady=5)
    new_password_entry = Entry(reset_password_window, show="*")
    new_password_entry.pack(pady=5)

    Label(reset_password_window, text="Confirm New Password:").pack(pady=5)
    confirm_new_password_entry = Entry(reset_password_window, show="*")
    confirm_new_password_entry.pack(pady=5)

    def submit_reset_password():
        """Submit the reset password form and reset the user's password."""
        username = username_entry.get()
        old_password = password_entry.get()
        new_password = new_password_entry.get()
        confirm_new_password = confirm_new_password_entry.get()
        hash_password = User.hash_password(old_password)
        auth.reset_password(username, hash_password, new_password, confirm_new_password)
        messagebox.showinfo(
            "Reset Password Info", f"Username: {username}\nPassword: {old_password}"
        )
        reset_password_window.destroy()
        root.deiconify()

    def cancel_reset_password():
        reset_password_window.destroy()
        root.deiconify()

    button_frame = Frame(reset_password_window)
    button_frame.pack(pady=10)

    submit_button = Button(button_frame, text="Submit", command=submit_reset_password)
    submit_button.pack(side=RIGHT, padx=5)

    cancel_button = Button(button_frame, text="Cancel", command=cancel_reset_password)
    cancel_button.pack(side=RIGHT, padx=5)


def exit_action():
    root.quit()


# Main program
root = Tk()
root.title("My Tkinter App")
root.geometry("800x600")

login_button = Button(root, text="Login", command=login_action)
login_button.pack(pady=10)

reset_password_button = Button(
    root, text="Reset Password", command=reset_password_action
)
reset_password_button.pack(pady=10)

exit_button = Button(root, text="Exit", command=exit_action)
exit_button.pack(pady=10)

help_button = Button(root, text="Help", command=HelpPage.help_page)
help_button.pack(pady=10)

root.mainloop()
