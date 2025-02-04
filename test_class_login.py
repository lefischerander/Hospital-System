from user_test import User, Admin, Patient, Doctor
import sys
import getpass
#import users_data

class AuthSystem:
    def __init__(self):
        self.users = {
            '123': Admin('K.Kolbek','3eb3fe66b31e3b4d10fa70b5cad49c7112294af6ae4e476a1c405155d45aa121', 'Konstantin', 'Kolbek',), # admin123 Admin123!  
            '234': Admin('L.Fischer', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 'Leander', 'Fischer'),
            '345': Admin('N.Razafindraibe', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 'Nante', 'Razafindraibe'),
            '456': Admin('E.Schaefer', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 'Erik', 'Schaefer'),
            '10000001': Patient('10000001', '3eb3fe66b31e3b4d10fa70b5cad49c7112294af6ae4e476a1c405155d45aa121', 'ATest', 'TestA'), # 01.01.2025
            '10003400': Patient('10003400', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69', 'BTest', 'TestB'),
            '10002428': Patient('10002428', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69', 'CTest', 'TestC'),
            '10032725': Patient('10032725', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69', 'DTest', 'TestD'),
            '10027445': Patient('10027445', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69', 'ETest', 'TestE'),
            '10022281': Patient('10022281', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69', 'FTest', 'TestF'),
            '10035631': Patient('10035631', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69', 'GTest', 'TestG'),
            '10024043': Patient('10024043', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69', 'HTest', 'TestH'),
            '10025612': Patient('10025612', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69', 'ITest', 'TestI'),
            '10003046': Patient('10003046', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69', 'JTest', 'TestJ'),
            '110': Doctor('110', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08', 'Doom', 'Paris', 'radiology'), # test
            '111': Doctor('111', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08', 'Maik', 'Maier','gastroenterology'),
            '112': Doctor('112', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08', 'Anja', 'Mueller','oncology')
        }
        self.logged_in = False

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


