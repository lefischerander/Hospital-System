from user import admins, users  # Import user and admin data
import getpass  # Import getpass for hidden password input
import hashlib

def login():
    # Prompt for username and password
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    pw = hashlib.sha256(password.encode()).hexdigest()
    user = users.get(username) or admins.get(username)  # Check if user exists
    # Check if password is correct
    if user and user['password'] == pw:
        print()
        print(f"Login successful! Welcome, {username}.")
        print(f"You are {user['role']} in this hospital.")
        # Execute different actions based on user role
        if user['role'] == 'admin':
            print()
            admin_actions()
        elif user['role'] == 'doktor':
            print(f"Your department: {user['department']}")
            print()
            doktor_actions()
        elif user['role'] == 'patient':
            print()
            patient_actions()
    else:
        print("Invalid username or password!")  # Output if login data is incorrect

def admin_actions():
    # Actions for the admin
    print("Your possible actions: ")
    print()
    print("1. View all users")
    print("2. View a specific user")
    print("3. Logout")
    print()
    
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
    print("1. View a patient")
    print("2. Logout")
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

def patient_actions():
    # Actions for the patient
    print("Your possible actions: ")
    print("1. View your medical record")
    print("2. Logout")
    print()
    
    choice = input("Choose an action: ")
    if choice == '1':
        print("Folder is empty")    # Show empty directory (no medical record)
        print()
        patient_actions()   # Return to patient actions
    elif choice == '2':
        logout()    # Logout

def logout():
    print("Logged out successfully.")   # Success message after logout

if __name__ == "__main__":
    login() # Start the login process