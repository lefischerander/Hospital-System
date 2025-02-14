from tkinter import Tk, Button, messagebox, Label, Entry, Toplevel, Frame, RIGHT, LEFT, RAISED, TOP

# import getpass
from test_class_login import AuthSystem

from helppage import HelpPage

import sys
import subprocess
# from test_class_actions import Actions
from user_test import User
import Service_Database
# from main_ui import root

user_service = (
    Service_Database.User_service()
)  # creating an instance of the class Userservice


user_service= Service_Database.User_service()#creating an instance of the class Userservice
#Doktor [uid][name][surname][department]
#Patient [uid][gender][age][Date of Death][name][surname]
class ActionsUI:
    def doktor_actions(global_username):
        actions_window = Tk()
        actions_window.title("Doktor Actions")
        actions_window.geometry("800x600")

        print("1. View patient data")
        print("2. View your profile")
        print("3. Change Password")
        print("4. Logout")
        print()

        def view_patient_data():
            def get_patient_id():
                get_patient_id_window = Toplevel(actions_window)
                get_patient_id_window.title("Patient ID")

                Label(get_patient_id_window, text="Patient ID:").pack(pady=5)
                patient_id = Entry(get_patient_id_window)
                patient_id.pack(pady=5)

                def submit_patient_id():
                    get_patient_id_window.destroy()
                    return patient_id

                
                def cancel_get_patient_id():
                    get_patient_id_window.destroy()

                button_frame = Frame(get_patient_id_window)
                button_frame.pack(pady=10)
                
                submit_button = Button(get_patient_id_window, text="Submit", command=submit_patient_id)
                submit_button.pack(pady=5, side=RIGHT)

                cancel_button = Button(get_patient_id_window, text="Cancel", command=cancel_get_patient_id)
                cancel_button.pack(pady=5, side=RIGHT)

            patient_id = get_patient_id()
            view_patient_data_window = Toplevel(actions_window)
            view_patient_data_window.title("Patient Data")
            view_patient_data_window.geometry("800x600")


            patient_data = user_service.get_patient_profile(patient_id)
            patient_info = ["Patient_ID", "Gender", "Age", "Name", "Surname", "Date of Death"]
            for i in range(len(patient_data)):
                for j in range(2):
                    patient_grid = Frame(master=view_patient_data_window, relief=RAISED, borderwidth=1, width=15)
                    patient_grid.grid(row=i, column=j)
                    if(j==0):
                        label = Label(master=patient_grid, text=patient_info[i])
                        label.pack()
                    else:
                        label = Label(master=patient_grid, text=patient_data[i])
                        label.pack()
            #check output
            #add back button

        def view_profile():
            actions_window.withdraw()
            view_profile_window = Toplevel(actions_window)
            view_profile_window.title("Profile")
            view_profile_window.geometry("800x600")

            user_profile = user_service.get_your_profile(global_username)
            user_info = ["User ID", "Gender", "Age", "Name", "Surname"]

            for i in range(len(user_profile)):
                for j in range(2):
                    
                    user_grid = Frame(master=view_profile_window, relief=RAISED, borderwidth=1, width=15)
                    user_grid.grid(row=i, column=j)
                    if(j==0):
                        label = Label(master=user_grid, text=user_info[i])
                        label.pack()
                    else:
                        label = Label(master=user_grid, text=user_profile[i])
                        label.pack()

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
                messagebox.showinfo(
                    "Reset Password Info",
                    f"Username: {username}\nPassword: {old_password}",
                )
                auth.reset_password(username, hash_password, new_password, confirm_new_password)
                messagebox.showinfo("Reset Password Info", f"Username: {username}\nPassword: {old_password}")
                change_password_window.destroy()
                actions_window.deiconify()

            def cancel_change_password():
                change_password_window.destroy()
                actions_window.deiconify()

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

        def logout():
            actions_window.destroy()
            subprocess.run(["python", "main_ui.py"])
            sys.exit()            
            
            

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
        
        help_button = Button(actions_window, text="Help", command=HelpPage.help_page)
        help_button.pack(pady=10)

    def patient_actions(global_username):
        action_window = Tk()
        action_window.title("Patient Actions")
        action_window.geometry("800x600")

        print("1. View your profile")
        print("2. Change Password")
        print("3. Logout")
        print()

        def view_profile():
            action_window.withdraw()
            view_profile_window = Toplevel(action_window)
            view_profile_window.title("Profile")
            view_profile_window.geometry("800x600")

            user_profile = user_service.get_your_profile(global_username)
            user_info = ["User ID", "Gender", "Age", "Name", "Surname"]

            for i in range(len(user_profile)):
                for j in range(2):
                    
                    user_grid = Frame(master=view_profile_window, relief=RAISED, borderwidth=1, width=15)
                    user_grid.grid(row=i, column=j)
                    if(j==0):
                        label = Label(master=user_grid, text=user_info[i])
                        label.pack()
                    else:
                        label = Label(master=user_grid, text=user_profile[i])
                        label.pack()

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
                messagebox.showinfo(
                    "Reset Password Info",
                    f"Username: {username}\nPassword: {old_password}",
                )
                auth.reset_password(username, hash_password, new_password, confirm_new_password)
                messagebox.showinfo("Reset Password Info", f"Username: {username}\nPassword: {old_password}")
                change_password_window.destroy()
                action_window.deiconify()

            def cancel_change_password():
                change_password_window.destroy()
                action_window.deiconify()

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

        def logout():
            action_window.destroy()
            subprocess.run(["python", "main_ui.py"])
            sys.exit()            
            

        button_frame = Frame(action_window)
        button_frame.pack(pady=10)

        logout_button = Button(button_frame, text="Logout", command=logout)
        logout_button.pack(side=RIGHT, padx=5)

        change_password_button = Button(button_frame, text="Change Password", command=change_password)
        change_password_button.pack(side=RIGHT, padx=5)

        view_profile_button = Button(button_frame, text="View your profile", command=view_profile)
        view_profile_button.pack(side=RIGHT, padx=5)

        help_button = Button(action_window, text="Help", command=HelpPage.help_page)
        help_button.pack(pady=10)

    def admin_actions(global_username):
        actions_window = Tk()
        actions_window.title("Actions")
        actions_window.geometry("800x600")

        print("1. View all users")
        print("2. Delete a user")
        print("3. Change Password")
        print("4. Logout")
        print()

        def view_all_users():
            user_table = Toplevel(actions_window)
            user_table.title("All Users")
            user_table.geometry("800x600")

            row_list = ["User ID", "Name", "Surname", "Role"]
            all_users = user_service.view_all_users()

            for i in range(len(all_users)+1):
                for j in range(len(row_list)):
                    user_grid = Frame(master=user_table, relief=RAISED, borderwidth=1, width=15)
                    user_grid.grid(row=i, column=j)

                    if i == 0:
                        label = Label(master=user_grid, text=row_list[j])
                        label.pack()
                        continue
                        
                    label = Label(master=user_grid, text=all_users[i-1][j])
                    label.pack()



        def delete_user():
            # delete user
            actions_window.withdraw()

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
                messagebox.showinfo(
                    "Reset Password Info",
                    f"Username: {username}\nPassword: {old_password}",
                )
                auth.reset_password(username, hash_password, new_password, confirm_new_password)
                messagebox.showinfo("Reset Password Info", f"Username: {username}\nPassword: {old_password}")
                change_password_window.destroy()
                actions_window.deiconify()

            def cancel_change_password():
                change_password_window.destroy()
                actions_window.deiconify()

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

        def logout():
            actions_window.destroy()
            subprocess.run(["python", "main_ui.py"])
            sys.exit()            
        
        button_frame = Frame(actions_window)
        button_frame.pack(pady=10)

        logout_button = Button(button_frame, text="Logout", command=logout)
        logout_button.pack(side=RIGHT, padx=5)

        change_password_button = Button(button_frame, text="Change Password", command=change_password)
        change_password_button.pack(side=RIGHT, padx=5)

        delete_user_button = Button(button_frame, text="Delete a user", command=delete_user)
        delete_user_button.pack(side=RIGHT, padx=5)

        view_all_users_button = Button(button_frame, text="View all users", command=view_all_users)
        view_all_users_button.pack(side=RIGHT, padx=5)

        help_button = Button(actions_window, text="Help", command=HelpPage.help_page)
        help_button.pack(pady=10)
