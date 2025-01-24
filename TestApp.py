##import re
from operator import ge
from sqlite3 import connect
import pyodbc
import hashlib
from datetime import datetime
import re

connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-CC0D63;DATABASE=LANK;UID=LANK_USER;PWD=Lank1.;TrustServerCertificate=YES'

class User:
    def __init__(self, subject_id):
        self.subject_id = subject_id
    
    def get_id(self):        
        return self.subject_id
    
    def create_user(self, creator, user):
        if creator.user_type == 'admin' or 'doctor':
            self.users.append(user)
            return user 
        ##elif creator.user_type == 'doctor':
            ##self.users.appends(user)
            ##return user
    
    def create_admin(self):
        admin_user= User("Kolbek","Konstantin", "admin")
        self.users.append(admin_user)
        return admin_user
    
    def get_user_by_name(self, firstname, surname, subject_id):
        try:
            connection= pyodbc.connect(connection_string)
            cursor= connection.cursor()
            
            cursor.execute("select  * from login_data where login_data.subject_id = ?", subject_id)
            rows= cursor.fetchall()
            if not rows:
                raise Exception("User not found")

            user = rows[0]

            if user.role == 'admin':
                cursor.exectue("select * from patients where patients.subject_id = ?", user.subject_id)
                patient_info = cursor.fetchall()
                cursor.execute("select * from doctors where doctors.subject_id = ?", user.subject_id)
                doctor_info = cursor.fetchall()
                return Admin(user.subject_id, patient_info, doctor_info)
            elif user.role == 'doctor':
                cursor.execute("select * from patients where patients.subject_id = ?", user.subject_id)
                rows = cursor.fetchall()
                doctor = rows[0]
                return Doctor(user.subject_id, doctor)
            elif user.role == 'patient':
                cursor.execute("select * from patients where patients.subject_id = ?", user.subject_id)
                rows = cursor.fetchall()
                patient = rows[0]
                return Patient(user.subject_id, patient)
        
        except Exception as Error:
            print("User not found: ", Error)
            return None
    
    def create_department(self, department_name):
        try:
            if self.get_role_by_id(self.get_id()) != 'admin': #Role Check
                raise PermissionError("Only admins can create departments") 
            
            
            connection= pyodbc.connect(connection_string)  #Database connection
            cursor = connection.cursor()                   

            cursor.execute("insert into departements(name) values(?)", (department_name))#Prepare the SQL querey to insert  a new departmets table

            connection.commit() #Commit the changes to the database

            cursor.close()
            connection.close()

            print(f"Department {department_name} created succesfully.")
        except PermissionError as pe:
            print( pe)  
        except Exception as Error:
            print("Error creating department: ", Error)

    def delete_department(self, department_name):
        try:
            if self.get_role_by_id(self.get_id()) != 'admin': #Role Check
                raise PermissionError("Only admins can delte departments")
        
            connection= pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute("delete from departments where departments.name = ?", department_name)

        except PermissionError as pe:
           print(pe)
        except Exception as Error:
            print("Error deleting department: ", Error)
    

        
        
            
            


    def create_role(self, role_name):
        try:
            if self.get_role_by_id(self.get_id()) != 'admin':
                raise Exception("Only admins can create roles")
            
            connection= pyodbc.connect(connection_string)
            cursor = connection.cursor()

            cursor.execute("insert into roles(name) values(?)", (role_name))

            connection.commit()

            cursor.close()
            connection.close()

            print(f"Role {role_name} created succesfully.")
        except Exception as Error:
            print("Error creating role: ", Error)
    
    
    
    
    def delete_user(self,user):
        self.users.remove(user)
    
    def get_role_by_id(self, subject_id):
        cursor.execute("select role from login_data where login_data.subject_id = ?", subject_id)
        rows = cursor.fetchall()
        return rows[0].role
    
    def get_user_by_id(self, caller_user, id):
        #Fetch user information from the database
        cursor.execute("select * from login_data where login_data.subject_id = ?", id)
        rows = cursor.fetchall()
        user = rows[0]
        
        if user.role == 'admin': #Check if the user is an admin(The admin has the right to see all the information)
            cursor.execute("select *from patients where patients.subject_id= ?", id)
            patient_info = cursor.fetchall()
            cursor.execute("select * from doctors where doctors.subject_id = ?", id)
            doctor_info= cursor.fetchall()
            return Admin(user.subject_id, patient_info, doctor_info)
        
        elif user.role == 'doctor': #Check if the user is a doctor(The doctor has the right to see only the information of patients)
            cursor.execute("select * from patients where patients.subject_id = ?", id)
            rows = cursor.fetchall()
            doctor = rows[0]
            return Doctor(user.subject_id, doctor)
        
        elif user.role == 'patient':# Check if the user is a patient(The patient has the right to see only his/her information)
            if caller_user.get_id() != id:
                raise Exception("Patients can only access their own information")

            cursor.execute("selct * from patients where patients.subject_id= ?", id)
            rows = cursor.fetchall()
            doctor = rows[0]
            return Patient(user.subject_id, doctor)
    
    def transfer(self, patient, department):
        try: 
            if self.get_role_by_id(self.get_id()) != 'admin' and self.get_role_by_id(self.get_id()) != 'doctor':
                raise Exception("Only admins and doctors can transfer patients")
        
            connection= pyodbc.connect(connection_string)
            cursor= connection.cursor()
        except Exception as Error:
            print("Error transferring patient: ", Error)
        
        cursor.execute("update patients set department= ? where patients.subject_id = ?", department, patient.get_id())

    

