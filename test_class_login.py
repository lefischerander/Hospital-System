from user_test import User, Admin, Patient, Doctor
import getpass
import sys

class AuthSystem:
    def __init__(self):
        self.users = {
            '123': Admin('123','3eb3fe66b31e3b4d10fa70b5cad49c7112294af6ae4e476a1c405155d45aa121', 'Konstantin', 'Kolbek',), # admin123 Admin123!  
            # 'L.Fischer': Admin('L.Fischer', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9'),
            # 'N.Razafindraibe': Admin('N.Razafindraibe', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9'),
            # 'E.Schaefer': Admin('E.Schaefer', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9'),
            # '1.1': Patient('1.1', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'), # 01.01.2025
            # '10003400': Patient('10003400', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            # '10002428': Patient('10002428', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            # '10032725': Patient('10032725', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            # '10027445': Patient('10027445', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            # '10022281': Patient('10022281', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            # '10035631': Patient('10035631', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            # '10024043': Patient('10024043', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            # '10025612': Patient('10025612', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            # '10003046': Patient('10003046', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            # 'D.Paris': Doctor('D.Paris', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08', 'radiology'), # test
            # 'M.Maier': Doctor('M.Maier', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08', 'gastroenterology'),
            # 'A.Mueller': Doctor('A.Mueller', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08', 'oncology')
        }
        self.logged_in = []

    def login(self, subject_id, password):
        password = User.hash_password(password) #hashlib.sha256(password.encode()).hexdigest()
        if subject_id not in self.users:
            print(f"\nUsername {subject_id} not found.")
        elif self.users[subject_id].password != User.hash_password(password):
            print("\nInvalid password.\n")
        elif subject_id in self.logged_in:
            print(f"\nUser {subject_id} already logged in.\n")
        else:
            self.logged_in.append(subject_id)
            print(f"\nLogin successful! Welcome, {subject_id}.")
            print(self.logged_in)
            user_role = self.users[subject_id].role
            if user_role == 'doctor':
                print(f"You are {user_role} in this hospital")
                print(f"Your department: {self.users[subject_id].department}\n")
            else:
                print(f"You are {user_role} in this hospital\n")

    def logout(self, subject_id):
        # subject_id = input("Enter your username: ")
        print(subject_id)
        print(self.logged_in)
        if subject_id in self.logged_in:
            self.logged_in.remove(subject_id)
            print(f"User {subject_id} logged out seccesful. Thank you for using our services.")
            sys.exit()
        else:
            print("Error: User isn't logged in")

    def reset_password(self):
        try:
            username = input("Enter your username: ").strip()
            if username not in self.users:
                raise ValueError("Invalid username.\n")
            
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
                    if self.users[username].password == User.hash_password(h_new_password):
                        raise ValueError("\nNew password must be different from the old password.\n")
                    
                    #with open('test_class_login.py', 'w') as file:
                        User.hash_password[username] = file.write(f"{h_new_password}")
                    print("\nPassword reset successful!\n")
                        
                    break
                except ValueError as error:
                    print(error)
        except ValueError as error:
            print(error)


