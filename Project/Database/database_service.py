import pyodbc
from Database.db_access import connection_string
import sqlalchemy as sa
import pandas as pd
from tkinter import messagebox


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


class User_service:
    """This class is responsible for handling all database operations"""

    def __init__(self):
        """Initializes the connection string to the database

        Parameters:
        connection_string: str
            The connection string to the database
        """
        self.connection_string = connection_string
        self.connection_url = sa.URL.create(
            "mssql+pyodbc", query={"odbc_connect": connection_string}
        )

    def read_table_sa(self, table_name):
        """Reads an entire table from the database with SQLAlchemy and fills a pandas DataFrame with the data

        Args:
            table_name (str): The name of the table to be read

        Returns:
            DataFrame: The table data in a pandas DataFrame
        """
        engine = sa.create_engine(self.connection_url)
        with engine.begin() as conn:
            df = pd.read_sql_query(sa.text(f"SELECT * FROM {table_name}"), conn)

        return df

    def read_sa_query(self, query):
        """Queries the database with SQLAlchemy and fills a pandas DataFrame with the data

        Args:
            query (str): The query to be executed

        Returns:
            DataFrame: The table data in a pandas DataFrame
        """
        engine = sa.create_engine(self.connection_url)
        with engine.begin() as conn:
            df = pd.read_sql_query(sa.text(query), conn)

        return df

    def get_admin_email(self):
        """Gets the admin's email from the database

        Returns:
            str: Email of the admin
        """
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute(f"select email from {ADMINS}")
            email = cursor.fetchone()[0]
            cursor.close()
            connection.close()
            return email
        except Exception as e:
            print("No Admin found. See:", e)

    def delete_user(self, subject_id):  ##low priority
        """Deletes a user from the database based on the user's subject ID

        Args:
            user (int): the to-be-deleted user's subject ID

        Raises:
            Exception: If the user is not an admin
            Exception: If the user is not found in the database or another error occurs

        Returns:
            bool: False if the user doesn't exist, True if an existing user got deleted
        """
        try:
            checked_id = self.check_id(subject_id)

            if checked_id is None:
                messagebox.showerror("Error", "User doesn't exist.")
                return False

            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute(
                f"DELETE FROM {LOGIN_DATA} WHERE subject_id = ?", int(subject_id)
            )

            connection.commit()

            cursor.close()
            connection.close()
            print(f"User: {subject_id} deleted successfully")
            return True
        except Exception as e:
            print("Error:", e)

    def get_role_by_id(self, id):
        """
        Gets the role of a user based on the user's subject ID

        Args:
            id (int): the user's subject ID

        Returns:
            str: the role of the user

        Raises:
            Exception: If the user is not found in the database or another error occurs
        """
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute(f"select role from {LOGIN_DATA} where subject_id = ?", id)
            role = cursor.fetchone()[0]
            cursor.close()
            connection.close()
            return role
        except Exception as e:
            print("Error: user not found", e)

   

    def get_doctor_by_name(self, surname):
        """Gets a doctor's information based on the doctor's surname

        Args:
            surname (str): The doctor's surname

        Returns:
            pyodbc.row: The row containing the doctor's information (pyodbc object)

        Raises:
            Exception: If the doctor is not found in the database or another error occurs
        """
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute(
                f"select firstname, surname, department, age from {DOCTORS} where surname = ?",
                surname,
            )
            doctor = cursor.fetchone()
            cursor.close()
            connection.close()
            return doctor
        except Exception as e:
            print("Error: user not found ", e)

    def get_your_profile(self, subject_id):
        """
        Gets the profile of a user based on the user's subject ID

        Args:
            subject_id (int): the user's subject ID

        Returns:
            pyodbc.row: the row containing the user's profile (pyodbc object)

        Raises:
            Exception: If the user is not found in the database or another error occurs
        """
        try:
            if self.get_role_by_id(subject_id) == "Patient":
                connection = pyodbc.connect(self.connection_string)
                cursor = connection.cursor()
                query = f"""
                SELECT subject_id, gender, anchor_age, firstname, surname 
                FROM {PATIENTS} 
                WHERE subject_id = ?
                """
                cursor.execute(query, subject_id)
                result = cursor.fetchone()
                cursor.close()
                connection.close()
                return result
            elif self.get_role_by_id(subject_id) == "Doctor":
                connection = pyodbc.connect(self.connection_string)
                cursor = connection.cursor()
                query = f"""
                SELECT subject_id, firstname, surname, department, age 
                FROM {DOCTORS} 
                WHERE subject_id = ?
                """
                cursor.execute(query, subject_id)
                result = cursor.fetchone()
                cursor.close()
                connection.close()
                return result

            else:
                return "Error fetching profile ,please retry"
        except Exception as e:
            print("Error fetching profile: ", e)
            return None

    def create_user(
        self, subject_id, password, role, firstname, surname
    ):  ##low priority
        """Creates a new user in the database

        Args:
            subject_id (int): The subject ID of the new user
            password (str): The password of the new user
            role (str): The role of the new user (e.g., 'admin', 'doctor', 'patient')
            firstname (str): The first name of the new user
            surname (str): The surname of the new user

        Raises:
            Exception: If any error occurs during the process
        """
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute(
                f"INSERT INTO {LOGIN_DATA} (subject_id, password, role, firstname, surname) VALUES (?, ?, ?, ?, ?)",
                subject_id,
                password,
                role,
                firstname,
                surname,
            )
            connection.commit()
            cursor.close()
            connection.close()
            print(f"User {subject_id} created successfully")
        except Exception as e:
            print("Error creating user: ", e)

    
    def check_id(self, subject_id):  # just for patients
        """
        This method is used to verify if a input subject_id exists in the database based on the subject_id.
        The patient user is most likely to be checked.

        Args:
            subject_id (int): the user's subject ID

        Returns:
            none if the entered subject_id does not exist in the database

        Raises:
            Exception: any database inconvenience
        """
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()

            cursor.execute(
                f"select subject_id from {LOGIN_DATA} where subject_id= ?",
                subject_id,
            )

            checked_id = cursor.fetchone()

            if checked_id is None:
                return None

            connection.commit()
            cursor.close()
            connection.close()

            return "Yay DB found the user!"

        except Exception as e:
            print("Oups error: ", e)
            return None
    #unused
    def read_d_icd_diagnoses(self, icd_code):
        """This method is used to read the d_icd_diagnoses table and return the long title of the icd code entered by the user.

        Returns:
            str: The long title of the icd code entered by the user.
        """
        df = self.us.read_table_sa("d_icd_diagnoses")
        try:
            # Get the long title of the icd code
            icd_code = df[df["icd_code"].astype(str) == icd_code][
                ["icd_code", "icd_version", "long_title"]
            ]
            return icd_code.to_string(index=False)
        except Exception as e:
            print("Invalid icd code.", e)
            User_service.read_d_icd_diagnoses()  # Call the method again if the icd code is invalid

    def create_diagnosis(self, patient_id, caller_id, icd_code):
        """If the user is a doctor, adds a diagnosis to a patient's record

        Args:
            patient_id (int): id of the patient
            icd_code (int): code of the icd diagnosis
            icd_version (str): version of the icd_code (9 or 10)

        Raises:
            Exception: If the patient with the given ID can't be found
            Exception: If any other Error happens during the process

        Returns:
            bool: False if the patient ID or ICD Code doesn't exist, True if the diagnosis was created
        """

        try:
            user_role = self.get_role_by_id(caller_id)

            if user_role != "Doctor":
                raise Exception("Only doctors can add diagnoses")

            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()

            check_id = self.check_id(patient_id)

            if check_id is None:
                messagebox.showerror("Error", "This patient ID doesn't exist.")
                return False

            diagnosis_added = self.read_sa_query(
                f"SELECT * FROM {DIAGNOSES_DESC} WHERE icd_code = '{icd_code}'"
            )

            if diagnosis_added.empty:
                messagebox.showerror("Error", "This ICD Code doesn't exist.")
                return False
            

            # the function finds the most recent hospital admission (hadm_id) for the given patient_id then,
            #it queries the ADMISSIONS table, ordering by hadm_id in descending order, and retrieves the latest hadm_id.
            hadm_id = cursor.execute(
                f"select hadm_id from {ADMISSIONS} where subject_id = ? order by hadm_id desc",
                patient_id,
            ).fetchone()[0]
            try:
                
                seq_num = (
                    cursor.execute(
                        "select max(seq_num) from diagnoses_icd where subject_id = ? and hadm_id = ?",
                        patient_id,
                        hadm_id,
                    ).fetchone()[0]
                    + 1
                )
            #If no previous diagnosis exists, it sets seq_num = 1.
            except pyodbc.Error:
                seq_num = 1
            
            #  these new variable store the selected first row of the DataFrame and s
            icd_code = str(diagnosis_added.iloc[0]["icd_code"]) 
            icd_version = str(diagnosis_added.iloc[0]["icd_version"])

            cursor.execute(
                "insert into diagnoses_icd (subject_id, hadm_id, seq_num, icd_code, icd_version) values(?, ?, ?, ?, ?)",
                str(patient_id),
                str(hadm_id),
                str(seq_num),
                str(icd_code),
                str(icd_version),
            )

            connection.commit()
            cursor.close()
            connection.close()

            messagebox.showinfo(title="Success", message="Diagnosis added successfully")

        except Exception as e:
            print("Error:  ", e)
            return False

    def get_patient_profile(self, subject_id):  # dod time must be string
        """Gets a patient's profile based on the patient's subject_id.

        Before making any connection with the database, the entered subject_id needs to be checked first.

        Args:
            entered subject_id

        Returns:
            pyodbc.row: the row containing the user's profile (pyodbc object)
            bool: If the user doesn't exist

        Raises:
            Exception: if the checked subject_id does not exist on the database or if the database could not fetch the patient profile

        """
        try:
            check_id = self.check_id(subject_id)
            if check_id is None:
                messagebox.showerror("Error", "This patient ID doesn't exist.")
                return False

            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            query = "SELECT * FROM patients WHERE p.subject_id = ?"
            cursor.execute(query, subject_id)
            result = cursor.fetchone()[0]
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            print("Error fetching patient profile: ", e)
            return None

    def get_diagnosis(self, patient_id, caller_id):
        """Gets the diagnosis of a patient based on the patient's subject ID

        Args:
            patient_id (int): The patient's subject ID

        Returns:
            pyodbc.row: The row containing the patient's diagnosis (pyodbc object)
            None: If an error occurs, nothing is returned
        """
        try:
            user_role = self.get_role_by_id(caller_id)
            if (
                user_role == "Doctor"
                or user_role == "admin"
                or (user_role == "Patient" and caller_id == patient_id)
            ):
                connection = pyodbc.connect(self.connection_string)
                cursor = connection.cursor()
                cursor.execute(
                    "select d.subject_id, d.hadm_id, d.icd_code from diagnoses_icd AS d INNER JOIN d_icd_diagnoses AS dc on d.icd_code = dc.icd_code where d.subject_id = ?",
                    patient_id,
                )
                diagnosis = cursor.fetchone()
                cursor.close()
                connection.close()
                return diagnosis
        except Exception as e:
            print("Error: user not found ", e)
            return None

    def get_procedures_by_subject_id(self, subject_id, caller_id):
        (
            """Reads the procedures of a patient based on the patient's subject ID

        Args:
            subject_id (int): The patient's subject ID
            caller_id (int): The logged in user's subject ID 

        Raises:
            Exception: If the user is not a doctor or searches for another patient's procedures

        Returns:
            pyodbc.row: The row containing the patient's procedures (pyodbc object)
        """
            """"""
        )
        try:
            user_role = self.get_role_by_id(caller_id)

            if user_role == "Doctor" or (
                user_role == "Patient" and caller_id == subject_id
            ):
                connection = pyodbc.connect(self.connection_string)
                cursor = connection.cursor()
                query = f"""
                    SELECT p.subject_id, p.hadm_id, p.seq_num, p.chartdate, p.icd_code, p.icd_version, dp.long_title 
                    FROM {PROCEDURES} AS p
                    INNER JOIN {PROCEDURES_DESC} AS dp ON p.icd_code = dp.icd_code
                    WHERE p.subject_id = ?
                    ORDER BY p.seq_num
                """
                cursor.execute(query, subject_id)
                results = cursor.fetchall()
                cursor.close()
                connection.close()

                return results
            else:
                raise Exception(" Patients can only view their own medical procedures")
        except Exception as e:
            print("Error fetching procedures: ", e)
            return None

   

    def view_all_users(self):
        """Sees all the users present in the database.

        Returns:
               pyodbc.row: The row containing the users in the database (pyodbc object)

        """
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute(f"select subject_id, role from {LOGIN_DATA}")
            users = cursor.fetchall()
            cursor.close()
            connection.close()
            return users
        except pyodbc as database_error:
            print("Error fetching all users: ", database_error)
            return None

   