from test_class_login import AuthSystem
import getpass
from user_test import User, Admin, Patient, Doctor
import hashlib
import Service_Database

user_service= Service_Database.User_service()#creating an instance of the class Userservice
auth_system = AuthSystem()#instance of the class AuthSystem

class Actions:
    def admin_actions():
        # Actions for the admin
        print("Your possible actions: ")
        print()
        print("1. View all users")
        print("2. Delete an account")
        print("3. View patient's information")
        print("4. View doctor's information")
        print("5. Change password")
        print("6. Logout")
        
        choice = input("Choose an action: ")
        if choice == '1':
            user_service.view_all_users()
            print("Press 'menu' to go back to the main menu or 'logout' to logout")
            
            answer = input()
            if answer == 'menu':
                Actions.admin_actions()
            elif answer == 'logout':
                auth_system.logout()
                


            
            
            
            
            #Actions.admin_actions()
            
            #print(f"All Users: {Patient, Doctor}", ) # Show all users
            #print()
            #Actions.admin_actions() # Return to admin actions
        
        elif choice == '2':
          user_to_be_deleted = int(input("Enter the subject_id of the user you want to delete: "))
          answer= print("Are you sure you want to delete this user? (yes/no)")
          if answer == 'yes':
            user_service.delete_user(user_to_be_deleted)
            print("User deleted successfully")
            print("Press 'menu' to go back to the main menu or 'logout' to logout")
            answer = input()
            if answer == 'menu':
                Actions.admin_actions()
            elif answer == 'logout':
                auth_system.logout()
            else:
                print("Invalid input")
                Actions.admin_actions()
          
          else:
                print("You changed your mind")
                answer= print("Press 'menu' to go back to the main menu or 'logout' to logout")
                if answer == 'menu':
                    Actions.admin_actions()
                elif answer == 'logout':
                    auth_system.logout()
                else:
                    print("Invalid input")
                    Actions.admin_actions()

        elif choice == '3':
            patient = int(input("Enter the subject_id of the patient you want to view:  "))
            patient_info= user_service.get_patient_information(patient)
            print(patient_info)
            print("Press 'menu' to go back to the main menu or 'logout' to logout")

                

          


            
            
            
            
            
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
        elif choice == '3':
            print("Platzhalter Zeile: 33")
            print()
            Actions.admin_actions() # Return to admin actions
        elif choice == '4': 
            print("Platzhalter Zeile: 37")
            print()
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
        print("5. Add diagnosis")
        print("6. Logout")
        print()
        
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
            print("Platzhalter Zeile: 79")
            print()
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
            print("Platzhalter Zeile: 120")
            print()
            Actions.patient_actions()
        elif choice == '4':
            AuthSystem.logout()    # Logout

    