import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import Service_Database as db
import os
from pathlib import Path
import sqlalchemy as sa
from db_access import connection_string


class Analyse:
    """This class is used to analyse the data in the database."""

    def __init__(self):
        """This method is used to initialize the connection_url and the User_service object."""
        self.connection_url = sa.URL.create(
            "mssql+pyodbc", query={"odbc_connect": connection_string}
        )
        self.us = db.User_service()

    def connect_to_db(self):
        """This method is used to connect to the database using the connection string.

        Returns:
            object: The connection to the database.
        """
        self.connection_string = connection_string
        self.connection_url = sa.URL.create(
            "mssql+pyodbc", query={"odbc_connect": connection_string}
        )
        return sa.create_engine(self.connection_url)

    def read_omr(self, id):
        """This method is used to read the omr table and plot the height, weight, BMI, and blood pressure of the patient,
        return it as string and save the data as a text file.

        Args:
            id (int): The subject_id of the patient.

        Returns:
            str: The data of the patient with the entered subject_id.
        """
        # Read the data from the omr table
        engine = self.connect_to_db()
        query = f"""select d.chartdate, d.result_name, d.result_value from omr as d 
                    where subject_id = {id} order by d.chartdate"""

        with engine.begin() as conn:
            df = pd.read_sql_query(
                sa.text(query),
                conn,
            )

        # Initialize the variables from the omr table
        x1 = x2 = x3 = x4 = None

        x1 = df[df["result_name"] == "Height (Inches)"]
        x2 = df[df["result_name"] == "Weight (Lbs)"]
        x3 = df[df["result_name"] == "BMI (kg/m2)"]
        x4 = df[df["result_name"] == "Blood Pressure"]

        # Plot the data as subplots
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 6))

        axes[0, 0].plot(x1["chartdate"], pd.to_numeric(x1["result_value"]))
        axes[0, 0].set_title("Height (Inches)")
        axes[0, 0].tick_params(axis="x", rotation=30)

        axes[0, 1].plot(x2["chartdate"], pd.to_numeric(x2["result_value"]))
        axes[0, 1].set_title("Weight (Lbs)")
        axes[0, 1].tick_params(axis="x", rotation=30)

        axes[1, 0].plot(x3["chartdate"], pd.to_numeric(x3["result_value"]))
        axes[1, 0].set_title("BMI (kg/m2)")
        axes[1, 0].tick_params(axis="x", rotation=30)

        axes[1, 1].plot(x4["chartdate"], x4["result_value"].sort_values())
        axes[1, 1].set_title("Blood Pressure")
        axes[1, 1].tick_params(axis="x", rotation=30)

        plt.tight_layout()
        plt.show()

        # Save the data of the patient as a text file and return it as a string for better visualization
        downloads_path = str(Path.home() / "Downloads")
        file_path = os.path.join(downloads_path, f"omr_{id}.txt")
        with open(file_path, "w") as file:
            file.write(df.to_string(index=False))
            print(f"\nYour Online Medical Record (OMR) is saved under {file_path}!")

        return df.to_string(index=False)

    def read_admissions(self, id):
        """This method is used to read the admissions table and plot the duration of stay in the hospital of all patients by gender,
        save the data of patient with entered subject_id as a text file and return it as a string.

        Args:
            id (int): The subject_id of the patient.

        Returns:
            str: The data of the patient with the entered subject_id.
        """
        # Read the data from the admissions table and gender of the patient from the patients table
        engine = self.connect_to_db()
        query = """select a.subject_id, a.hadm_id, a.admission_type , a.admittime, a.dischtime, a.deathtime, a.insurance, a.edregtime, a.edouttime, p.genders, a.hospital_expire_flag from admissions as a
                inner join patients as p ON a.subject_id = p.subject_id order by d.hadm_id"""

        with engine.begin() as conn:
            df = pd.read_sql_query(
                sa.text(query),
                conn,
            )

        # Read the data from the admissions table and calculate the duration of stay in the hospital
        adtime = df["admittime"]
        ditime = df["dischtime"]
        gender = df["gender"]
        time = pd.to_datetime(ditime) - pd.to_datetime(adtime)
        days = time.dt.days

        # Initialize the gender for the boxplot
        data_1 = days[gender == "M"]
        data_2 = days[gender == "F"]
        data = [data_1, data_2]

        # Plot the data of all patients as boxplot
        plt.boxplot(
            data,
            patch_artist=True,
            meanline=True,
            showmeans=True,
            labels=["Male", "Female"],
        )
        plt.title("Duration of Stay (Days) in Hospital")
        plt.ylabel("Days")
        plt.yticks(np.arange(0, max(days) + 1, 2))
        plt.grid(True, linestyle="--", linewidth=1.5, alpha=0.7)
        plt.show()

        # Save the data of the patient as a text file and return it as a string for better visualization
        patient = df[df["subject_id"] == id][
            "hadm_id, admission_type, admittime, dischtime, deathtime, insurance, edregtime, edouttime, hospital_expire_flag"
        ]
        downloads_path = str(Path.home() / "Downloads")
        file_path = os.path.join(downloads_path, f"admission_{id}.txt")
        with open(file_path, "w") as file:
            file.write(patient.to_string(index=False))
            print(f"\nYour admission is saved under {file_path}!")

        return patient.to_string(index=False)

    def read_diagnoses_icd(self, id):
        """This method is used to read the diagnoses_icd table, save the diagnoses of patient with entered subject_id as a text file and return it as a string.

        Args:
            id (int): The subject_id of the patient.

        Returns:
            str: The diagnoses of the patient with the entered subject_id.
        """
        # Read the data from the diagnoses_icd table and save the data as a text file
        engine = self.connect_to_db()
        query = f"""select d.hadm_id, d.seq_num, d.icd_code, id.long_title, d.icd_version from diagnoses_icd as d 
                    inner join d_icd_diagnoses as id ON d.icd_code = id.icd_code 
                    where subject_id = {id} order by d.hadm_id, seq_num"""
        with engine.begin() as conn:
            df = pd.read_sql_query(
                sa.text(query),
                conn,
            )

        downloads_path = str(Path.home() / "Downloads")
        file_path = os.path.join(downloads_path, f"diagnoses_{id}.txt")
        with open(file_path, "w") as file:
            file.write(df.to_string(index=False))
            print(f"\nYour diagnoses are saved under {file_path}!")

        # Return the diagnoses of the patient as a string for better visualization
        return df.to_string(index=False)

    def read_drgcodes(self, id):
        """This method is used to read the drgcodes table and return the drg codes of the patient, save the data as a text file and return it as a string.

        Args:
            id (int): The subject_id of the patient.

        Returns:
            str: The drg codes of the patient with the entered subject_id.
        """
        # Read the data from the drgcodes table
        engine = self.connect_to_db()
        query = f"""select d.hadm_id, d.drg_code, d.description, d.drg_severity, d.drg_mortality from drgcodes as d 
                    where subject_id = {id} order by d.hadm_id"""

        with engine.begin() as conn:
            df = pd.read_sql_query(
                sa.text(query),
                conn,
            )

        # Save the data of the patient as a text file and return it as a string for better visualization
        downloads_path = str(Path.home() / "Downloads")
        file_path = os.path.join(downloads_path, f"drg_codes_{id}.txt")
        with open(file_path, "w") as file:
            file.write(df.to_string(index=False))
            print(
                f"\nYour diagnosis related group (DRG) codes for hospitalizations are saved under {file_path}!"
            )

        return df.to_string(index=False)

    def read_emar(self, id):
        """This method is used to read the emar table and return the medication of the patient, save the data as a text file and return it as a string.

        Args:
            id (int): The subject_id of the patient.

        Returns:
            str: The medication of the patient with the entered subject_id.
        """
        # Read the data from the emar table
        engine = self.connect_to_db()
        query = f"""select e.hadm_id, e.pharmacy_id, e.medication, e.charttime, e.scheduletime, e.event_txt from emar as e 
                    where subject_id = {id} order by d.hadm_id"""

        with engine.begin() as conn:
            df = pd.read_sql_query(
                sa.text(query),
                conn,
            )

        # Save the data of the patient as a text file and return it as a string for better visualization
        downloads_path = str(Path.home() / "Downloads")
        file_path = os.path.join(downloads_path, f"emar_{id}.txt")
        with open(file_path, "w") as file:
            file.write(df.to_string(index=False))
            print(
                f"\nYour Electronic Medicine Administration Record (eMAR) is saved under {file_path}!"
            )

        return df.to_string(index=False)

    def read_patients(self, id):
        """This method is used to read the patients table and plot the distribution of patients by age
        and return the data of the patient with the entered subject_id.

        Args:
            id (int): The subject_id of the patient.

        Returns:
            str: The data of the patient with the entered subject_id.
        """
        # Read the data from the patients table
        engine = self.connect_to_db()
        query = """select p.subject_id, p.gender, p.anchor_age, p.dod from patients as p order by anchor_age"""

        with engine.begin() as conn:
            df = pd.read_sql_query(
                sa.text(query),
                conn,
            )

        # Initialize the variables for the plot
        age = df["anchor_age"]
        gender = df["gender"]
        b_width = 5  # set the width of bin

        # Plot the distribution of patients by age
        fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure and axis
        ax.hist(
            age[gender == "M"],
            bins=np.arange(min(age) - 1, max(age) + 1, b_width),
            alpha=0.5,
            label="Male",
            color="b",
        )
        ax.hist(
            age[gender == "F"],
            bins=np.arange(min(age) - 1, max(age) + 1, b_width),
            alpha=0.5,
            label="Female",
            color="r",
        )

        ax.set_title("Distribution of Patient Ages by Gender")
        ax.set_xlabel("Age")
        ax.set_ylabel("Number of Patients")
        ax.legend(loc="upper right")

        plt.show()

        # Return the data of the patient as a string for better visualization
        patient = df[df["subject_id"] == id][["gender", "anchor_age", "dod"]]
        return patient.to_string(index=False)

    def read_pharmacy(self, id):
        """This method is used to read the pharmacy table, return the pharmacy data of the patient with the entered subject_id
        and save the data as a text file.

        Args:
            id (int): The subject_id of the patient.

        Returns:
            str: The pharmacy data of the patient with the entered subject_id.
        """
        # Read the data from the pharmacy table
        engine = self.connect_to_db()
        query = f"""select p.hadm_id, p.pharmacy_id, p.medication, p.proc_type, p.frequency, p.starttime, p.stoptime from pharmacy as p 
                    where subject_id = {id} order by d.hadm_id"""

        with engine.begin() as conn:
            df = pd.read_sql_query(
                sa.text(query),
                conn,
            )

        # Save the data of the patient as a text file and return it as a string for better visualization
        downloads_path = str(Path.home() / "Downloads")
        file_path = os.path.join(downloads_path, f"pharmacy_{id}.txt")
        with open(file_path, "w") as file:
            file.write(df.to_string(index=False))
            print(f"\nYour pharmacy is saved under {file_path}!")

        return df.to_string(index=False)

    def read_procedures_icd(self, id):
        """This method is used to read the procedures_icd table, save the procedures of patient with entered subject_id as a text file and return it as a string.

        Args:
            id (int): The subject_id of the patient.

        Returns:
            str: The procedures of the patient with the entered subject_id.
        """
        # Read the data from the procedures_icd table and save the data as a text file
        engine = self.connect_to_db()
        query = f"""select d.hadm_id, d.chartdate, d.seq_num, d.icd_code, id.long_title, d.icd_version from procedures_icd as d 
                    inner join d_icd_procedures as id ON d.icd_code = id.icd_code 
                    where subject_id = {id} order by d.hadm_id, d.chartdate, d.seq_num"""
        with engine.begin() as conn:
            df = pd.read_sql_query(
                sa.text(query),
                conn,
            )

        downloads_path = str(Path.home() / "Downloads")
        file_path = os.path.join(downloads_path, f"procedures_{id}.txt")
        with open(file_path, "w") as file:
            file.write(df.to_string(index=False))
            print(f"\nYour procedures are saved under {file_path}!")

        # Return the diagnoses of the patient as a string for better visualization
        return df.to_string(index=False)

    def read_d_icd_diagnoses(self):
        """This method is used to read the d_icd_diagnoses table and return the data of the icd code entered by the user.

        Returns:
            str: The data of the icd code entered by the user.
        """
        df = self.us.read_table_sa("d_icd_diagnoses")
        try:
            icd = input("Enter icd code: ")
            # Get the data of the icd code
            icd_code = df[df["icd_code"].astype(str) == icd][
                ["icd_code", "icd_version", "long_title"]
            ]
            return icd_code.to_string(index=False)
        except Exception as e:
            print("Invalid icd code.", e)
            Analyse.read_d_icd_diagnoses()  # Call the method again if the icd code is invalid

    def read_d_icd_procedures(self):
        """This method is used to read the d_icd_procedures table and return the long title of the icd code entered by the user.

        Returns:
            str: The long title of the icd code entered by the user.
        """
        df = self.us.read_table_sa("d_icd_procedures")
        icd = input("Enter icd code: ")
        # Get the long title of the icd code
        icd_code = df[df["icd_code"].astype(str) == icd]["long_title"]
        return icd_code
