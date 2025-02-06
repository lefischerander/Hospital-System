from tkinter import Tk, Button, messagebox, Label, Entry, Toplevel, Frame, LEFT, RIGHT
import getpass
from test_class_login import AuthSystem
import sys
from test_class_actions import Actions
from user_test import User
from actions_ui import ActionsUI
global_username = None
global_password = None

class MainUI:
    def home_action():
        root.deiconify()

    def logout():
        global global_username
        auth = AuthSystem()
        auth.logout(global_username)
        global_username = None
        MainUI.home_action()

    def login_action():
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
            global global_username
            username = username_entry.get()
            password = password_entry.get()
            global_username = username
            messagebox.showinfo("Globalusername", f"Username: {username}")
            hash_password = User.hash_password(password)
            auth.login(username, hash_password)
            if auth.logged_in == False:
                messagebox.showerror("Login Error", "Invalid username or password")
                global_username = None
                MainUI.login_action()
                login_window.destroy()
            else:
                user_role = auth.users[0][2]
                if user_role == 'Doctor':
                    ActionsUI.doktor_actions()
                    login_window.destroy()
                elif user_role == 'Patient':
                    ActionsUI.patient_actions()
                    login_window.destroy()
                elif user_role == 'admin': 
                    ActionsUI.admin_actions()
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
            username = username_entry.get()
            old_password = password_entry.get()
            new_password = new_password_entry.get()
            confirm_new_password = confirm_new_password_entry.get()
            hash_password = User.hash_password(old_password)
            auth.reset_password(username, hash_password)
            messagebox.showinfo("Reset Password Info", f"Username: {username}\nPassword: {old_password}")
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

root = Tk()
root.title("My Tkinter App")
root.geometry("800x600")

login_button = Button(root, text="Login", command=MainUI.login_action)
login_button.pack(pady=10)

reset_password_button = Button(root, text="Reset Password", command=MainUI.reset_password_action)
reset_password_button.pack(pady=10)

exit_button = Button(root, text="Exit", command=MainUI.exit_action)
exit_button.pack(pady=10)

root.mainloop()