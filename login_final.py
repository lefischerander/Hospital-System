from user import admins, users
import getpass
#Test
def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    user = users.get(username) or admins.get(username)

    if user and user['password'] == password:
        print()
        print(f"Login successful! Welcome, {username}.")
        print(f"You are {user['role']} in this hospital.")
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
        print("Invalid username or password!")

def admin_actions():
    print("Your possible actions: ")
    print()
    print("1. View all users")
    print("2. View a specific user")
    print("3. Logout")
    print()
    
    choice = input("Choose an action: ")
    if choice == '1':
        print("Users: ", users)
        print()
        admin_actions()
    elif choice == '2':
        username = input("Username: ")
        user = users.get(username)
        print(user)
        print()
        admin_actions()
    elif choice == '3':
        logout()

def doktor_actions():
    print("Your possible actions: ")
    print("1. View a patient")
    print("2. Logout")
    print()
    
    choice = input("Choose an action: ")
    if choice == '1':
        username = input("Patient: ")
        patient = users.get(username)
        if patient:
            if patient['role'] == 'patient':
                print("Folder is empty")
                print()
            else:
                print("User is not a patient!")
                print()
        else:
            print("Such patient doesn't exist!")
            print()
        doktor_actions()
    elif choice == '2':
        logout()

def patient_actions():
    print("Your possible actions: ")
    print("1. View your medical record")
    print("2. Logout")
    print()
    
    choice = input("Choose an action: ")
    if choice == '1':
        print("Folder is empty")
        print()
        patient_actions()
    elif choice == '2':
        logout()

def logout():
    print("Logged out successfully.")

if __name__ == "__main__":
    login()