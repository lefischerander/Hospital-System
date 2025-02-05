from test_class_login import AuthSystem
import getpass
import hashlib
import Service_Database
from user_test import User

user_service= Service_Database.User_service()#creating an instance of the class Userservice

class Actions:
    def admin_actions():
        # Actions for the admin
        print("Your possible actions: \n")
        print("1. View all users")
        print("2. Delete an account")
        print("3. View patient's information")
        print("4. Change your password") 
        print("5. Logout\n")
        
        choice = input("Choose an action: \n")
        auth = AuthSystem()

        if choice == '1':
            print("All Users: Patients, Doctors 'Zeile: 21'") # Show all users
            print()
            Actions.admin_actions() # Return to admin actions
        
        elif choice == '2':
          try:
              user_to_be_deleted = int(input("Enter the subject_id of the user you want to delete: "))
              user_service.delete_user(user_to_be_deleted)
          except Exception as e:
                print(f"An unexpected error occurred: {e}")
                print("Do you want to try again? (yes/no)")
                answer = input()
                if answer == 'yes':
                    user_to_be_deleted = input("Enter the subject_id of the user you want to delete: ")
                    user_service.delete_user(user_to_be_deleted)
                else:
                    Actions.admin_actions()

        elif choice == '3':
            try:
                patient = int(input("Enter the subject_id of the patient you want to view:  "))
                patient_info= user_service.get_patient_information(patient)
                print(patient_info)
            except Exception as e:
                print("Error: ", e) 
            Actions.admin_actions() # Return to admin actions
        

            # username = input("Username: ")
            # user = AuthSystem.self.users[username]  # pick specific user
            # kill_acc = input(f"Are you sure you want to delete {username}? \n1. YES 2. NO \n") # asking befor detliting
            # if kill_acc == '1':
            #     print("Platzhalter Zeile: 26")
            #     print(f"{username} is now deleted")
            # elif kill_acc == '2':
            #     print(f"The {username} will be not deleted")
            # print()
            # Actions.admin_actions() # Return to admin actions

            
        elif choice == '4': 
            user = input("Username: ").strip()
            pw = getpass.getpass("Your currend Password: ")
            pw = User.hash_password(pw)
            auth.reset_password(user, pw)
            Actions.admin_actions() # Return to admin actions
        
        elif choice == '5':
            #subject_id = input("Enter your username: ")
            auth = AuthSystem()
            id = input("Enter your username: ").strip()
            auth.logout(id)    # Logout

    def doktor_actions():
    # Actions for the doctor
        print("Your possible actions: ")
        print("1. View a patient")
        print("2. View your profile")
        print("3. Change your password")
        print("4. View patient's information")
        print("5. Logout")
        print()

        auth = AuthSystem()
        
        choice = input("Choose an action: ")
        if choice == '1':
            username = input("Patient: ")
            patient = AuthSystem.self.users[username]   # Show patient data
            if patient:
                if patient['role'] == 'patient':
                    print("Platzhalter Zeile: 58")
                    print()
                    b = input("Work on patient record -> 1. \nback to actions -> 2.\n")
                    if b == '1':
                        print("Platzhalter Zeile: 61")
                        Actions.doktor_actions()
                    elif b == '2':
                        print()
                        Actions.doktor_actions()
                else:
                    print("User is not a patient!") # Check if user is a patient
                    print()
                    Actions.doktor_actions()    # Return to doctor actions
            else:
                print("Such patient doesn't exist!")    # Check if patient exists
                print()
                Actions.doktor_actions()    # Return to doctor actions

        elif choice == '2':
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            pw = hashlib.sha256(password.encode()).hexdigest()  #hashing the password
            user = AuthSystem.self.users[username]
            if user and user['password'] == pw:
                print()
                print(user)
                print()
                b = input("Work on your profile -> 1. \nback to actions -> 2.\n")
                if b == '1':
                    print("Platzhalter Zeile: 87")
                    return b
                elif b == '2':
                    print()
                    Actions.doktor_actions()
            else:
                print("Invalid username or password!")  # Output if login data is incorrect
                username
        
        elif choice == '3':
            user = input("Username: ").strip()
            pw = getpass.getpass("Your currend Password: ")
            pw = User.hash_password(pw)
            auth.reset_password(user, pw)
            Actions.doktor_actions() # Return to admin actions
        
        elif choice=='4':
            try:
                patient= input("Enter the subject_id of the patient you want to view:  ")
                user_service.get_patient_information(patient)
            except Exception as e:
                print("Error: ", e)
        elif choice == '5':
            AuthSystem.logout()    # Logout

    def patient_actions():
        # Actions for the patient
        print("Your possible actions: ")
        print("1. View your medical record")
        print("2. View your profile")
        print("3. Change password")
        print("4. Logout") 
        print()

        auth = AuthSystem()
        
        choice = input("Choose an action: ")
        if choice == '1':
            print("Platzhalter Zeile: 114")    # Show empty directory (no medical record)
            print()
            Actions.patient_actions()   # Return to patient actions  
        elif choice == '2':
            print("Platzhalter Zeile: 120")
            print()
            Actions.patient_actions()
        elif choice == '3':
            user = input("Username: ").strip()
            pw = getpass.getpass("Your currend Password: ")
            pw = User.hash_password(pw)
            auth.reset_password(user, pw)
            Actions.patient_actions()

        elif choice == '4':
            AuthSystem.logout()    # Logout

    