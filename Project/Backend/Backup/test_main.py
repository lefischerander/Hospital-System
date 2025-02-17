import getpass
import sys
from Backend.class_actions import Actions
from Backend.Database.login import AuthSystem
from Backend.user import User
import Database.config as config

# This is the main file of the backup. 
# We import config.py for one specific reason
# As soon as an user is connected, the only variable (initialized as None) in config will save the user's id
# This variable will be then used several times as an argument when calling a method from classes

def main():
    # We created an instance of the class AuthSystem
    auth = AuthSystem()
    
    # The user is asked to choose between these actions
    action = input("1:login 2:reset password 3:exit: ").strip()

    try:
        if action == "3":
            print("Goodbye!")
            sys.exit()
        elif action == "1":
            user = input("Username: ").strip()
            pw = getpass.getpass("Password: ")
            pw = User.hash_password(pw)
            
            # We call the method login from the class AuthSystem to log the user in 
            auth.login(user, pw)
            
            # Since auth.logged_in is initially False, the program forces the user to go through main()
            # Otherwise the program might try to perform actions for a user who hasn’t logged in yet.
            if not auth.logged_in:
                main()
            
            # This while loop keeps running as long as the user remains logged in,
            # to ensure the system continues to work while the user is logged in.
            while auth.logged_in:
                
                # We extract the fourth index from the list (users) and store it in the user_role variable
                user_role = auth.users[0][4]
                
                # The variable from the module we created stores the subject_id of the logged_in user
                config.subject_id_logged = int(auth.users[0][3])

                if user_role == "Doctor":
                    Actions.doktor_actions()
                elif user_role == "Patient":
                    Actions.patient_actions()
                elif user_role == "admin":
                    Actions.admin_actions()
                else:
                    print("Error 404\n")
                    break
        elif action == "2":
            user = input("Username: ").strip()
            pw = getpass.getpass("Your current Password: ")
            pw = User.hash_password(pw)
            new_pw = getpass.getpass("New Password: ")
            auth.reset_password(user, pw, new_pw, new_pw)
            main()
        else:
            print("\nInvalid input. Please try again.\n")
            main()
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
