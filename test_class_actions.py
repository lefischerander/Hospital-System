from test_class_login import AuthSystem
import getpass
from user_test import User, Admin, Patient, Doctor
import hashlib
import pyodbc
import Service_Database


connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-CC0D63;DATABASE=LANK;UID=LANK_USER;PWD=Lank1.;TrustServerCertificate=YES'

user_service= Service_Database.User_service()



class Actions:
    def admin_actions():
        # Actions for the admin
        print("Your possible actions: ")
        print()
        print("1. View all users")
        print("2. View patient data")
        print("3. View doctor data")
        print("3. Creating a new account")
        print("4. Change your password") 
        print("5. Logout")
        
        choice = input("Choose an action: ")
        if choice == '1':
            print(f"All Users: {Patient, Doctor}", ) # Show all users
            print()
            Actions.admin_actions() # Return to admin actions
        elif choice == '2':
            subject_id = input("Pleaser enter the patient ID: ")


            
            
            
            
            
            
            
            
            #user = AuthSystem.self.users[subject_id]  # pick specific user
            #kill_acc = input(f"Are you sure you want to delete {subject_id}? \n1. YES 2. NO \n") # asking befor detliting
            #if kill_acc == '1':
                ##print("Platzhalter Zeile: 26")
                #print(f"{username} is now deleted")
            #elif kill_acc == '2':
             #print(f"The {username} will be not deleted")
            #print()
            #Actions.admin_actions() # Return to admin actions
        elif choice == '3':
            print("Platzhalter Zeile: 33")
            print()
            Actions.admin_actions() # Return to admin actions
        elif choice == '4': 
            print("Platzhalter Zeile: 37")
            print()
            Actions.admin_actions() # Return to admin actions
        elif choice == '5':
            AuthSystem.logout()    # Logout

    def doctor_actions():
    # Actions for the doctor
        print("Your possible actions: ")
        print("1. View a patient")
        print("2. View your profile")
        print("3. Change your password")
        print("4. Logout")
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
        elif choice == '4':
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

    