from test_class_login import AuthSystem
import getpass
import test_analyse

# import hashlib
import Service_Database
from user_test import User
import config

user_service = (
    Service_Database.User_service()
)  # creating an instance of the class Userservice
# auth_system = AuthSystem()  # instance of the class AuthSystem

analyzing = test_analyse.Analyse()


class Actions:
    """This class is reponsible for handling all possible actions of each user:
                    
                    Admin, Doctor and Patient 
    """
    
    
    #Konstantin, Nante
    
    
    def admin_actions():
        
        """ This function takes no parameter (or arguments) 
             
            The admin user can perform 6 possible actions. From 1 to 6.
             
            Each time the user is done doing his action, 
            he can go back to the menu by clicking on the back button (UI).
            If the user is using a console, he will be sent directly back to the menu (this function)
            
            (This function)
                                   
        """
        
        print("Your possible actions: \n")
        print("1. View all users")
        print("2. Delete an account")  # low priority
        print("3. View patient's profile")
        print("4. View doctor's profile")
        print("5. Change password")
        print("6. Logout\n")

        choice = input("Choose an action: \n")
        auth = AuthSystem()

        # Nante
        if choice == "1":
            # We are parsing the view_all-users function to the instance of the class Service
            user_service.view_all_users()
            print("All users: ", user_service.view_all_users())
            # After tah
            Actions.admin_actions()
        # Nante
        elif choice == "2":  # low priority
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

        # Nante
        elif choice == "3":
            patient = int(
                input("Enter the subject_id of the patient you want to view:  \n")
            )
            patient_info = user_service.get_patient_profile(patient)
            print(patient_info)

            
            Actions.admin_actions()
        #Nante
        elif choice == "4":
            doctor = int(input("Enter the surname of the doctor you want to view"))
            doctor_info = user_service.get_doctor_by_name(doctor)
            print(doctor_info)
            print("Press 'menu' to go back to the main menu or 'logout' to logout")
        # Nante
        elif choice == "5":
            user = input("Enter your Subject_id: ").strip()
            pw = getpass.getpass("Your currend Password: ")
            pw = User.hash_password(pw)
            auth.reset_password(user, pw)
            Actions.admin_actions()  # Return to admin actions
        # Nante
        elif choice == "6":
            # auth_system.logout()
            Actions.admin_actions()  # Return to admin actions
        # Nante
        else:
            print("Invalid please choose one of the above possibles actions")
            print()

    # Nante
    def doktor_actions():
        
        """ This function takes no parameter (or arguments) 
             
            The doctor user can perform 7 possible actions. From 1 to 7.
             
            Each time the user is done doing his action, 
            he can go back to the menu by clicking on the back button (UI).
            If the user is using a console, he will be sent directly back to the menu (this function)
            
            
                                   
        """
        
        
        print("Your possible actions: ")
        print("1. View patient's profile")
        print("2. View your profile")
        print("3. Add diagnosis")
        print("4. View patient's recent medical procedures")
        print("5. View diagnosis of a patient")
        print("6. Change password")
        print("7. Logout")

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
            doctor_profile = user_service.get_your_profile(config.subject_id_logged)
            print(doctor_profile)
            print("Your subject_id: ", config.subject_id_logged)

            Actions.doktor_actions()

        elif choice == "3":
            try:
                diagnosis_subject_id = None
                while (
                    diagnosis_subject_id is None
                    or user_service.check_id(diagnosis_subject_id) is None
                ):
                    diagnosis_subject_id = str(
                        input(
                            " Enter the subject_id of the patient you want to add a diagnosis to: "
                        )
                    )

                    icd_code = int(input("Enter the diagnosis (icd_code): "))

                    diagnosis_added = str(
                        (
                            user_service.create_diagnosis(
                                diagnosis_subject_id, config.subject_id_logged, icd_code
                            )
                        )
                    )

                if diagnosis_added is not None:
                    print("Diagnosis added successfully")

                else:
                    raise Exception("Please enter a valid input (valid ICD-Code)")

                Actions.doktor_actions()
            except Exception as e:
                print("An error occured: ", e)
                Actions.doktor_actions()

        elif choice == "4":
            patient_procedures = int(
                input(
                    "Enter the subject_id of the patient you want to view the recent medical procedures: "
                )
            )
            procedures = user_service.get_procedures_by_subject_id(
                patient_procedures, config.subject_id_logged
            )
            print(procedures)
            print("Press 'menu' to go back to the main menu")

        elif choice == "5":
            patient_diagnosis = int(
                input(
                    "Enter the subject_id of the patient you want to see the diagnosis: "
                )
            )

            diagnosis = user_service.get_diagnosis(
                patient_diagnosis, config.subject_id_logged
            )
            print(f"The diagnosis of the patient (subject_id): {patient_diagnosis} ")
            print(diagnosis)

        elif choice == "6":
            user = input("Enter your Subject_id: ").strip()
            pw = getpass.getpass("Your currend Password: ")
            pw = User.hash_password(pw)
            auth.reset_password(user, pw)
            Actions.admin_actions()  # Return to admin actions
        else:
            print("Invalid please choose one of the above possibles actions")
            print()

    def patient_actions():
        
        """ This function takes no parameter (or arguments) 
             
            The patient user can perform 4 possible actions. From 1 to 4.
             
            Each time the user is done doing his action, 
            he can go back to the menu by clicking on the back button (UI).
            If the user is using a console, he will be sent directly back to the menu (this function)
            
            
                                   
        """
        print("Your possible actions: ")
        print("1. View your medical procedures")
        print("2. View your profile")
        print("3. Change password")
        print("4. Logout")

        auth = AuthSystem()
        choice = input("Choose an action: ")

        if choice == "1":
            try:
                patient_procedures = user_service.get_procedures_by_subject_id(
                    config.subject_id_logged, config.subject_id_logged
                )
                print("Your recent procedures: ", patient_procedures)

            except Exception as e:
                print("An unexpected error occured: ", e)
                Actions.patient_actions()

        elif choice == "2":
            patient_profile = user_service.get_your_profile(config.subject_id_logged)
            print(patient_profile)

            Actions.patient_actions()
        elif choice == "3":
            user = input("Username: ").strip()
            pw = getpass.getpass("Your currend Password: ")
            pw = User.hash_password(pw)
            auth.reset_password(user, pw)
            Actions.patient_actions()

        elif choice == "4":  # already implemented in the ui
            auth.logout()  # Logout

        else:
            print("Invalid please choose one of the above possibles actions")
            print()
