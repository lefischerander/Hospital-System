import getpass
from test_class_login import AuthSystem

def main():
    auth = AuthSystem()
    while True:
        action = input("Möchten Sie sich anmelden oder abmelden? (login = 1, logout = 2, exit = 3): ").strip().lower()

        if action == "3":
            break
        elif action == "1":
            username = input("Benutzername: ").strip()
            password = getpass.getpass("Passwort: ").strip()
            auth.login(username, password)
        elif action == "2":
            auth.logout(username)
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")


    

if __name__ == "__main__":
    main()