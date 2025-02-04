#from operator import ge
#from sqlite3 import connect
#import pyodbc
import hashlib
#from datetime import datetime
#import re

# connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-CC0D63;DATABASE=LANK;UID=LANK_USER;PWD=Lank1.;TrustServerCertificate=YES'
# connection = pyodbc.connect(connection_string)
# cursor = connection.cursor()

class User:
    def __init__(self, subject_id, firstname, lastname, password, role= 'role', department=None):
        self.subject_id = subject_id
        self.password = self.hash_password(password)
        self.firstname = firstname
        self.lastname = lastname
        self.role = role
        self.department = department

    @staticmethod
    def get_id(subject_id):        
        return subject_id

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

class Admin(User):
    def __init__(self, subject_id, password, firstname, lastname):
        super().__init__(subject_id, firstname, lastname, password, role='admin')

class Patient(User):
    def __init__(self, subject_id, password, firstname, lastname):
        super().__init__(subject_id, password, firstname, lastname, role='patient')

class Doctor(User):
    def __init__(self, subject_id, password, firstname, lastname, department):
        super().__init__(subject_id, password, firstname, lastname, role='doctor', department=department)

