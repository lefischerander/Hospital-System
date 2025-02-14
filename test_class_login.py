# import getpass
import sys
import pyodbc
from user_test import User

connection_string = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-CC0D63;DATABASE=LANK;UID=LANK_USER;PWD=Lank1.;TrustServerCertificate=YES"


class AuthSystem:
    def __init__(self):
        self.users = []
        self.logged_in = False

    def data_base_log(self, subject_id, password):
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute(
                "select  firstname, surname, role, password FROM New_login_data WHERE subject_id = ? AND password = ?",
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

    def login(self, subject_id, password):
        self.data_base_log(subject_id, password)
        user = None

        for i in self.users:
            if str(i[0] == str(subject_id)):
                user = i
                break

        if user is None:
            print(f"\nUsername {subject_id} not found.")
        elif password != user[3]:
            print(User.hash_password(password))
            print("\nInvalid password.\n")
        else:
            with open("logged_in_users.txt", "r") as file:
                line = file.readline()
                while line:
                    if subject_id == line.strip():
                        print(
                            f"\nUser {user[0]} {user[1]} (role: {user[2]}  already logged in.\n"
                        )
                        break
                    else:
                        line = file.readline()
                if not line:
                    with open("logged_in_users.txt", "a") as file:
                        file.write(f"{user[0]} {user[1]} \n")
                        print(f"\nLogin successful! Welcome, {user[0]} {user[1]}.")
                        self.logged_in = True
                        user_role = user[2]
                        if user_role == "Doctor":
                            print(f"You are {user_role} in this hospital")
                            print("Your department: \n")  # edit department later
                        else:
                            print(f"You are {user_role} in this hospital\n")

    def logout(self, subject_id):
        with open("logged_in_users.txt", "r") as file:
            lines = file.readlines()

        with open("logged_in_users.txt", "w") as file:
            for line in lines:
                if line.strip() != subject_id:
                    file.write(line)
                else:
                    print(
                        f"\nUser {subject_id} logged out successfully. Thank you for using our services.\n"
                    )
                    self.logged_in = False
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

                    # with open('test_class_login.py', 'w') as file:
                    # User.hash_password[username] = file.write(f"{h_new_password}")
                    print("\nPassword reset successful!\n")

                    break
                except ValueError as error:
                    print(error)
        except ValueError as error:
            print(error)
