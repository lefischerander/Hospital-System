from test_class_login import AuthSystem
import getpass


# import hashlib
import Service_Database
from user_test import User
import config

user_service = (
    Service_Database.User_service()
)  # creating an instance of the class Userservice
#auth_system = AuthSystem()  # instance of the class AuthSystem


class Actions:
    def admin_actions():
        # Actions for the admin
        print("Your possible actions: \n")
        print("1. View all users")
        print("2. Delete an account") 
        print("3. View patient's profile")
        print("4. View doctor's profile")
        print("5. Change password")
        print("6. Logout\n")

        choice = input("Choose an action: \n")
        auth = AuthSystem()
        

        if choice == "1":
            # We are parsing the view_all-users function to the instance of the class Service 
            user_service.view_all_users()
            print("All users: ", user_service.view_all_users())
            # After tah
            Actions.admin_actions()

        elif choice == "2":
            user_to_be_deleted = int(
                int(input("Enter the subject_id of the user you want to delete: "))
            )
            answer = print("Are you sure you want to delete this user? (yes/no)")
            if answer == "yes":
                user_service.delete_user(user_to_be_deleted)
                print("User deleted successfully")
                subaction = print("Press 'menu' to go back to the main menu")
                if subaction == "menu":
                    Actions.admin_actions()
                else:
                    print("Invalid input")
                    Actions.admin_actions()

            else:
                print("You changed your mind")
                answer = print("Press 'menu' to go back to the main menu")
                if subaction == "menu":
                    Actions.admin_actions()

                else:
                    print("Invalid input")
                    Actions.admin_actions()

        elif choice == "3":
            patient = int(
                input("Enter the subject_id of the patient you want to view:  \n")
            )
            patient_info = user_service.get_patient_profile(patient)
            print(patient_info)

            answer = print("Press 'menu' to go back to the main menu")
            if answer == "menu":
                Actions.admin_actions()

        elif choice == "4":
            doctor = int(input("Enter the surname of the doctor you want to view"))
            doctor_info = user_service.get_doctor_by_name(doctor)
            print(doctor_info)
            print("Press 'menu' to go back to the main menu or 'logout' to logout")

        elif choice == "5":
            user = input("Enter your Subject_id: ").strip()
            pw = getpass.getpass("Your currend Password: ")
            pw = User.hash_password(pw)
            auth.reset_password(user, pw)
            Actions.admin_actions()  # Return to admin actions

        elif choice == "6":
            #auth_system.logout()
            Actions.admin_actions()  # Return to admin actions

    def doktor_actions():
        # Actions for the doctor
        print("Your possible actions: ")
        print("1. View patient's profile")
        print("2. View your profile")
        print("3. Add diagnosis")
        print("4. View patient's recent medical procedures")
        print("5. Change password")
        print("6. Logout")
        print()

        auth = AuthSystem()
        
        
        choice = input("Choose an action: ")

        if choice == "1":
            patient = int(
                input("Enter the subject_id of the patient you want to view:  ")
            )
            patient_profile = user_service.get_patient_profile(patient)
            print(patient_profile)

            answer = print("Press 'menu' to go back to the main menu")
            if answer == "menu":
                Actions.doktor_actions()
            else:
                print("Invalid input")
                Actions.doktor_actions()

        elif choice == "2":
            # doctor_id = int(
            #     input(
            #         "Before you can view your profile, you need to input your subject_id first: "
            #     )
            # )
            doctor_profile = user_service.get_your_profile(config.subject_id_logged)
            print(doctor_profile)

            Actions.doktor_actions()

        elif choice == "3":
            patient_diagnosis = int(
                input(
                    " Enter the subject_id of the patient you want to add a diagnosis to: "
                )
            )
            icd_c = input("Enter the diagnosis' ICD-Code: ")
            icd_v = input("Enter the diagnoses' ICD-Version: ")
            user_service.create_diagnosis(patient_diagnosis, icd_c, icd_v)
            print("Diagnosis added successfully")

            answer = print("Do you want to see the diagnosis you just added? (yes/no)")
            if answer == "yes":
                diagnosis = user_service.get_diagnosis(patient_diagnosis)
                print(diagnosis)
                print("Press 'menu' to go back to the main menu")
            else:
                Actions.doktor_actions()

        elif choice == "4":
            patient_procedures = int(
                input(
                    "Enter the subject_id of the patient you want to view the recent medical procedures: "
                )
            )
            procedures = user_service.get_procedures_by_subject_id(patient_procedures, config.subject_id_logged)
            print(procedures)
            print("Press 'menu' to go back to the main menu")
            

        elif choice == "5":
            user = input("Enter your Subject_id: ").strip()
            pw = getpass.getpass("Your currend Password: ")
            pw = User.hash_password(pw)
            auth.reset_password(user, pw)
            Actions.admin_actions()  # Return to admin actions

        elif choice == "6":
            AuthSystem.logout()  # Logout

    def patient_actions():
        # Actions for the patient
        print("Your possible actions: ")
        print("1. View your medical procedures")
        print("2. View your profile")
        print("3. Change password")
        print("4. Logout")
        print()

        auth = AuthSystem()
        #subject_id_logged_in = auth.users[4]
        choice = input("Choose an action: ")

        if choice == "1":
            patient_procedures = int(
                input("Enter your subject_id before to view your medical procedures: ")
            )
            user_service.get_procedures_by_subject_id(patient_procedures)
            print(patient_procedures)

            answer = print("Press 'menu' to go back to the main menu")
            if answer == "menu":
                Actions.patient_actions()
            else:
                print("Invalid input")
                Actions.patient_actions()

        elif choice == "2":
            patient = int(
                input(
                    "Before you can view your profile, you need to input your subject_id first"
                )
            )
            patient_profile = user_service.get_your_profile(patient)
            print(patient_profile)

            Actions.patient_actions()
        elif choice == "3":
            user = input("Username: ").strip()
            pw = getpass.getpass("Your currend Password: ")
            pw = User.hash_password(pw)
            auth.reset_password(user, pw)
            Actions.patient_actions()

        elif choice == "4":
            AuthSystem.logout()  # Logout
