import pyodbc
from db_access import connection_string
import config
import sqlalchemy as sa
import pandas as pd


# database tables
LOGIN_DATA = "New_login_data"
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


class User_service:
    """
    This class is responsible for handling all database operations
    """

    def __init__(self):
        """
        Initializes the connection string to the database

        Parameters:
        connection_string: str
            The connection string to the database
        """
        self.connection_string = connection_string
        self.connection_url = sa.URL.create(
            "mssql+pyodbc", query={"odbc_connect": connection_string}
        )

    def read_table_sa(self, table_name):
        """
        Reads an entire table from the database with SQLAlchemy and fills a pandas DataFrame with the data

        Args:
            table_name (str): The name of the table to be read

        Returns:
            DataFrame: The table data in a pandas DataFrame
        """
        engine = sa.create_engine(self.connection_url)
        with engine.begin() as conn:
            df = pd.read_sql_query(sa.text(f"SELECT * FROM {table_name}"), conn)

        return df

    def delete_user(self, user):  ##low priority
        """Deletes a user from the database based on the user's subject ID

        Args:
            user (int): the to-be-deleted user's subject ID

        Raises:
            Exception: If the user is not an admin
            Exception: If the user is not found in the database or another error occurs
        """
        try:
            if self.get_role_by_id(self.get_id()) != "admin":
                raise Exception("Only admins can delete users")

            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute(
                "delete from ? where subject_id = ?",
                LOGIN_DATA,
                user.get_id(),
            )

            connection.commit()

            cursor.close()
            connection.close()
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

    def get_id(self, surname):
        """Gets a user's subject ID based on the user's surname

        Args:
            surname (str): The user's surname

        Returns:
            int: The user's subject ID

        Raises:
            Exception: If the user is not found in the database or another error occurs
        """
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute(
                f"select subject_id from {LOGIN_DATA} where surname = ?", surname
            )
            id = cursor.fetchone()[0]
            cursor.close()
            connection.close()
            return id
        except Exception as e:
            print("Error: user not found ", e)

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
                "select firstname, surname, department_name, age from ? where surname = ?",
                DOCTORS,
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
                SELECT subject_id, firstname, surname, department_name, age 
                FROM  {DOCTORS} 
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

    def create_user(self, username, password, role):  ##low priority
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute(
                "insert into ? (username, password, role) values (?, ?, ?)",
                LOGIN_DATA,
                username,
                password,
                role,
            )
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            print("Error creating user: ", e)

    def change_password(self, username, password):  ##low priority
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
    
    def check_id(self, subject_id):
        try:
            connection= pyodbc.connect(self.connection_string)
            cursor= connection.cursor()

            cursor.execute(
                f"select subject_id from {PATIENTS} where subject_id= ?", 
                subject_id,
            )

            if cursor.fetchone()[0] == 0:
                raise Exception(f" User: '{subject_id}' not found in the database")
            
            checked_id= cursor.fetchone()
            connection.commit()
            cursor.close()
            connection.close()

            return checked_id
        except Exception as e:
            print(f"Oups error: ", e)
            return None


            

            

    def create_diagnosis(self, patient_id, icd_code, icd_version):
        try:
            if self.get_role_by_id(config.Subject_id_logged) != "Doctor":
                raise Exception("Only doctors can add diagnoses")

            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
  
            check_id = self.check_id(patient_id)
            if check_id is None:
                raise Exception(f"Patient with subject ID {patient_id} not found")

            hadm_id = cursor.execute(
                "select subject_id, hadm_id from ? where subject_id = ? order by hadm_id desc",
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

            cursor.execute(
                "insert into diagnoses_icd (subject_id, hadm_id, seq_num, icd_code, icd_version) values (?, ?, ?, ?, ?)",
                patient_id,
                hadm_id,
                seq_num,
                icd_code,
                icd_version,
            )
            connection.commit()
            cursor.close()
            connection.close()
            print(f" Diagnosis added for patients with subject ID: {patient_id}")
        except Exception as e:
            print("Error:  ", e)
            return None

    def get_patient_profile(self, subject_id):  # dod time must be string
        try:
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

    def get_diagnosis(self, patient_id):
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute(
                "select d.subject_id, d.hadm_id, d.d_icd_diagnosis from diagnosis AS d where d.subject_id = ?",
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

    def get_most_recent_weight(self, subject_id):
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            query = """
                SELECT TOP 1 * 
                FROM ?
                WHERE subject_id = ? AND result_name LIKE 'Weight%'
                ORDER BY chartdate DESC
            """
            cursor.execute(query, OMR, subject_id)
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            print("Error fetching most recent weight: ", e)
            return None

    def get_most_recent_height(self, subject_id):
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            query = """
                SELECT TOP 1 * 
                FROM ?
                WHERE subject_id = ? AND result_name LIKE 'Height%'
                ORDER BY chartdate DESC
            """
            cursor.execute(query, OMR, subject_id)
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            print("Error fetching most recent height: ", e)
            return None

    def get_most_recent_bmi(self, subject_id):
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            query = """
                SELECT TOP 1 * 
                FROM ?
                WHERE subject_id = ? AND result_name LIKE 'BMI%'
                ORDER BY chartdate DESC
            """
            cursor.execute(query, OMR, subject_id)
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            print("Error fetching most recent BMI: ", e)
            return None

    def view_all_users(self):
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute(
                f"select subject_id, firstname, surname, role from {LOGIN_DATA}"
            )
            users = cursor.fetchall()
            cursor.close()
            connection.close()
            return users
        except pyodbc as database_error:
            print("Error fetching all users: ", database_error)
            return None

    def get_password(self, subject_id):  # low priority
        try:
            connection = pyodbc.connect(self.connection_string)
            cursor = connection.cursor()
            cursor.execute(
                "select password from ? where subject_id = ?", LOGIN_DATA, subject_id
            )
            password = cursor.fetchone()[0]
            cursor.close()
            connection.close()
            return password
        except Exception as e:
            print("Error: ", e)

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
    print("Welcome to the hospital database.")
    print("Please choose an action:")

    action = input(
        "Press '1'to get role by id, Press '2' to view a patient's profile, Press '3' to create a diagnosis:, Press '4' to view procedures record of a patient "
    )
    print("Okay you chose: ", action)
    if action == "1":
        role = input("Give the subject_id: ")
        The_role_id = user_service.get_role_by_id(role)
        print(The_role_id)

    elif action == "2":
        subject_id = int(input("Enter subject ID: "))
        your_profile = user_service.get_your_profile(subject_id)
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
            subject_id, config.Subject_id_logged
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
