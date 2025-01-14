
#from csv import Error

from user import admins, users
import getpass

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
    print("\n1. View all users")
    print("\n3. Logout")
    print("\n4. Change password") ## added by Nantequiou

    
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
    print("\n2. Logout")
    print("\n3. Change password") ## added by Nantequiou
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

        reset_password() ## added by Nantequiou

def patient_actions():
    print("Your possible actions: ")
    print("\n1. View your medical record")
    print("\n3. Change password") ## added by Nantequiou
    

    print()
    
    choice = input("Choose an action: ")
    if choice == '1':
        print("Folder is empty")
        print()
        patient_actions()
    elif choice == '2':
        logout()
    
    elif choice == '3':
        reset_password() ## added by Nantequiou


def logout():
    print("Logged out successfully.")

if __name__ == "__main__":
    login()
    


def reset_password():   ## added by Nantequiou
    try:
        username= input ("Please Enter your Username:")
        if username not in users:
            raise ValueError("Username not found.")
        
        new_password= getpass.getpass("Enter your new password: ")
        users[username]= new_password
        print("Your password has been reset successfully!")
    except ValueError as error:
        print(error)

def confrm_password():  ## added by Nantequiou
    try:
        print("Please confirm your password")
        password= getpass.getpass("Confirm your new password: ")
        if password not in users:
            raise ValueError("Incorrect password.")
        print("Password confirmed!")
    except ValueError as error:
        print(error)       

