from tkinter import Tk, Button, messagebox, Label, Entry, Toplevel, Frame, LEFT, RIGHT
import getpass
from test_class_login import AuthSystem
import sys
from test_class_actions import Actions
from user_test import User
import Service_Database
from main_ui import MainUI

user_service= Service_Database.User_service()#creating an instance of the class Userservice

class ActionsUI:
     
    def doktor_actions():
        actions_window = Tk()
        actions_window.title("Doktor Actions")
        actions_window.geometry("800x600")

        print("1. View patient data")
        print("2. View your profile")
        print("3. Change Password")
        print("4. Logout")
        print()

        def view_patient_data():
            print("Patient data")
            print()

        def view_profile():
            print("Profile")

        def change_password():
            actions_window.withdraw()
            auth = AuthSystem()
            change_password_window = Toplevel(actions_window)
            change_password_window.title("Change Password")

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
                username = username_entry.get()
                old_password = password_entry.get()
                new_password = new_password_entry.get()
                confirm_new_password = confirm_new_password_entry.get()
                hash_password = User.hash_password(old_password)
                auth.reset_password(username, hash_password)
                messagebox.showinfo("Reset Password Info", f"Username: {username}\nPassword: {old_password}")
                change_password_window.destroy()
                actions_window.deiconify()

            def cancel_change_password():
                change_password_window.destroy()
                actions_window.deiconify()
            
            button_frame = Frame(change_password_window)
            button_frame.pack(pady=10)

            submit_button = Button(button_frame, text="Submit", command=submit_change_password)
            submit_button.pack(side=RIGHT, padx=5)

            cancel_button = Button(button_frame, text="Cancel", command=cancel_change_password)
            cancel_button.pack(side=RIGHT, padx=5)
        
        button_frame = Frame(actions_window)
        button_frame.pack(pady=10)

        logout_button = Button(button_frame, text="Logout", command=MainUI.logout())
        logout_button.pack(side=RIGHT, padx=5)

        patient_data = Button(button_frame, text="View patiant data", command=view_patient_data)
        patient_data.pack(side=RIGHT, padx=5)

        profile = Button(button_frame, text="View your profile", command=view_profile)
        profile.pack(side=RIGHT, padx=5)

        change_password_button = Button(button_frame, text="Change Password", command=change_password)
        change_password_button.pack(side=RIGHT, padx=5)

        


    def patient_actions():
        action_window = Tk()
        action_window.title("Patient Actions")
        action_window.geometry("800x600")

        print("1. View your profile")
        print("2. Change Password")
        print("3. Logout")
        print()

        def change_password():
            action_window.withdraw()
            auth = AuthSystem()
            change_password_window = Toplevel(action_window)
            change_password_window.title("Change Password")

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
                username = username_entry.get()
                old_password = password_entry.get()
                new_password = new_password_entry.get()
                confirm_new_password = confirm_new_password_entry.get()
                hash_password = User.hash_password(old_password)
                auth.reset_password(username, hash_password)
                messagebox.showinfo("Reset Password Info", f"Username: {username}\nPassword: {old_password}")
                change_password_window.destroy()
                action_window.deiconify()

            def cancel_change_password():
                change_password_window.destroy()
                action_window.deiconify()
            
            button_frame = Frame(change_password_window)
            button_frame.pack(pady=10)

            submit_button = Button(button_frame, text="Submit", command=submit_change_password)
            submit_button.pack(side=RIGHT, padx=5)

            cancel_button = Button(button_frame, text="Cancel", command=cancel_change_password)
            cancel_button.pack(side=RIGHT, padx=5)
        
        button_frame = Frame(action_window)
        button_frame.pack(pady=10)

        logout_button = Button(button_frame, text="Logout", command=MainUI.logout())
        logout_button.pack(side=RIGHT, padx=5)

        change_password_button = Button(button_frame, text="Change Password", command=change_password)
        change_password_button.pack(side=RIGHT, padx=5)

    def admin_actions():
        actions_window = Tk()
        actions_window.title("Actions")
        actions_window.geometry("800x600")

        print("1. View all users")
        print("2. Delete a user")
        print("3. View your profile")
        print("4. Change Password")
        print("5. Logout")
        print()

        def change_password():
            actions_window.withdraw()
            auth = AuthSystem()
            change_password_window = Toplevel(actions_window)
            change_password_window.title("Change Password")

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
                username = username_entry.get()
                old_password = password_entry.get()
                new_password = new_password_entry.get()
                confirm_new_password = confirm_new_password_entry.get()
                hash_password = User.hash_password(old_password)
                auth.reset_password(username, hash_password)
                messagebox.showinfo("Reset Password Info", f"Username: {username}\nPassword: {old_password}")
                change_password_window.destroy()
                actions_window.deiconify()

            def cancel_change_password():
                change_password_window.destroy()
                actions_window.deiconify()
            
            button_frame = Frame(change_password_window)
            button_frame.pack(pady=10)

            submit_button = Button(button_frame, text="Submit", command=submit_change_password)
            submit_button.pack(side=RIGHT, padx=5)

            cancel_button = Button(button_frame, text="Cancel", command=cancel_change_password)
            cancel_button.pack(side=RIGHT, padx=5)
        
        button_frame = Frame(actions_window)
        button_frame.pack(pady=10)

        logout_button = Button(button_frame, text="Logout", command=MainUI.logout())
        logout_button.pack(side=RIGHT, padx=5)

        change_password_button = Button(button_frame, text="Change Password", command=change_password)
        change_password_button.pack(side=RIGHT, padx=5)
