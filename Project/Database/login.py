from tkinter import messagebox
import pyodbc
from Backend.user import User
from Database.db_access import connection_string

# database tables
LOGIN_DATA = "login_data"
DOCTORS = "doctors"
PATIENTS = "patients"
DIAGNOSES = "diagnoses_icd"
PROCEDURES = "procedures_icd"
OMR = "omr"
DIAGNOSES_DESC = "d_icd_diagnoses"
PROCEDURES_DESC = "d_icd_procedures"
EMAR = "emar"
ADMISSIONS = "admissions"
PHARMACY = "pharmacy"
ADMINS = "admins"


class AuthSystem:
    
    def __init__(self):
        self.users = []
        self.logged_in = False

    def check_user(self, subject_id, password):
   
        """Checks if the user exists in the database.

        Args:
            subject_id (int): The subject id of the user
            password (str): The password of the user

        Returns:
            list: User data if the user exists, None otherwise
        """
        
        #Database queries
        try:
            # Connecting to the database
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            
            # This queries the login table to check if a user with the given subject_id and password exists
            cursor.execute(
                f"select password, subject_id, role FROM {LOGIN_DATA} WHERE subject_id = ? AND password = ?",
                subject_id,
                password,
            )
            # The result is stored in a list
            self.users = cursor.fetchall()
            
            # Close the connection 
            cursor.close()
            connection.close()
        
        # Catches database connection error
        except pyodbc.Error as db_error:
            print(f" Db error: {db_error}")
        except Exception as e:
            print(f"An unexpected error occured: {e}")
        
        # Store a single user if found in self.users.
        temp_user = None
        # This list will store the user's final information before returning it.
        # Convert a database row (tuple) into a list so it can be modified later (if necessary)
        user = []
        
        # Check the given subject_id and comparing it
        for i in self.users:
            if str(i[0] == str(subject_id)):
               
                # if a match is found we set temp_user to that user
                temp_user = i
                
                # we exist the loop once a match is found
                break
        
        # Check if the tuple is not empty
        if temp_user:
            # Copy the elements inside temp_user into the user list
            for i in temp_user:
                user.append(i)
            
            # If the user is a Doctor, the program fetches the first name, surname, and department from the DOCTORS table.
            if user[2] == "Doctor":
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                cursor.execute(
                    f"""select d.firstname, d.surname, d.department FROM {DOCTORS} AS d 
                    INNER JOIN {LOGIN_DATA} AS l ON d.subject_id = l.subject_id 
                    WHERE d.subject_id = ? """,
                    subject_id,
                )
                result = cursor.fetchall()[0]
                cursor.close()
                connection.close()
                for r in result:
                    user.append(r)
            
            # If the user is a Patient, the program fetches the first name, surname, and department from the PATIENTS table.
            elif user[2] == "Patient":
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                cursor.execute(
                    f"""select p.firstname, p.surname FROM {PATIENTS} AS p
                    INNER JOIN {LOGIN_DATA} AS l ON p.subject_id = l.subject_id 
                    WHERE p.subject_id = ? """,
                    subject_id,
                )
                result = cursor.fetchall()[0]
                cursor.close()
                connection.close()
                for r in result:
                    user.append(r)
            # If the user is an Admin, the program fetches the first name, surname, and department from the ADMINS table.
            elif user[2] == "Admin":
                connection = pyodbc.connect(connection_string)
                cursor = connection.cursor()
                cursor.execute(
                    f"""select a.firstname, a.surname FROM {ADMINS} AS a 
                    INNER JOIN {LOGIN_DATA} AS l ON a.subject_id = l.subject_id 
                    WHERE a.subject_id = ? """,
                    subject_id,
                )
                result = cursor.fetchall()[0]
                cursor.close()
                connection.close()
                for r in result:
                    user.append(r)
        
        # If the user remains empty, it means no valid user was found
        if user is None:
            print("Invalid username or password.")
        return user

   
    def login(self, subject_id, password):
        """Logs the user into the system if the credentials are correct.

        Args:
            subject_id (int): The user's subject id
            password (str): The user's password
        """
        user = self.check_user(subject_id, password)
        if user:
            print(user)
            print(f"\nLogin successful! Welcome, {user[3]} {user[4]}.")
            self.logged_in = True
            user_role = user[2]
            
            # We thought, it would make more sense for the Doctor to always know in which department he was working in 
            if user_role == "Doctor":
                print(f"Your role in this hospital: {user_role}")
                print(f"Your department: {user[5]}")
            else:
                print(f"Your role in this hospital: {user_role}")

    def reset_password(self, subject_id, password, new_password, confirm_new_password):
        """Resets the user's password.

        Args:
            subject_id (int): The user's subject id
            password (str): The user's password
            new_password (str): The user's new password
            confirm_new_password (str): The user's new password confirmation

        Raises:
            ValueError: If the password doesn't meet the requirements
        """
        
        user = self.check_user(subject_id, password)
        if user is None:
            messagebox.showerror("Error", "Wrong User ID")
            return False

        if new_password != confirm_new_password:
            messagebox.showerror("Error", "Passwords do not match")
            return False

        h_new_password = User.hash_password(new_password)
        if user[0] == h_new_password:
            messagebox.showerror(
                "Error", "New Password cannot be the same as the old one"
            )
            return False

        # If the input of the user is successfull then the programm will store the new password
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute(
                f"UPDATE {LOGIN_DATA} SET password = ? WHERE subject_id = ?",
                h_new_password,
                subject_id,
            )
            cursor.close()
            connection.commit()
            connection.close()
            messagebox.showinfo("Success", "Password changed successfully!")
            return True
            # break
        except ValueError as error:
            messagebox.showerror(error, "Password has not been changed")
            return False

    # def Autologout(self, timeout_minutes = 4):
