import getpass
from test_class_login import AuthSystem
import sys
from test_class_actions import Actions

def main():
    auth = AuthSystem()
    #while True:
    action = input("1:login 2:reset password 3:exit: ").strip().lower()
    
    try:
        if action == "3":
            print("Goodbye!")
            sys.exit()
        elif action == "1":
            user = input("Username: ").strip()
            pw = getpass.getpass("Password: ")
            auth.login(user, pw)
            if user not in auth.logged_in:
                main()
            while True:
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
            auth.reset_password()
            main()
        else:
            print("\nInvalid input. Please try again.\n")
            main()
    except ValueError as error:
            print(error)


    

if __name__ == "__main__":
    main()