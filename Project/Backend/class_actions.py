# This is a backup file
from Database.login import AuthSystem
import getpass


import Database.database_service as database_service
from Backend.user import User
import Database.config as config

# We import config.py for one specific reason
# As soon as a user is connected, the only variable (initialized as None) in config will save the user's id
# This variable will be then used several times as an arguments when calling a method from classes

user_service = (
    database_service.User_service()
)  # creating an instance of the class Userservice


class Actions:
    """This class is reponsible for handling all possible actions of each user:

    Admin, Doctor and Patient
    """

    # Konstantin, Nante

    def admin_actions():
        """This function takes no parameter (or arguments)

        The admin user can perform 6 possible actions. From 1 to 6.

        Each time the user is done doing his action,
        he can go back to the menu by clicking on the back button (UI).
        If the user is using a console, he will be sent directly back to the menu (this function)

        """

        print("Your possible actions: \n")
        print("1. View all users")
        print("2. Create an user account")
        print("3. Delete an account")
        print("4. View patient's profile")
        print("5. View doctor's profile")
        print("6. Change password")
        print("7. Logout\n")

        choice = input("Choose an action: \n")
        auth = AuthSystem()

        # Nante
        if choice == "1":
            # The function takes no argument
            # A row from the database will be output
            user_service.view_all_users()

            print("All users: ", user_service.view_all_users())

            # By calling this method the admin user is sent directly to the user menu
            Actions.admin_actions()

        elif choice == "2":
            # We are making sure that the code is robust enough to handle errors and not to crash
            
            try:
                # Username variable stores the input subject_id
                # We are making sure that the input is an integer
                username = int(input("Set the username (subject_id) of the user: "))

                # This variable stores the input password of the user by using getpass module
                password_input = getpass.getpass("Set the password of the user: ")

                # The password variable stores then the hashed password
                password = User.hash_password(password_input)

                role = input("Set the role of the user: ")
                firstname = input("Set the firstname of the user: ")
                surname = input("Set the surname of the user: ")

                # We call the function.
                user_service.create_user(username, password, role, firstname, surname)
            
            # An exception is raised if an error occurs
            except Exception as e:
                print("Error: ", e)

            Actions.admin_actions()

        elif choice == "3":
            try:
                # The input will be directly convert to an integer
                user_to_be_deleted = int(
                    input("Enter the subject_id of the user you want to delete: ")
                )
                # Ask the admin to confirm his choice
                answer = input("Are you sure you want to do delete an user? (yes/no): ")

                
                if answer == "yes":
                    # If he is sure then, then we will call the function
                    user_service.delete_user(
                        user_to_be_deleted, config.subject_id_logged
                    )
                    
                    #Back to the menu
                    Actions.admin_actions()

                elif answer == "no":
                    print("You changed your mind")
                    
                    #Back to the menu
                    Actions.admin_actions()

                else:
                    print("Invalid input")
                    Actions.admin_actions()

            except Exception as e:
                print("Oups error: ", e)
                Actions.admin_actions()

        

        elif choice == "4":
            # The input will be directly convert to an integer
            patient = int(
                input("Enter the subject_id of the patient you want to view:  \n")
            )
            
            # The function is called and takes one argument
            patient_info = user_service.get_patient_profile(patient)
            
            # A row from the database will be printed
            print(patient_info)
            
            # Back to the menu
            Actions.admin_actions()
        
        elif choice == "5":
            try:
                # This time we are making sure the input is a string
                doctor = str(
                    input("Enter the surname of the doctor you want to view: ")
                )
                
                # This variable will store the row from the database and then be printed
                doctor_info = user_service.get_doctor_by_name(doctor)

                print(doctor_info)
            except Exception as e:
                print("Oups user not found: ", e)

        
        elif choice == "6":
            # The variable user will store the input from the admin 
            user = input("Enter your Subject_id: ").strip()
            
            # The getpass method from the module is called. This is for making sure that the user's input is invisible on the terminal
            pw = getpass.getpass("Your currend Password: ")
            
            # The password is hashed
            pw = User.hash_password(pw)
            
            # The function from the class AuthSystem is called, and takes two arguments
            auth.reset_password(user, pw)
            
            # Return to admin actions
            Actions.admin_actions()  
       
        
        elif choice == "7":
            # auth_system.logout()
            Actions.admin_actions()  # Return to admin actions
       
        else:
            print("Invalid please choose one of the above possibles actions")
            Actions.admin_actions()


    def doktor_actions():
        """This function takes no parameter (or arguments)

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
             # We are making sure that the input is an integer
            
            patient = int(
                input("Enter the subject_id of the patient you want to view:  ")
            )
            # This variable will store the row from the database
            patient_profile = user_service.get_patient_profile(patient)

            # The row from the database will be output
            print(patient_profile)
            

            Actions.doktor_actions()

        elif choice == "2":
            # For debugging
            print("Your subject_id: ", config.subject_id_logged)
            
            # This variable will store the returned value of the function get_your_profile
            doctor_profile = user_service.get_your_profile(config.subject_id_logged)
            
            print(doctor_profile)
            

            Actions.doktor_actions()

        elif choice == "3":
            # We are making sure that the code is robust enough to handle errors and not to crash
            try:
                # We intialized the diagnosis_subject_id (this will be input by the doctor later) to None
                diagnosis_subject_id = None
                
                # The loop ensures that only valid patient IDs are accepted before proceeding
                # This helps avoid errors later when trying to add a diagnosis to a 'non-existent patient'.
                while (
                    diagnosis_subject_id is None
                    or user_service.check_id(diagnosis_subject_id) is None
                ):
                    diagnosis_subject_id = str(
                        input(
                            " Enter the subject_id of the patient you want to add a diagnosis to: "
                        )
                    )
                    
                    try:
                        # The doctor is asked then to input an icd_code
                        icd_code = int(input("Enter the diagnosis (icd_code): "))
                    
                    except ValueError as ve:
                        print("Invalid input: ", ve)
                    
                    
                    # diagnosis_added will store the returned value from the method create_diagnosis.
                    # The method create_diagnosis takes 3 arguments
                    diagnosis_added = str(
                        (
                            user_service.create_diagnosis(
                                diagnosis_subject_id, config.subject_id_logged, icd_code
                            )
                        )
                    )
                    
                    # If the variable diagnosis_added contains the expected value then the Diagnosis was added successfully

                if diagnosis_added is not None:
                    print("Diagnosis added successfully")
                    
                    # If the variable is None then an Exception will be raised meaning that an error occured
                else:
                    raise Exception("An unexpected error occured")

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
            
            Actions.doktor_actions()

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
            
            Actions.admin_actions()

    def patient_actions():
        """This function takes no parameter (or arguments)

        The patient user can perform 4 possible actions. From 1 to 4.

        Each time the user is done doing his action,
        he can go back to the menu by clicking on the back button (UI).
        If the user is using a console, he will be sent directly back to the menu (this function)



        """
        print("Your possible actions: ")
        print("1. View your medical procedures")
        print("2. View your profile")
        print("3. View a doctor profile")
        print("4. Change password")
        print("5. Logout")

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
            doctor_name = input(
                " Enter the surname of the doctor you want to view the profile: "
            )
            doctor_profile = user_service.get_doctor_by_name(doctor_name)
            print(doctor_profile)

            Actions.patient_actions()

        elif choice == "4":
            user = input("Username: ").strip()
            pw = getpass.getpass("Your currend Password: ")
            pw = User.hash_password(pw)
            auth.reset_password(user, pw)
            Actions.patient_actions()

        elif choice == "5":  # already implemented in the ui
            auth.logout()  # Logout

        else:
            print("Invalid please choose one of the above possibles actions")
            print()
