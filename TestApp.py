import pyodbc
import hashlib

class User:
    def __init__(self, subject_id):
        self.subject_id = subject_id

class Doctor(User):
    def __init__(self, subject_id, gender, firstname, lastname, department):
        super.__init__(subject_id)
        self.gender = gender
        self.firstname = firstname
        self.lastname = lastname
        self.department = department

class Patient(User):
    def __init__(self, subject_id, gender, anchor_age, anchor_year_group, firstname, lastname, email):
        super().__init__(subject_id)
        self.gender = gender
        self.anchor_age = anchor_age
        self.anchor_year_group = anchor_year_group
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def profile(self):
        print("Oho mein Profil!")

class Admin(User):
    def __init__(self, subject_id):
        super().__init__(subject_id)


DRIVER = '{ODBC Driver 18 for SQL Server}'
SERVER = 'LAPTOP-CC0D63'
DATABASE = 'lank'
USERNAME = 'Nante'
PASSWORD = 'lank1.'

conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-CC0D63;DATABASE=lank;UID=Nante;PWD=lank1.;TrustServerCertificate=YES')

cursor = conn.cursor()

action = input("Enter action: ") 
if action == "L":
    userIn = input("Enter Username: ")
    passwordIn = input("Enter password: ")

    cursor.execute("select password from login_data where login_data.subject_id = ?", userIn)

    rows = cursor.fetchall()

    user = rows[0]

    if hashlib.sha1(passwordIn.encode()).hexdigest() == user.password:
        print("Welcome")
        cursor.execute("select * from patients inner join login_data On patients.subject_id = login_data.subject_id where patients.subject_id = ?", userIn) 
        rows = cursor.fetchall()
        user = rows[0]
        active_user = Patient(user.subject_id, user.gender, user.anchor_age, user.anchor_year_group, user.firstname, user.surname, user.email)
    else:  
        print("tschüss")

elif action == "R":
    userIn = input("Enter Username: ")
    email = input("Enter email: ")
    






