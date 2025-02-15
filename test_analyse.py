import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import Service_Database as db
import sqlalchemy as sa
from db_access import connection_string


class Analyse:
    def __init__(self):
        self.connection_url = sa.URL.create(
            "mssql+pyodbc", query={"odbc_connect": connection_string}
        )
        self.us = db.User_service()

    def read_omr(self):
        df = self.us.read_table_sa("omr")

        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = df[
            df["subject_id"] == id
        ]  # Get the patient with the entered subject_id
        patient = patient.sort_values(by="chartdate")

        x1 = x2 = x3 = x4 = None

        x1 = patient[patient["result_name"] == "Height (Inches)"]
        x2 = patient[patient["result_name"] == "Weight (Lbs)"]
        x3 = patient[patient["result_name"] == "BMI (kg/m2)"]
        x4 = patient[patient["result_name"] == "Blood Pressure"]

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
        patient_value = df[df["subject_id"] == id][
            ["chartdate", "result_name", "result_value"]
        ]
        return patient_value.to_string(index=False)

    def read_admissions(self):
        engine = sa.create_engine(self.connection_url)

        with engine.begin() as conn:
            df = pd.read_sql_query(
                sa.text(
                    "select a.*, p.gender from admissions as a inner join patients as p ON p.subject_id = a.subject_id"
                ),
                conn,
            )

        adtime = df["admittime"]
        ditime = df["dischtime"]
        gender = df["gender"]
        time = pd.to_datetime(ditime) - pd.to_datetime(adtime)
        days = time.dt.days

        data_1 = days[gender == "M"]
        data_2 = days[gender == "F"]
        data = [data_1, data_2]

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
        plt.show()  # Display the plot

        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
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
        df = self.us.read_table_sa("diagnoses_icd")
        df1 = self.us.read_table_sa("d_icd_diagnoses")
        merged_df = pd.merge(
            df, df1[["icd_code", "long_title"]], on="icd_code", how="left"
        )
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = merged_df[merged_df["subject_id"] == id][
            ["seq_num", "icd_code", "icd_version", "long_title"]
        ]
        return patient.to_string(index=False)

    def read_drgcodes(self):
        df = self.us.read_table_sa("drgcodes")
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = df[df["subject_id"] == id][
            ["drg_code", "description", "drg_severity", "drg_mortality"]
        ]
        return patient.to_string(index=False)

    def read_emar(self):
        df = self.us.read_table_sa("emar")
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = df[df["subject_id"] == id][
            ["pharmacy_id", "medication", "charttime", "scheduletime", "event_txt"]
        ]
        return patient.to_string(index=False)

    def read_patients(self):
        df = self.us.read_table_sa("patients")
        age = df["anchor_age"]
        gender = df["gender"]
        b_width = 5  # set the width of bin

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

        plt.show()  # Display the plot
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = df[df["subject_id"] == id][["gender", "anchor_age", "dod"]]
        return patient.to_string(index=False)

    def read_pharmacy(self):
        df = self.us.read_table_sa("pharmacy")
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
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
        df = self.us.read_table_sa("procedures_icd")
        df1 = self.us.read_table_sa("d_icd_procedures")
        merged_df = pd.merge(
            df, df1[["icd_code", "long_title"]], on="icd_code", how="left"
        )
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = merged_df[merged_df["subject_id"] == id][
            ["chartdate", "seq_num", "icd_code", "long_title", "icd_version"]
        ]
        return patient.to_string(index=False)

    def read_d_icd_diagnoses(self):
        df = self.us.read_table_sa("d_icd_diagnoses")
        icd = input("Enter icd code: ")  # Ask the user to enter the icd code
        icd_code = df[df["icd_code"].astype(str) == icd]["long_title"].values[
            0
        ]  # Get the long title of the icd code
        return icd_code

    def read_d_icd_procedures(self):
        df = self.us.read_table_sa("d_icd_procedures")
        icd = input("Enter icd code: ")  # Ask the user to enter the icd code
        icd_code = df[df["icd_code"].astype(str) == icd]["long_title"].values[
            0
        ]  # Get the long title of the icd code
        return icd_code
