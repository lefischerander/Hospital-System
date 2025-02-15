import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import Service_Database as db
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

    def read_omr(self):
        """This method is used to read the omr table and plot the data of the patient with the entered subject_id as line plot
        and return the data as a string.

        Returns:
            str: The data of the patient with the entered subject_id.
        """
        df = self.us.read_table_sa("omr")

        # Ask to enter the subject_id and sort the data by chartdate
        id = int(input("Enter subject_id: "))
        patient = df[df["subject_id"] == id]
        patient = patient.sort_values(by="chartdate")

        # Initialize the variables
        x1 = x2 = x3 = x4 = None

        x1 = patient[patient["result_name"] == "Height (Inches)"]
        x2 = patient[patient["result_name"] == "Weight (Lbs)"]
        x3 = patient[patient["result_name"] == "BMI (kg/m2)"]
        x4 = patient[patient["result_name"] == "Blood Pressure"]

        # Plot the data
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

        # Return the data of the patient as a string for better visualization
        patient_value = df[df["subject_id"] == id][
            ["chartdate", "result_name", "result_value"]
        ]
        return patient_value.to_string(index=False)

    def read_admissions(self):
        """This method is used to read the admissions table and plot the duration of stay of all patients in the hospital as boxplot.
        It also returns the data of the patient with the entered subject_id.

        Returns:
            str: The data of the patient with the entered subject_id.
        """
        engine = sa.create_engine(self.connection_url)

        with engine.begin() as conn:
            df = pd.read_sql_query(
                sa.text(
                    "select a.*, p.gender from admissions as a inner join patients as p ON p.subject_id = a.subject_id"
                ),
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

        # Return the data of the patient as a string for better visualization
        id = int(input("Enter subject_id: "))
        patient = df[df["subject_id"] == id][
            [
                "admittime",
                "dischtime",
                "deathtime",
                "admission_type",
                "insurance",
                "edregtime",
                "edouttime",
                "hospital_expire_flag",
            ]
        ]
        return patient.to_string(index=False)

    def read_diagnoses_icd(self):
        """This method is used to read the diagnoses_icd table and return diagnoses of the patient with the entered subject_id.

        Returns:
            str: The diagnoses of the patient with the entered subject_id.
        """
        df = self.us.read_table_sa("diagnoses_icd")
        df1 = self.us.read_table_sa("d_icd_diagnoses")
        merged_df = pd.merge(
            df, df1[["icd_code", "long_title"]], on="icd_code", how="left"
        )
        id = int(input("Enter subject_id: "))
        # Return the diagnoses of the patient as a string for better visualization
        patient = merged_df[merged_df["subject_id"] == id][
            ["seq_num", "icd_code", "icd_version", "long_title"]
        ]
        return patient.to_string(index=False)

    def read_drgcodes(self):
        """This method is used to read the drgcodes table and return the drg codes of the patient with the entered subject_id.

        Returns:
            str: The drg codes of the patient with the entered subject_id.
        """
        df = self.us.read_table_sa("drgcodes")
        id = int(input("Enter subject_id: "))
        # Return the drg codes of the patient as a string for better visualization
        patient = df[df["subject_id"] == id][
            ["drg_code", "description", "drg_severity", "drg_mortality"]
        ]
        return patient.to_string(index=False)

    def read_emar(self):
        """This method is used to read the emar table and return the medication of the patient with the entered subject_id.

        Returns:
            str: The medication of the patient with the entered subject_id.
        """
        df = self.us.read_table_sa("emar")
        id = int(input("Enter subject_id: "))
        # Return the medication of the patient as a string for better visualization
        patient = df[df["subject_id"] == id][
            ["pharmacy_id", "medication", "charttime", "scheduletime", "event_txt"]
        ]
        return patient.to_string(index=False)

    def read_patients(self):
        """This method is used to read the patients table and plot the distribution of patients by age
        and return the data of the patient with the entered subject_id.

        Returns:
            str: The data of the patient with the entered subject_id.
        """
        df = self.us.read_table_sa("patients")
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

        id = int(input("Enter subject_id: "))
        # Return the data of the patient as a string for better visualization
        patient = df[df["subject_id"] == id][["gender", "anchor_age", "dod"]]
        return patient.to_string(index=False)

    def read_pharmacy(self):
        """This method is used to read the pharmacy table and return the pharmacy data of the patient with the entered subject_id.

        Returns:
            str: The pharmacy data of the patient with the entered subject_id.
        """
        df = self.us.read_table_sa("pharmacy")
        id = int(input("Enter subject_id: "))
        # Return the pharmacy data of the patient as a string for better visualization
        patient = df[df["subject_id"] == id][
            [
                "pharmacy_id",
                "medication",
                "proc_type",
                "frequency",
                "starttime",
                "stoptime",
            ]
        ]
        return patient.to_string(index=False)

    def read_procedures_icd(self):
        """This method is used to read the procedures_icd table and return the procedures of the patient with the entered subject_id.

        Returns:
            str: The procedures of the patient with the entered subject_id.
        """
        df = self.us.read_table_sa("procedures_icd")
        df1 = self.us.read_table_sa("d_icd_procedures")
        # Merge the data of the procedures_icd and d_icd_procedures table
        merged_df = pd.merge(
            df, df1[["icd_code", "long_title"]], on="icd_code", how="left"
        )
        id = int(input("Enter subject_id: "))
        # Return the procedures of the patient as a string for better visualization
        patient = merged_df[merged_df["subject_id"] == id][
            ["chartdate", "seq_num", "icd_code", "long_title", "icd_version"]
        ]
        return patient.to_string(index=False)

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
