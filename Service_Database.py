import pyodbc
from db_access import connection_string
import config
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
        """
        try:
            checked_id = self.check_id(subject_id)

            if checked_id is None:
                messagebox.showinfo("User not found")

            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute(
                f"DELETE FROM {LOGIN_DATA} WHERE subject_id = ?", int(subject_id)
            )

            connection.commit()

            cursor.close()
            connection.close()
            print(f"User: {subject_id} deleted successfully")
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

    # def get_id(self, surname):
    #     """Gets a user's subject ID based on the user's surname

    #     Args:
    #         surname (str): The user's surname

    #     Returns:
    #         int: The user's subject ID

    #     Raises:
    #         Exception: If the user is not found in the database or another error occurs
    #     """
    #     try:
    #         connection = pyodbc.connect(self.connection_string)
    #         cursor = connection.cursor()
    #         cursor.execute(
    #             f"select subject_id from {LOGIN_DATA} where surname = ?", surname
    #         )
    #         id = cursor.fetchone()[0]
    #         cursor.close()
    #         connection.close()
    #         return id
    #     except Exception as e:
    #         print("Error: user not found ", e)

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

    def change_password(self, username, password):  # Not necessary
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute(
                "update ? set password = ? where username = ?",
                LOGIN_DATA,
                password,
                username,
            )
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            print("Error changing password: ", e)

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
        """

        try:
            user_role = self.get_role_by_id(caller_id)

            if user_role != "Doctor":
                raise Exception("Only doctors can add diagnoses")

            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()

            check_id = self.check_id(patient_id)

            if check_id is None:
                raise Exception(f"Patient with subject ID {patient_id} not found")

            diagnosis_added = self.read_sa_query(
                f"SELECT * FROM {DIAGNOSES_DESC} WHERE icd_code = '{icd_code}'"
            )

            if diagnosis_added.empty:
                raise Exception("Invalid icd_code. Please retry ")

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
            except pyodbc.Error:
                seq_num = 1
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

            messagebox.showinfo(title="Success", text="Diagnosis added successfully")

        except Exception as e:
            print("Error:  ", e)

    def get_patient_profile(self, subject_id):  # dod time must be string
        """Gets a patient's profile based on the patient's subject_id.

        Before making any connection with the database, the entered subject_id need to be checked first.

        Args:
            entered subject_id

        Returns:
        pyodbc.row: the row containing the user's profile (pyodbc object)

        Raises:
            Exception: if the checked subject_id does not exist on the database
                        if the database could not fetch the patient profile

        """
        try:
            check_id = self.check_id(subject_id)
            if check_id is None:
                raise Exception("The user you input is not on the database")

            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            query = """
                SELECT p.subject_id, p.gender, p.anchor_age, p.firstname, p.surname, p.dod 
                FROM patients AS p
                WHERE p.subject_id = ?
            """
            cursor.execute(query, subject_id)
            result = cursor.fetchone()
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

    # def get_most_recent_weight(self, subject_id):
    #     try:
    #         connection = pyodbc.connect(self.connection_string)
    #         cursor = connection.cursor()
    #         query = """
    #             SELECT TOP 1 *
    #             FROM ?
    #             WHERE subject_id = ? AND result_name LIKE 'Weight%'
    #             ORDER BY chartdate DESC
    #         """
    #         cursor.execute(query, OMR, subject_id)
    #         result = cursor.fetchone()
    #         cursor.close()
    #         connection.close()
    #         return result
    #     except Exception as e:
    #         print("Error fetching most recent weight: ", e)
    #         return None

    # def get_most_recent_height(self, subject_id):
    #     try:
    #         connection = pyodbc.connect(self.connection_string)
    #         cursor = connection.cursor()
    #         query = """
    #             SELECT TOP 1 *
    #             FROM ?
    #             WHERE subject_id = ? AND result_name LIKE 'Height%'
    #             ORDER BY chartdate DESC
    #         """
    #         cursor.execute(query, OMR, subject_id)
    #         result = cursor.fetchone()
    #         cursor.close()
    #         connection.close()
    #         return result
    #     except Exception as e:
    #         print("Error fetching most recent height: ", e)
    #         return None

    # def get_most_recent_bmi(self, subject_id):
    #     try:
    #         connection = pyodbc.connect(self.connection_string)
    #         cursor = connection.cursor()
    #         query = """
    #             SELECT TOP 1 *
    #             FROM ?
    #             WHERE subject_id = ? AND result_name LIKE 'BMI%'
    #             ORDER BY chartdate DESC
    #         """
    #         cursor.execute(query, OMR, subject_id)
    #         result = cursor.fetchone()
    #         cursor.close()
    #         connection.close()
    #         return result
    #     except Exception as e:
    #         print("Error fetching most recent BMI: ", e)
    #         return None'

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

    # def get_password(self, subject_id):  # low priority10002495
    #     try:
    #         connection = pyodbc.connect(self.connection_string)
    #         cursor = connection.cursor()
    #         cursor.execute(
    #             "select password from ? where subject_id = ?", LOGIN_DATA, subject_id
    #         )
    #         password = cursor.fetchone()[0]
    #         cursor.close()
    #         connection.close()
    #         return password
    #     except Exception as e:
    #         print("Error: ", e)

    # def login(self, subject_id, password):
    #     try:
    #         connection = pyodbc.connect(self.connection_string)
    #         cursor = connection.cursor()
    #         cursor.execute(
    #             "select firstname, surname from ? where subject_id = ? and password = ?",
    #             LOGIN_DATA,
    #             subject_id,
    #             password,
    #         )
    #         result = cursor.fetchone()
    #         cursor.close()
    #         connection.close()
    #         if result:
    #             print(f"Welcome {result[0]} {result[1]}")
    #         else:
    #             return "Invalid subject_id or password"

    #     except Exception as db_error:
    #         return f"Database error: {db_error}"
    #     except Exception as e:
    #         return f"An unexpected error occurred: {e}"

    # usage example


