from tkinter import (
    Tk,
    Button,
    messagebox,
    Label,
    Entry,
    Toplevel,
    Frame,
    RIGHT,
    RAISED,
    LEFT,
)
from Backend.Database.login import AuthSystem
from UI.helppage import HelpPage
import sys
import subprocess
from Backend.user import User
import Backend.Database.database_service as database_service
from UI.analyse_ui import AnalyseUI
from Backend.analyse import Analyse

user_service = database_service.User_service()


class ActionsUI:
    """This class is responsible for the user interface if you are logged in"""

    def doktor_actions(global_username):
        """This method is responsible for the actions of the doctor

        Args:
            global_username (str): The username of the user
        """
        actions_window = Tk()
        actions_window.title("Homepage")
        actions_window.geometry("800x600")

        def on_closing():
            """This method is responsible for handling the window close event"""
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                actions_window.destroy()
                sys.exit()

        actions_window.protocol("WM_DELETE_WINDOW", on_closing)

        # get name and surname of user
        user = user_service.get_your_profile(global_username)
        name = user[1]
        surname = user[2]

        def view_patient_data():
            """This method is responsible for viewing the patient data"""
            actions_window.withdraw

            get_patient_id_window = Toplevel(actions_window)
            get_patient_id_window.title("Patient ID")

            Label(get_patient_id_window, text="Patient ID:").pack(pady=5)
            patient_id = Entry(get_patient_id_window)
            patient_id.pack(pady=5)

            def submit_patient_id():
                """This method is responsible for submitting the patient id"""

                def back_action():
                    """This method is responsible for going back to the actions window"""
                    actions_window.deiconify
                    view_patient_data_window.destroy

                view_patient_data_window = Toplevel(actions_window)
                view_patient_data_window.title("Patient Data")
                view_patient_data_window.geometry("800x600")

                view_patient_data_window.protocol(
                    "WM_DELETE_WINDOW", actions_window.deiconify
                )

                button_grid = Frame(
                    master=view_patient_data_window,
                    relief=RAISED,
                    borderwidth=1,
                    width=15,
                )
                button_grid.grid(row=0, column=0, padx=0, pady=0, sticky="ne")

                back_button = Button(button_grid, text="Back", command=back_action)
                back_button.grid(row=0, column=0, padx=10, pady=10, sticky="ne")

                patient_data = user_service.get_patient_profile(patient_id)
                patient_info = [
                    "Patient_ID",
                    "Gender",
                    "Age",
                    "Name",
                    "Surname",
                    "Date of Death",
                ]
                for i in range(len(patient_data)):
                    for j in range(2):
                        patient_grid = Frame(
                            master=view_patient_data_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15,
                        )
                        patient_grid.grid(row=i + 1, column=j, padx=5, pady=5)
                        if j == 0:
                            label = Label(master=patient_grid, text=patient_info[i])
                            label.pack()
                        else:
                            label = Label(master=patient_grid, text=patient_data[i])
                            label.pack()

            def cancel_get_patient_id():
                """This method is responsible for cancelling the patient id"""
                get_patient_id_window.destroy()
                actions_window.deiconify

            button_frame = Frame(get_patient_id_window)
            button_frame.pack(pady=10)

            submit_button = Button(
                get_patient_id_window, text="Submit", command=submit_patient_id
            )
            submit_button.pack(pady=5, side=RIGHT)

            cancel_button = Button(
                get_patient_id_window, text="Cancel", command=cancel_get_patient_id
            )
            cancel_button.pack(pady=5, side=RIGHT)

        def view_patient_diagnosis():
            """This method is responsible for viewing the diagnosis of patients"""
            get_patient_id_window = Toplevel(actions_window)
            get_patient_id_window.title("Patient ID")
            get_patient_id_window.geometry("200x300")

            Label(get_patient_id_window, text="Patient ID:").pack(pady=5)
            patient_id = Entry(get_patient_id_window)
            patient_id.pack(pady=5)

            def submit_patient_id():
                """This method is responsible for submitting the patient id"""
                id = patient_id.get()
                get_patient_id_window.destroy()
                AnalyseUI.analyse_action_doctor(id)

            def cancel_get_patient_id():
                """This method is responsible for cancelling the patient id"""
                get_patient_id_window.destroy()

            button_frame = Frame(get_patient_id_window)
            button_frame.pack(pady=10)

            submit_button = Button(
                get_patient_id_window, text="Submit", command=submit_patient_id
            )
            submit_button.pack(pady=5, side=RIGHT)

            cancel_button = Button(
                get_patient_id_window, text="Cancel", command=cancel_get_patient_id
            )
            cancel_button.pack(pady=5, side=RIGHT)

        def create_diagnostic_report():
            """This method is responsible for creating a diagnostic report"""
            get_patient_id_window = Toplevel(actions_window)
            get_patient_id_window.title("Patient ID")

            Label(get_patient_id_window, text="Patient ID:").pack(pady=5)
            patient_id = Entry(get_patient_id_window)
            patient_id.pack(pady=5)

            Label(get_patient_id_window, text="ICD Code:").pack(pady=5)
            icd_code_entry = Entry(get_patient_id_window)
            icd_code_entry.pack(pady=5)

            def submit_patient_id():
                """This method is responsible for submitting the patient id"""
                id = patient_id.get()
                icd_code = icd_code_entry.get()
                get_patient_id_window.destroy()
                user_service.create_diagnosis(id, global_username, icd_code)

            def cancel_get_patient_id():
                """This method is responsible for cancelling the patient id"""
                get_patient_id_window.destroy()
                actions_window.deiconify

            button_frame = Frame(get_patient_id_window)
            button_frame.pack(pady=10)

            submit_button = Button(
                get_patient_id_window, text="Submit", command=submit_patient_id
            )
            submit_button.pack(pady=5, side=RIGHT)

            cancel_button = Button(
                get_patient_id_window, text="Cancel", command=cancel_get_patient_id
            )
            cancel_button.pack(pady=5, side=RIGHT)

        def view_all_patient_addmissions():
            """This method is responsible for viewing all patient admissions"""
            analyse_user = Analyse()
            analyse_user.admissions_all_patients()

        def all_patient_info():
            """This method is responsible for viewing all patient information"""
            analyse_user = Analyse()
            analyse_user.all_patients()

        def view_profile():
            """This method is responsible for viewing the profile of the user"""
            actions_window.withdraw()
            view_profile_window = Toplevel(actions_window)
            view_profile_window.title("Profile")
            view_profile_window.geometry("800x600")

            user_profile = user_service.get_your_profile(global_username)
            user_info = ["User ID", "Name", "Surname", "Department", "Age"]
            print(global_username)
            print(user_profile)

            def back_action():
                """This method is responsible for going back to the actions window"""
                actions_window.deiconify()
                view_profile_window.destroy()

            view_profile_window.protocol("WM_DELETE_WINDOW", actions_window.deiconify)

            button_grid = Frame(
                master=view_profile_window,
                relief=RAISED,
                borderwidth=1,
                width=15,
            )
            button_grid.grid(row=0, column=0, padx=0, pady=0, sticky="ne")

            back_button = Button(button_grid, text="Back", command=back_action)
            back_button.grid(row=0, column=0, padx=10, pady=10, sticky="ne")

            for i in range(len(user_profile)):
                for j in range(2):
                    user_grid = Frame(
                        master=view_profile_window,
                        relief=RAISED,
                        borderwidth=1,
                        width=15,
                    )
                    user_grid.grid(row=i + 1, column=j, padx=5, pady=5)
                    if j == 0:
                        label = Label(master=user_grid, text=user_info[i])
                        label.pack()
                    else:
                        label = Label(master=user_grid, text=user_profile[i])
                        label.pack()

        def change_password():
            """This method is responsible for changing the password of the user"""
            actions_window.withdraw()
            auth = AuthSystem()
            change_password_window = Toplevel(actions_window)
            change_password_window.title("Change Password")
            change_password_window.geometry("500x300")

            change_password_window.protocol(
                "WM_DELETE_WINDOW", actions_window.deiconify
            )

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
                auth.reset_password(
                    username, hash_password, new_password, confirm_new_password
                )
                messagebox.showinfo("Password Reset Successful!")
                change_password_window.destroy()
                actions_window.deiconify()

            def cancel_change_password():
                """This method is responsible for cancelling the password change"""
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
            """This method is responsible for logging out the user"""
            actions_window.destroy()
            messagebox.showinfo(title=None, message="You have been logged out")
            subprocess.run(["python", "main_ui.py"])
            sys.exit()

        Label(
            actions_window, text=f"Welcome {name} {surname}", font=("Arial", 20)
        ).pack(pady=10)

        button_frame = Frame(actions_window)
        button_frame.pack(pady=10)

        logout_button = Button(button_frame, text="Logout", command=logout)
        logout_button.pack(side=RIGHT, padx=5)

        view_diagnosis = Button(
            button_frame,
            text="View Patient analysis",
            command=view_patient_diagnosis,
        )
        view_diagnosis.pack(side=RIGHT, padx=5)

        profile = Button(button_frame, text="View your profile", command=view_profile)
        profile.pack(side=RIGHT, padx=5)

        create_diagnostic_report_button = Button(
            button_frame,
            text="Create Diagnostic Report",
            command=create_diagnostic_report,
        )
        create_diagnostic_report_button.pack(side=RIGHT, padx=5)

        view_all_patient_addmissions_button = Button(
            button_frame,
            text="Average Length of Hospital Stays",
            command=view_all_patient_addmissions,
        )
        view_all_patient_addmissions_button.pack(side=RIGHT, padx=5)

        all_patient_info_button = Button(
            button_frame, text="Patient Age Distribution", command=all_patient_info
        )
        all_patient_info_button.pack(side=RIGHT, padx=5)

        change_password_button = Button(
            button_frame, text="Change Password", command=change_password
        )
        change_password_button.pack(side=RIGHT, padx=5)

        help_button = Button(actions_window, text="Help", command=HelpPage.help_page)
        help_button.pack(pady=10)

        """auto logout after 60 minutes"""
        actions_window.after(60 * 60000, logout)

    def patient_actions(global_username):
        """This method is responsible for the actions of the patient

        Args:
            global_username (str): The username of the user
        """
        action_window = Tk()
        action_window.title("Homepage")
        action_window.geometry("800x600")

        def on_closing():
            """This method is responsible for handling the window close event"""
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                action_window.destroy()
                sys.exit()

        action_window.protocol("WM_DELETE_WINDOW", on_closing)

        # get name and surname of user
        user = user_service.get_your_profile(global_username)
        name = user[3]
        surname = user[4]

        def view_profile():
            """This method is responsible for viewing the profile of the user"""
            action_window.withdraw()
            view_profile_window = Toplevel(action_window)
            view_profile_window.title("Profile")
            view_profile_window.geometry("800x600")

            user_profile = user_service.get_your_profile(global_username)
            user_info = ["User ID", "Gender", "Age", "Name", "Surname"]

            def back_action():
                """This method is responsible for going back to the actions window"""
                view_profile_window.destroy()
                action_window.deiconify

            view_profile_window.protocol("WM_DELETE_WINDOW", action_window.deiconify)

            button_grid = Frame(
                master=view_profile_window,
                relief=RAISED,
                borderwidth=1,
                width=15,
            )
            button_grid.grid(row=0, column=0, padx=0, pady=0, sticky="ne")

            back_button = Button(button_grid, text="Back", command=back_action)
            back_button.grid(row=0, column=0, padx=10, pady=10, sticky="ne")

            for i in range(len(user_profile)):
                for j in range(2):
                    user_grid = Frame(
                        master=view_profile_window,
                        relief=RAISED,
                        borderwidth=1,
                        width=15,
                    )
                    user_grid.grid(row=i + 1, column=j, padx=5, pady=5)
                    if j == 0:
                        label = Label(master=user_grid, text=user_info[i])
                        label.pack()
                    else:
                        if user_profile[i] == "F":
                            label = Label(master=user_grid, text="Female")
                            label.pack()
                        elif user_profile[i] == "M":
                            label = Label(master=user_grid, text="Male")
                            label.pack()
                        else:
                            label = Label(master=user_grid, text=user_profile[i])
                            label.pack()

        def view_diagnosis():
            """This method is responsible for viewing the diagnosis of the patient"""
            patient_id = global_username
            AnalyseUI.analyse_action_main(patient_id)

        def change_password():
            """This method is responsible for changing the password of the user"""
            action_window.withdraw()
            auth = AuthSystem()
            change_password_window = Toplevel(action_window)
            change_password_window.title("Change Password")
            change_password_window.geometry("500x300")

            change_password_window.protocol("WM_DELETE_WINDOW", action_window.deiconify)

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
                # auth.reset_password(username, hash_password)
                messagebox.showinfo(
                    "Reset Password Info",
                    f"Username: {username}\nPassword: {old_password}",
                )
                auth.reset_password(
                    username, hash_password, new_password, confirm_new_password
                )
                messagebox.showinfo("Password Reset Successful!")
                change_password_window.destroy()
                action_window.deiconify()

            def cancel_change_password():
                """This method is responsible for cancelling the password change"""
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

            action_window.after(60 * 60000, logout)

        def logout():
            """This method is responsible for logging out the user"""
            action_window.destroy()
            messagebox.showinfo(title=None, message="You have been logged out")
            subprocess.run(["python", "main_ui.py"])
            sys.exit()

        Label(action_window, text=f"Welcome {name} {surname}", font=("Arial", 20)).pack(
            pady=10
        )

        button_frame = Frame(action_window)
        button_frame.pack(pady=10)

        logout_button = Button(button_frame, text="Logout", command=logout)
        logout_button.pack(side=RIGHT, padx=5)

        change_password_button = Button(
            button_frame, text="Change Password", command=change_password
        )
        change_password_button.pack(side=RIGHT, padx=5)

        view_diagnosis_button = Button(
            button_frame, text="View your diagnosis", command=view_diagnosis
        )
        view_diagnosis_button.pack(side=LEFT, padx=5)

        view_profile_button = Button(
            button_frame, text="View your profile", command=view_profile
        )
        view_profile_button.pack(side=RIGHT, padx=5)

        help_button = Button(action_window, text="Help", command=HelpPage.help_page)
        help_button.pack(pady=10)

        """auto logout after 60 minutes"""
        action_window.after(60 * 60000, logout)

    def admin_actions(global_username):
        """This method is responsible for the actions of the admin

        Args:
            global_username (str): The username of the user
        """
        actions_window = Tk()
        actions_window.title("Homepage")
        actions_window.geometry("800x600")

        def on_closing():
            """This method is responsible for handling the window close event"""
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                actions_window.destroy()
                sys.exit()

        actions_window.protocol("WM_DELETE_WINDOW", on_closing)

        def view_all_users():
            """This method is responsible for viewing all users"""
            actions_window.withdraw
            user_table = Toplevel(actions_window)
            user_table.title("All Users")
            user_table.geometry("800x600")

            user_table.protocol("WM_DELETE_WINDOW", actions_window.deiconify)

            row_list = ["User ID", "Role"]
            all_users = user_service.view_all_users()

            def back_action():
                """This method is responsible for going back to the actions window"""
                actions_window.deiconify
                user_table.destroy()

            button_grid = Frame(
                master=user_table,
                relief=RAISED,
                borderwidth=1,
                width=15,
            )
            button_grid.grid(row=0, column=0, padx=0, pady=0, sticky="ne")

            back_button = Button(button_grid, text="Back", command=back_action)
            back_button.grid(row=0, column=0, padx=10, pady=10, sticky="ne")

            for i in range(len(all_users) + 1):
                for j in range(len(row_list)):
                    user_grid = Frame(
                        master=user_table, relief=RAISED, borderwidth=1, width=15
                    )
                    user_grid.grid(row=i + 1, column=j, padx=5, pady=5)

                    if i == 0:
                        label = Label(master=user_grid, text=row_list[j])
                        label.pack()
                        continue

                    label = Label(master=user_grid, text=all_users[i - 1][j])
                    label.pack()

        def delete_user():
            """This method is responsible for deleting a user"""
            get_user_id_window = Toplevel(actions_window)
            get_user_id_window.title("Patient ID")
            get_user_id_window.geometry("200x300")

            get_user_id_window.protocol("WM_DELETE_WINDOW", actions_window.deiconify)

            Label(get_user_id_window, text="Patient ID:").pack(pady=5)
            patient_id = Entry(get_user_id_window)
            patient_id.pack(pady=5)

            def submit_patient_id():
                """This method is responsible for submitting the user id"""
                if messagebox.askquestion(
                    title="Delete user",
                    message="Are you sure you want to continue?",
                ):
                    user_service.delete_user(patient_id.get())
                    messagebox.showinfo(title=None, message="User removed successfully")

                get_user_id_window.destroy()

            def cancel_get_patient_id():
                """This method is responsible for cancelling and returning to the actions window"""
                get_user_id_window.destroy()

            button_frame = Frame(get_user_id_window)
            button_frame.pack(pady=10)

            submit_button = Button(
                get_user_id_window, text="Submit", command=submit_patient_id
            )
            submit_button.pack(pady=5, side=RIGHT)

            cancel_button = Button(
                get_user_id_window, text="Cancel", command=cancel_get_patient_id
            )
            cancel_button.pack(pady=5, side=RIGHT)

        def change_password():
            """This method is responsible for changing the password of the user"""
            actions_window.withdraw()
            auth = AuthSystem()
            change_password_window = Toplevel(actions_window)
            change_password_window.title("Change Password")
            change_password_window.geometry("500x300")

            change_password_window.protocol(
                "WM_DELETE_WINDOW", actions_window.deiconify
            )

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
                    actions_window.deiconify()
                else:
                    messagebox.showerror("Error", "Password reset failed")
                    change_password()
                    change_password_window.destroy()

            def cancel_change_password():
                """This method is responsible for cancelling the password change"""
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
            """This method is responsible for logging out the user"""
            actions_window.destroy()
            messagebox.showinfo(title=None, message="You have been logged out.")
            subprocess.run(["python", "main_ui.py"])
            sys.exit()

        button_frame = Frame(actions_window)
        button_frame.pack(pady=10)

        logout_button = Button(button_frame, text="Logout", command=logout)
        logout_button.pack(side=RIGHT, padx=5)

        change_password_button = Button(
            button_frame, text="Change Password", command=change_password
        )
        change_password_button.pack(side=RIGHT, padx=5)

        delete_user_button = Button(
            button_frame, text="Delete a user", command=delete_user
        )
        delete_user_button.pack(side=RIGHT, padx=5)

        view_all_users_button = Button(
            button_frame, text="View all users", command=view_all_users
        )
        view_all_users_button.pack(side=RIGHT, padx=5)

        help_button = Button(actions_window, text="Help", command=HelpPage.help_page)
        help_button.pack(pady=10)

        """auto logout after 60 minutes"""
        actions_window.after(60 * 60000, logout)
