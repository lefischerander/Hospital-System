import getpass
import sys
from Backend.class_actions import Actions
from Backend.Database.login import AuthSystem
from Backend.user import User
import Database.config as config


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
            if not auth.logged_in:
                main()
            while auth.logged_in:
                user_role = auth.users[0][4]
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