if __name__ == "__main__":
    user_service = User_service()
    print("Welcome to the hospital database.\n")
    print("Please choose an action: ")
    print()
    print(config.subject_id_logged)
    action = input(
        "Press '1'to a doctor profile by name , Press '2' to view your profile , Press '3' to create a diagnosis:, Press '4' to view procedures record of a patient "
    )
    print("Okay you chose: ", action)

    if action == "1":
        name = input("Give the name: ")
        The_role_id = user_service.get_doctor_by_name(name)
        print(The_role_id)

    elif action == "2":
        your_profile = user_service.get_your_profile(config.subject_id_logged)
        if your_profile:
            print("Your profile", your_profile)
        else:
            print("No patient information found or an error occurred.")
    elif action == "3":
        subject_id = int(input("Enter subject ID: "))
        icd_code = input("Enter ICD code: ")
        icd_version = input("Enter ICD version: ")
        user_service.create_diagnosis(subject_id, icd_code, icd_version)

        sub_action = input("Do you want to view the diagnosis? (yes/no): ")
        if sub_action == "yes":
            diagnosis = user_service.get_diagnosis(subject_id)
            print("Diagnosis:", diagnosis)
        else:
            print("Okay")

    elif action == "4":
        subject_id = int(input("Enter subject ID: "))
        procedures = user_service.get_procedures_by_subject_id(
            subject_id, config.subject_id_logged
        )
        if procedures:
            print(f"Procedures record of patient {subject_id} :", procedures)
        else:
            print("No procedures found or an error occurred.")

    # elif action == '2':
    #     subject_id = input("Enter subject ID: ")
    #     patient_info = user_service.get_patient_information(subject_id)
    #     if patient_info:
    #         print("Patient information:", patient_info)
    #     else:
    #         print("No patient information found or an error occurred.")
    # elif action == '3':
    #     subject_id = input("Enter subject ID: ")
    #     weight_record = user_service.get_most_recent_weight(subject_id)
    #     if weight_record:
    #         print("Most recent weight record:", weight_record)
    #     else:
    #         print("No weight record found or an error occurred.")

    # elif action == '4':
    #     subject_id= input("Enter subject Id: ")
    #     heith_record= user_service.get_most_recent_height(subject_id)
    #     if heith_record:
    #         print("Most recent height record:", heith_record)
    #     else:
    #         print("No height record found or an error occurred.")

    ##def get_user_by_id(self, id):
    # try:
    # if self.get_role_by_id(self.get_id() != 'admin') or self.get_role_by_id(self.get_id() != 'doctor'):
    # raise Exception("Only admins and doctors can view  patient data")