class Doctor(User):
    def __init__(self, subject_id, gender, firstname, lastname, department):
        super.__init__(subject_id)
        self.gender = gender
        self.firstname = firstname
        self.lastname = lastname
        self.department = department
    
    def get_role_by_id(self, subject_id):
        return super().get_role_by_id(subject_id)
    
    def get_id(self):
        return super().get_id()
    
    def get_user_by_id(self, caller_user, id):
        return super().get_user_by_id(caller_user, id)
            
                
       
                
        
        ##return super().get_user_by_id(caller_user, id)
    
    def get_department(self):
        return self.department
    
    def add_patient(self, patient):
        cursor.execute("insert into patients(subject_id) values(?)", patient.get_id())
    
    def remove_patient(self, patient):
        cursor.execute("delete from patients where patients.subject_id = ?", patient.get_id())
    
    def add_prescriptions(self, patient, prescription):
        cursor.execute("insert into prescriptions(prescription) values(?)", prescription)
    
    def remove_prescriptions(self, patient, prescription):
        cursor.execute("delete from prescriptions where prescriptions.prescription = ?", prescription)
    
    def add_diagnosis(self, patient, diagnosis):
        cursor.execute("insert into diagnosis(diagnosis) values(?)", diagnosis)
    
    def remove_diagnosis(self, patient, diagnosis):
        cursor.execute("delete from diagnosis where diagnosis.diagnosis = ?", diagnosis)
    
    def yearly_report(self, year):
        cursor.execute("select * from patients where patients.anchor_year_group = ?", year)
        rows = cursor.fetchall()
        return rows
    
    def medical_history(self, patient):
        cursor.execute("select * from diagnosis where diagnosis.subject_id = ?", patient.get_id())
        rows = cursor.fetchall()
        return rows
    
    def treatment_history(self, patient):
        cursor.execute("select * from prescriptions where prescriptions.subject_id = ?", patient.get_id())
        rows = cursor.fetchall()
        return rows
    
    def write_report(self, patient, report):
        cursor.execute("insert into reports(report) values(?)", report)
    
    def get_report(self, patient):
        cursor.execute("select * from reports where reports.subject_id = ?", patient.get_id())
        rows = cursor.fetchall()
        return rows
    
    def remove_report(self, patient, report):
        cursor.execute("delete from reports where reports.report = ?", report)
    
    def get_diagnosis(self, patient):
        cursor.execute("select * from diagnosis where diagnosis.subject_id = ?", patient.get_id())
        rows = cursor.fetchall()
        return rows 
    def get_prescriptions(self, patient):
        cursor.execute("select * from prescriptions where prescriptions.subject_id = ?", patient.get_id())
        rows = cursor.fetchall()
        return rows
    
    def admisson(self, patient):
        cursor.execute("insert into admisson(admisson) values(?)", patient.get_id())
    
    def transfer(self, patient, department):
        cursor.execute("update patients set department = ? where patients.subject_id = ?", department, patient.get_id())
    
    

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


