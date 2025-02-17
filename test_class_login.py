# import getpass
from tkinter import messagebox
import pyodbc
from user_test import User

# import datetime
# import threading
from db_access import connection_string

# database tables
LOGIN_DATA = "login_data"
DOCTORS = "doctors"
PATIENTS = "patients"
DIAGNOSES = "diagnoses_icd"
PROCEDURES = "procedures_icd"
OMR = "omr"
DIAGNOSES_DESC = "d_icd_diagnoses"
PROCEDURES_DESC = "d_icd_procedures"
EMAR = "emar"
ADMISSIONS = "admissions"
PHARMACY = "pharmacy"
ADMINS = "admins"


class AuthSystem:
    # Nante
    def __init__(self):
        self.users = []
        self.logged_in = False

    def check_user(self, subject_id, password):
        # Nante, Leander
        """Checks if the user exists in the database.

        Args:
            subject_id (int): The subject id of the user
            password (str): The password of the user

        Returns:
            list: User data if the user exists, None otherwise
        """
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute(
                f"select password, subject_id, role FROM {LOGIN_DATA} WHERE subject_id = ? AND password = ?",
                subject_id,
                password,
            )
            self.users = cursor.fetchall()
            cursor.close()
            connection.close()
        except pyodbc.Error as db_error:
            print(f" Db error: {db_error}")
        except Exception as e:
            print(f"An unexpected error occured: {e}")

        temp_user = None
        user = []

        for i in self.users:
            if str(i[0] == str(subject_id)):
                temp_user = i
                break

        if temp_user:
            for i in temp_user:
                user.append(i)

            if user[2] == "Doctor":
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                cursor.execute(
                    f"""select d.firstname, d.surname, d.department FROM {DOCTORS} AS d 
                    INNER JOIN {LOGIN_DATA} AS l ON d.subject_id = l.subject_id 
                    WHERE d.subject_id = ? """,
                    subject_id,
                )
                result = cursor.fetchall()[0]
                cursor.close()
                connection.close()
                for r in result:
                    user.append(r)

            elif user[2] == "Patient":
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                cursor.execute(
                    f"""select p.firstname, p.surname FROM {PATIENTS} AS p
                    INNER JOIN {LOGIN_DATA} AS l ON p.subject_id = l.subject_id 
                    WHERE p.subject_id = ? """,
                    subject_id,
                )
                result = cursor.fetchall()[0]
                cursor.close()
                connection.close()
                for r in result:
                    user.append(r)

            elif user[2] == "Admin":
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                cursor.execute(
                    f"""select a.firstname, a.surname FROM {ADMINS} AS a 
                    INNER JOIN {LOGIN_DATA} AS l ON a.subject_id = l.subject_id 
                    WHERE a.subject_id = ? """,
                    subject_id,
                )
                result = cursor.fetchall()[0]
                cursor.close()
                connection.close()
                for r in result:
                    user.append(r)

        if user is None:
            print("Invalid username or password.")
        return user

    # Konstantin, Leander, Nante
    def login(self, subject_id, password):
        """Logs the user into the system if the credentials are correct.

        Args:
            subject_id (int): The user's subject id
            password (str): The user's password
        """
        user = self.check_user(subject_id, password)
        if user:
            print(user)
            print(f"\nLogin successful! Welcome, {user[3]} {user[4]}.")
            self.logged_in = True
            user_role = user[2]
            if user_role == "Doctor":
                print(f"Your role in this hospital: {user_role}")
                print(f"Your department: {user[5]}")
            else:
                print(f"Your role in this hospital: {user_role}")

    def logout(self):
        """Logs the user out and returns to the main menu."""
        self.logged_in = False

    def reset_password(self, subject_id, password, new_password, confirm_new_password):
        """Resets the user's password.

        Args:
            subject_id (int): The user's subject id
            password (str): The user's password
            new_password (str): The user's new password
            confirm_new_password (str): The user's new password confirmation

        Raises:
            ValueError: If the password doesn't meet the requirements
        """
        # Leander, Nante
        try:
            user = self.check_user(subject_id, password)
            if user is None:
                messagebox.showerror("Error", "Wrong User ID")
                raise ValueError

            if new_password != confirm_new_password:
                messagebox.showerror("Error", "Passwords do not match")
                raise ValueError

            h_new_password = User.hash_password(new_password)
            if user[0] == h_new_password:
                messagebox.showerror("Error", "Wrong old password")
                raise ValueError

            # Konstantin
            try:
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                cursor.execute(
                    f"UPDATE {LOGIN_DATA} SET password = ? WHERE subject_id = ?",
                    h_new_password,
                    subject_id,
                )
                cursor.close()
                connection.commit()
                connection.close()
                print("\nPassword reset successfull!\n")
                # break
            except ValueError as error:
                print(error)
        except ValueError as error:
            print(error)

    # def Autologout(self, timeout_minutes = 4):
