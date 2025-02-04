from user_test import User, Admin, Patient, Doctor
import sys
import getpass
import sys
import pyodbc

connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-CC0D63;DATABASE=LANK;UID=LANK_USER;PWD=Lank1.;TrustServerCertificate=YES'

class AuthSystem:
    def __init__(self):
        self.users=[]
    
    
    
    
    def data_base_log(self, subject_id, password):
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()
        cursor.execute("select firstname, surname from  from New_login_data where subject_id = ? and password = ?", subject_id, password)
        self.users = cursor.fetchall()
        cursor.close()
        connection.close()


    def login(self, subject_id, password):
        if subject_id not in self.users:
            print(f"\nUsername {subject_id} not found.")
        elif User.hash_password(password) != self.users[subject_id].password:
            print("\nInvalid password.\n")
        else:
            with open('logged_in_users.txt', 'r') as file:
                line = file.readline()
                while line:
                    if subject_id == line.strip():
                        print(f"\nUser {subject_id} already logged in.\n")
                        break
                    else:
                        line = file.readline()
                if not line:    
                    with open('logged_in_users.txt', 'a') as file:
                        file.write(f"{subject_id}\n")
                        print(f"\nLogin successful! Welcome, {subject_id}.")
                        self.logged_in = True
                        user_role = self.users[subject_id].role
                        if user_role == 'doctor':
                            print(f"You are {user_role} in this hospital")
                            print(f"Your department: {self.users[subject_id].department}\n")
                        else:
                            print(f"You are {user_role} in this hospital\n")       


    def logout(self, subject_id):
        with open('logged_in_users.txt', 'r') as file:
            for line in file:
                if subject_id != line.strip():
                    print(f"\nUser {subject_id} isn't logged in.\n")
                else:
                    with open('logged_in_users.txt', 'w') as file:
                        file.write(f"{0}\n")
                        print(f"\nUser {subject_id} logged out successfully. Thank you for using our services.\n")
                        sys.exit()

    def reset_password(self, subject_id, password):
        try:
            #subject_id = input("Enter your username: ").strip()
            if subject_id not in self.users:
                raise ValueError("Invalid username.\n")

            #password = getpass.getpass("Enter your current password: ")
            if self.users[subject_id].password != User.hash_password(password):
                raise ValueError("\nInvalid password.\n")
            
            while True:
                try:
                    new_password = getpass.getpass("Enter new password: ")
                    if len(new_password) < 8:
                        raise ValueError("\nPassword must be at least 8 characters long.\n")
                    if new_password.islower():
                        raise ValueError("\nPassword must contain at least one uppercase letter.\n")
                    if new_password.isupper():
                        raise ValueError("\nPassword must contain at least one lowercase letter.\n")
                    if new_password.isdigit():
                        raise ValueError("\nPassword must contain at least one letter.\n")
                    if new_password.isalpha():
                        raise ValueError("\nPassword must contain at least one number.\n")
                    if new_password.isalnum():
                        raise ValueError("\nPassword must contain at least one special character.\n")
                    
                    con_new_password = getpass.getpass("\nConfirm your new password: ")
                    if new_password != con_new_password:
                        raise ValueError("\nPasswords do not match!\n")
                    
                    h_new_password = User.hash_password(new_password)
                    if self.users[subject_id].password == User.hash_password(h_new_password):
                        raise ValueError("\nNew password must be different from the old password.\n")
                    
                    #with open('test_class_login.py', 'w') as file:
                        User.hash_password[username] = file.write(f"{h_new_password}")
                    print("\nPassword reset successful!\n")
                        
                    break
                except ValueError as error:
                    print(error)
        except ValueError as error:
            print(error)


