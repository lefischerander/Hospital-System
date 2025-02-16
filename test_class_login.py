# import getpass
import sys
import pyodbc
from user_test import User

# import datetime
# import threading
from db_access import connection_string
import config


class AuthSystem:
    def __init__(self):
        self.users = []
        self.logged_in = False

        

    def login(self, subject_id, password):
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute(
                "select  firstname, surname, role, password, subject_id FROM New_login_data WHERE subject_id = ? AND password = ?",
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
        
        user = None

        for i in self.users:
            if str(i[0] == str(subject_id)):
                user = i
                break

        if user is None:
            print(f"\nUsername {subject_id} not found.")
        elif password != user[3]:
          
            print("\nInvalid password.\n")
        else:
            print(f"\nLogin successful! Welcome, {user[0]} {user[1]}.")
            self.logged_in = True
            user_role = user[2]
            if user_role == "Doctor":
                print(f"Your role in this hospital: {user_role}")
                print("Your department: \n")
            else:
                print(f"Your role in this hospital: {user_role}")

    def logout():
        sys.exit()

    def reset_password(self, subject_id, password, new_password, confirm_new_password):
        try:
            if subject_id not in self.users:
                raise ValueError("Invalid username.\n")

            if self.users[subject_id].password != User.hash_password(password):
                raise ValueError("\nInvalid password.\n")

            while True:
                try:
                    if len(new_password) < 8:
                        raise ValueError(
                            "\nPassword must be at least 8 characters long.\n"
                        )
                    if new_password.islower():
                        raise ValueError(
                            "\nPassword must contain at least one uppercase letter.\n"
                        )
                    if new_password.isupper():
                        raise ValueError(
                            "\nPassword must contain at least one lowercase letter.\n"
                        )
                    if new_password.isdigit():
                        raise ValueError(
                            "\nPassword must contain at least one letter.\n"
                        )
                    if new_password.isalpha():
                        raise ValueError(
                            "\nPassword must contain at least one number.\n"
                        )
                    if new_password.isalnum():
                        raise ValueError(
                            "\nPassword must contain at least one special character.\n"
                        )

                    if new_password != confirm_new_password:
                        raise ValueError("\nPasswords do not match!\n")

                    h_new_password = User.hash_password(new_password)
                    if self.users[subject_id].password == User.hash_password(
                        h_new_password
                    ):
                        raise ValueError(
                            "\nNew password must be different from the old password.\n"
                        )

                  
                    print("\nPassword reset successful!\n")

                    break
                except ValueError as error:
                    print(error)
        except ValueError as error:
            print(error)

    # def Autologout(self, timeout_minutes = 4):
