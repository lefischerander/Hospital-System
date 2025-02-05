from tkinter import Tk, Button, messagebox, Label, Entry, Toplevel, Frame, LEFT, RIGHT
import getpass
from test_class_login import AuthSystem
import sys
from test_class_actions import Actions
from user_test import User
global global_username
global global_password  
global_username = ""
global_password = ""

def login_action():
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
        username = username_entry.get()
        password = password_entry.get()
        global_username = username
        messagebox.showinfo("Globalusername", f"Username: {global_username}")
        hash_password = User.hash_password(password)
        auth.login(username, hash_password)
        if auth.logged_in == False:
            messagebox.showerror("Login Error", "Invalid username or password")
            login_action()
            login_window.destroy()
        else:
        
            while auth.logged_in == True:
                user_role = auth.users[0][2]
                if user_role == 'Doctor':
                    doktor_actions()
                elif user_role == 'Patient':
                    patient_actions()
                elif user_role == 'admin': 
                    admin_actions()
                else:
                    print("Error 404\n")
                    break

            messagebox.showinfo("Login Info", f"Username: {username}\nPassword: {password}")
            login_window.destroy()
            

    def cancel_login():
        login_window.destroy()
        root.deiconify()

    def doktor_actions():
        actions_window = Toplevel(root)
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
            change_password_window = Toplevel(root)
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

        def logout():
            AuthSystem.logout(global_username)
            global_username = ""
            actions_window.destroy()
            root.deiconify()
        
        button_frame = Frame(actions_window)
        button_frame.pack(pady=10)

        logout_button = Button(button_frame, text="Logout", command=logout)
        logout_button.pack(side=RIGHT, padx=5)

        patient_data = Button(button_frame, text="View patiant data", command=view_patient_data)
        patient_data.pack(side=RIGHT, padx=5)

        profile = Button(button_frame, text="View your profile", command=view_profile)
        profile.pack(side=RIGHT, padx=5)

        change_password_button = Button(button_frame, text="Change Password", command=change_password)
        change_password_button.pack(side=RIGHT, padx=5)

        


    def patient_actions():
        action_window = Toplevel(root)
        action_window.title("Patient Actions")
        action_window.geometry("800x600")

        print("1. View your profile")
        print("2. Change Password")
        print("3. Logout")
        print()

        def change_password():
            action_window.withdraw()
            auth = AuthSystem()
            change_password_window = Toplevel(root)
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

        def logout():
            AuthSystem.logout(global_username)
            global_username = ""
            action_window.destroy()
            root.deiconify()
        
        button_frame = Frame(action_window)
        button_frame.pack(pady=10)

        logout_button = Button(button_frame, text="Logout", command=logout)
        logout_button.pack(side=RIGHT, padx=5)

        change_password_button = Button(button_frame, text="Change Password", command=change_password)
        change_password_button.pack(side=RIGHT, padx=5)

    def admin_actions():
        actions_window = Toplevel(root)
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
            change_password_window = Toplevel(root)
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

        def logout():
            AuthSystem.logout(global_username)
            global_username = ""
            actions_window.destroy()
            root.deiconify()
        
        button_frame = Frame(actions_window)
        button_frame.pack(pady=10)

        logout_button = Button(button_frame, text="Logout", command=logout)
        logout_button.pack(side=RIGHT, padx=5)

        change_password_button = Button(button_frame, text="Change Password", command=change_password)
        change_password_button.pack(side=RIGHT, padx=5)

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

login_button = Button(root, text="Login", command=login_action)
login_button.pack(pady=10)

reset_password_button = Button(root, text="Reset Password", command=reset_password_action)
reset_password_button.pack(pady=10)

exit_button = Button(root, text="Exit", command=exit_action)
exit_button.pack(pady=10)

root.mainloop()