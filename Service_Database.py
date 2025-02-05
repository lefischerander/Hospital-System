import pyodbc


connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-CC0D63;DATABASE=LANK;UID=LANK_USER;PWD=Lank1.;TrustServerCertificate=YES'


class User_service:
    
    def delete_user(self, user):
        
        try:
            if self.get_role_by_id(self.get_id()) != 'admin':
                raise Exception("Only admins can delete users")
            
            connection= pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute("delete from New_login_data where New_login_data.subject_id = ?", user.get_id())
            
            connection.commit()
            
            cursor.close()
            connection.close()
        except Exception as e:
            print("Error:" , e)
    
    def get_role_by_id(self, id):
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute("select role from New_login_data where subject_id = ?", id)
            role = cursor.fetchone()[0]
            cursor.close()
            connection.close()
            return role
        except Exception as e:
            print("Error: ", e)
    
    def get_id(self):
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute("select subject_id from New_login_data where surname = ?", self.surname)
            id = cursor.fetchone()[0]
            cursor.close()
            connection.close()
            return id
        except Exception as e:
            print("Error: ", e)

    def get_doctor_by_name(self, surname ):
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute("select firstname, lastname, department_name, age from doctors where surname = ?", surname)
            doctor = cursor.fetchone()
            cursor.close()
            connection.close()
            return doctor
        except Exception as e:
            print("Error: ", e)
    
    def create_user(self, username, password, role): ##low priority
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute("insert into New_login_data (username, password, role) values (?, ?, ?)", username, password, role)
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            print("Error creating user: ", e)

    def change_password(self, username, password):   ##low priority
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute("update New_login_data set password = ? where username = ?", password, username)
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            print("Error changing password: ", e)

    def create_diagnosis(self, patient_id, hadm_id ):
        try:
            if self.get_role_by_id(self.get_id()) != 'doctor':
                raise Exception("Only doctors can add diagnoses")
            
            connection= pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute("insert into diagnosis (subject_id, hadm_id) values (?, ?)", patient_id, hadm_id)
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as e:
            print("Error: ", e)
    
    def get_patient_information(self, subject_id):
        try:
            connection = pyodbc.connect(connection_string)
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
            print(f"All information about the patient {result[3]} {result[4]: }") 
            return result 
        except Exception as e:
            print("Error fetching patient information: ", e)
            return None
    
    def get_diagnosis(self, patient_id):
        try:
            connection= pyodbc.connect(connection_string)
            cursor= connection.cursor()
            cursor.execute("select d.subject_id, d.hadm_id from diagnosis AS d where d.subject_id = ?", patient_id)
            diagnosis = cursor.fetchone()
            cursor.close()
            connection.close()
            return diagnosis
        except Exception as e:
            print("Error: ", e)
    
    def get_procedures_by_subject_id(self, subject_id):
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            query = """
                SELECT p.subject_id, p.hadm_id, p.seq_num, p.chartdate, p.icd_code, p.icd_version, dp.long_title 
                FROM procedures_icd AS p
                INNER JOIN d_icd_procedures AS dp ON p.icd_code = dp.icd_code
                WHERE p.subject_id = ?
                ORDER BY p.seq_num
            """
            cursor.execute(query, subject_id)
            results = cursor.fetchall()
            cursor.close()
            connection.close()
            return results
        except Exception as e:
            print("Error fetching procedures: ", e)
            return None
    
    def get_most_recent_weight(self, subject_id):
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            query = """
                SELECT TOP 1 * 
                FROM omr
                WHERE subject_id = ? AND result_name LIKE 'Weight%'
                ORDER BY chartdate DESC
            """
            cursor.execute(query, subject_id)
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            print("Error fetching most recent weight: ", e)
            return None
        
    def get_most_recent_height(self, subject_id):
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            query = """
                SELECT TOP 1 * 
                FROM omr
                WHERE subject_id = ? AND result_name LIKE 'Height%'
                ORDER BY chartdate DESC
            """
            cursor.execute(query, subject_id)
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            print("Error fetching most recent height: ", e)
            return None
    
    def get_most_recent_bmi(self, subject_id):
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            query = """
                SELECT TOP 1 * 
                FROM omr
                WHERE subject_id = ? AND result_name LIKE 'BMI%'
                ORDER BY chartdate DESC
            """
            cursor.execute(query, subject_id)
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            print("Error fetching most recent BMI: ", e)
            return None
    def view_all_users(self):
        connection= pyodbc.connect(connection_string)
        cursor= connection.cursor()
        cursor.execute("select subject_id, firstname, surname, role from New_login_data")
        users= cursor.fetchall()
        cursor.close()
        connection.close()
        return users

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def login(self, subject_id, password):
        try:
            connection = pyodbc.connect(connection_string)
            cursor = connection.cursor()
            cursor.execute("select firstname, surname from  New_login_data where subject_id = ? and password = ?", subject_id, password)
            result = cursor.fetchone()
            cursor.close()
            connection.close()
            if result:
                print(f"Welcome {result[0]} {result[1]}")
            else:
                return "Invalid subject_id or password"
        
        except Exception as db_error:
           return f"Database error: {db_error}"
        except Exception as e:
           return f"An unexpected error occurred: {e}"
        
    


    #usage example

# if __name__ == "__main__":
#     user_service = User_service()
#     print("Welcome to the hospital database.")
#     print("Please choose an action:")
#     print()
#     print("\n"'1.Login ,2. View patient information, "\n",3. View most recent weight record,"\n"4.View most recent height record')
    
#     action = input("Choose an action: ")
#     if action == '1':
#         try:
#             subject_id= input("Subject ID: ")
#             password= input("Password: ")
#             login= user_service.login(subject_id, password)
#             if not login:

            

        
    
    
    
    
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
        #try:
            #if self.get_role_by_id(self.get_id() != 'admin') or self.get_role_by_id(self.get_id() != 'doctor'):
                #raise Exception("Only admins and doctors can view  patient data")
            
        
            
            

    