def validate_email(email): #Function to validate email
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email): #check if the email is valid
        return False

def validate_password(password):
    if not re.match(r"[A-Za-z0-9@#$%^&+=]{8,}", password):
        return False
    return True  


DRIVER = '{ODBC Driver 18 for SQL Server}'
SERVER = 'LAPTOP-CC0D63'
DATABASE = 'lank'
USERNAME = 'Nante'
PASSWORD = 'lank1.'

conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-CC0D63;DATABASE=LANK;UID=LANK_USER;PWD=Lank1.;TrustServerCertificate=YES')

cursor = conn.cursor()


action = input("Enter action: (Use R/r for registration or L/l to log in) ") .strip() .lower()

    
    
if action == "L" or action == "l": ## Login 
    try:
        userIn = input("Enter Username: ").strip()
        passwordIn = input("Enter password: ").strip()
        
       
    
        cursor.execute("select password from login_data where login_data.subject_id = ?", userIn)
        rows = cursor.fetchall()
    
        if not rows:
            raise ValueError("User not found")
    ## Validate the password
        stored_password = rows[0].password
        if stored_password != hashlib.sha1(passwordIn.encode()).hexdigest(): # Compare the password with the stored password
            raise ValueError("Invalid password")
    
        cursor.execute("select * from patients where patients.subject_id = ?", userIn)
        user_details = cursor.fetchone()
        if not user_details:
            raise ValueError("User details not found")

        active_user = Patient(user_details.subject_id, user_details.gender, user_details.anchor_age, user_details.anchor_year_group, user_details.firstname, user_details.surname, user_details.email)
        print("Welcome " + user_details.firstname + " " + user_details.surname)
    
    except ValueError as ve:
      print(ve)
    
    except pyodbc.Error as e:
        print(f"Database error: {e}")

    
    
    
elif action == "R" or action =="r": ## Registration
    try:
        email_in = input("Enter email: ")
        if not validate_email(email_in):
            raise ValueError("Please enteer a valid email") 
    
    
    
        password_in = input("Enter password: ")
        if not validate_password(password_in):
            raise ValueError("Password must be at least 8 characters long and contain at least one special character")
    
    
    
        firstname_in = input("Enter firstname: ")
        if firstname_in == "":
            raise ValueError("Please enter your firstname")
    
    
        surname_in = input("Enter surname: ")
        if surname_in == "":
            raise ValueError("Please enter your surname")
    
    
        gender_in = input("Enter gender: ")
        if gender_in not in [ "M" , "F" , "D"]:
            raise ValueError("Please enter a valid Gender (M/F/D)")
    
    
    
        age_in = input("Enter age: ")
        if  not age_in.isdigit(): #The input is a digit
            raise ValueError("Please enter a valid age")
        
        age = int(age_in) #Convert the age input to an integer
        

        if not (0 <= age <= 120): #The age must be between 0 and 120
            raise ValueError("Please enter a valid age")
    
    except ValueError as ve:
        print(ve)
    
    anchor_year_dict = {"2017-2019": 2160, "2018 - 2020": 2161, "2019 - 2021": 2162, "2020 - 2022": 2163, "2021 - 2023": 2164, "2022 - 2024": 2165, "2023 - 2025": 2166, "2024 - 2026": 2167}
    ## No clue what anchor_year and anchor_year_group is supposed to be and how it's calculated but it's not 
    ## required for our use-cases
    anchor_year = anchor_year_dict["" + str(datetime.now().year-1) + " - " + str(datetime.now().year + 1)] 
    anchor_year_group = str(datetime.now().year-1) + " - " + str(datetime.now().year + 1)
    subject_id = cursor.execute("select top 1 subject_id from patients order by subject_id desc").fetchall()[0].subject_id + 1
    cursor.execute("insert into patients (subject_id, gender, anchor_age, anchor_year, anchor_year_group, firstname, surname) values (?,?,?,?,?,?,?)", subject_id, gender_in, age_in, anchor_year, anchor_year_group, firstname_in, surname_in)
    cursor.execute("insert into login_data (subject_id, email, password, role) values (?,?,?, 'U')", subject_id, email_in, hashlib.sha1(password_in.encode()).hexdigest())
    cursor.commit()
