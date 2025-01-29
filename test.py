from user import User, Admin, Patient, Doctor
import getpass
import hashlib

class AuthSystem:
    def __init__(self):
        self.users = {
            'K.Kolbek': Admin('K.Kolbek', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9'),
            'L.Fischer': Admin('L.Fischer', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9'),
            'N.Razafindraibe': Admin('N.Razafindraibe', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9'),
            'E.Schaefer': Admin('E.Schaefer', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9'),
            '1.1': Patient('1.1', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            '10003400': Patient('10003400', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            '10002428': Patient('10002428', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            '10032725': Patient('10032725', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            '10027445': Patient('10027445', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            '10022281': Patient('10022281', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            '10035631': Patient('10035631', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            '10024043': Patient('10024043', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            '10025612': Patient('10025612', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            '10003046': Patient('10003046', '5ac7b35987b4b0235e42f7c8d85e69bffa03e14d36c1c3855ce11f29678b2a69'),
            'D.Paris': Doctor('D.Paris', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08', 'radiology'),
            'M.Maier': Doctor('M.Maier', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08', 'gastroenterology'),
            'A.Mueller': Doctor('A.Mueller', '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08', 'oncology')
        }
        self.logged_in_users = set()

    def login(self, username, password):
        password = hashlib.sha256(password.encode()).hexdigest()
        if username not in self.users:
            print(f"Benutzer {username} nicht gefunden.")
        elif self.users[username].password != User.hash_password(password):
            print("Falsches Passwort.")
        elif username in self.logged_in_users:
            print(f"Benutzer {username} bereits eingeloggt.")
        else:
            self.logged_in_users.add(username)
            print(f"Benutzer {username} erfolgreich eingeloggt.")

    def logout(self, username):
        if username in self.logged_in_users:
            self.logged_in_users.remove(username)
            print(f"Benutzer {username} erfolgreich ausgeloggt.")
        else:
            print(f"Benutzer {username} ist nicht eingeloggt.")

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
