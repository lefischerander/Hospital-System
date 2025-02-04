import getpass
from test_class_login import AuthSystem
import sys
from test_class_actions import Actions
from user_test import User

def main():
    auth = AuthSystem()
    action = input("1:login 2:reset password 3:exit: ").strip()
    
    try:
        if action == "3":
            print("Goodbye!")
            sys.exit()
        elif action == "1":
            user = input("Username: ").strip()
            pw = getpass.getpass("Password: ")
            pw = User.hash_password(pw)
            auth.login(user, pw)
            if auth.logged_in == False:
                main()
            while auth.logged_in == True:
                user_role = auth.users[user].role
                if user_role == 'doctor':
                    Actions.doktor_actions()
                elif user_role == 'patient':
                    Actions.patient_actions()
                elif user_role == 'admin': 
                    Actions.admin_actions()
                else:
                    print("Error 404\n")
                    break         
        elif action == "2":
            user = input("Username: ").strip()
            pw = getpass.getpass("Your currend Password: ")
            pw = User.hash_password(pw)
            auth.reset_password(user, pw)
            main()
        else:
            print("\nInvalid input. Please try again.\n")
            main()
    except ValueError as error:
            print(error)


    

if __name__ == "__main__":
    main()