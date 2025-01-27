from login_final import reset_password, logout
from user import admins, users

def admin_actions():
    # Actions for the admin
    print("Your possible actions: ")
    print()
    print("1. View all users")
    print("\n1. View all users")
    print("\n3. Logout")
    print("\n4. Change password") ## added by Nantequiou

    
    choice = input("Choose an action: ")
    if choice == '1':
        print("Users: ", users) # Show all users
        print()
        admin_actions() # Return to admin actions
    elif choice == '2':
        username = input("Username: ")
        user = users.get(username)  # Show specific user
        print(user)
        print()
        admin_actions() # Return to admin actions
    elif choice == '3':
        logout()    # Logout

def doktor_actions():
    # Actions for the doctor
    print("Your possible actions: ")
    print("\n2. Logout")
    print("\n3. Change password") ## added by Nantequiou
    print()
    
    choice = input("Choose an action: ")
    if choice == '1':
        username = input("Patient: ")
        patient = users.get(username)   # Show patient data
        if patient:
            if patient['role'] == 'patient':
                print("Folder is empty")
                print()
            else:
                print("User is not a patient!") # Check if user is a patient
                print()
        else:
            print("Such patient doesn't exist!")    # Check if patient exists
            print()
        doktor_actions()    # Return to doctor actions

    elif choice == '2':
        logout()    # Logout

        reset_password() ## added by Nantequiou

        reset_password() ## added by Nantequiou

def patient_actions():
    # Actions for the patient
    print("Your possible actions: ")
    print("\n1. View your medical record")
    print("\n3. Change password") ## added by Nantequiou
    

    print()
    
    choice = input("Choose an action: ")
    if choice == '1':
        print("Folder is empty")    # Show empty directory (no medical record)
        print()
        patient_actions()   # Return to patient actions
    elif choice == '2':
        logout()    # Logout
    
    elif choice == '3':
        reset_password() ## added by Nantequiou