import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
# import pyodbc
# from warnings import filterwarnings


class Analyse:
    def __init__(self):
        self.current_dir = "/mnt/c/Users/Konst/Desktop/Uni/Python/Kurs Projekt/Lank/Datenbank/mimic/mimic-demo/hosp"
        self.omr_csv_path = os.path.join(self.current_dir, "omr.csv.gz")
        self.admissions_csv_path = os.path.join(self.current_dir, "admissions.csv.gz")
        self.diagnoses_icd_csv_path = os.path.join(
            self.current_dir, "diagnoses_icd.csv.gz"
        )
        self.drgcodes_csv_path = os.path.join(self.current_dir, "drgcodes.csv.gz")
        self.emar_csv_path = os.path.join(self.current_dir, "emar.csv.gz")
        self.patients_csv_path = os.path.join(self.current_dir, "patients.csv.gz")
        self.pharmacy_csv_path = os.path.join(self.current_dir, "pharmacy.csv.gz")
        self.procedures_icd_csv_path = os.path.join(
            self.current_dir, "procedures_icd.csv.gz"
        )
        self.d_icd_diagnoses_csv_path = os.path.join(
            self.current_dir, "d_icd_diagnoses.csv.gz"
        )
        self.d_icd_procedures_csv_path = os.path.join(
            self.current_dir, "d_icd_procedures.csv.gz"
        )

    def read_omr(self):
        df = pd.read_csv(self.omr_csv_path)
        print(df.head())
        id = input("Enter subject_id: ")
        patient = df[df["subject_id"].astype(str) == id]

        return patient

    def read_admissions(self):
        df = pd.read_csv(self.admissions_csv_path)
        print(df.head())
        id = input("Enter subject_id: ")
        patient = df[df["subject_id"].astype(str) == id]
        return patient

    def read_diagnoses_icd(self):
        df = pd.read_csv(self.diagnoses_icd_csv_path)
        print(df.head())
        id = input("Enter subject_id: ")
        patient = df[df["subject_id"].astype(str) == id]
        return patient

    def read_drgcodes(self):
        df = pd.read_csv(self.drgcodes_csv_path)
        print(df.head())
        id = input("Enter subject_id: ")
        patient = df[df["subject_id"].astype(str) == id]
        return patient

    def read_emar(self):
        df = pd.read_csv(self.emar_csv_path)
        print(df.head())
        id = input("Enter subject_id: ")
        patient = df[df["subject_id"].astype(str) == id]
        return patient

    def read_patients(self):
        df = pd.read_csv(self.patients_csv_path)
        print(df.head())
        print(df.shape)
        b_width = 5  # set the width of bin
        df["anchor_age"].plot(
            kind="hist",
            bins=np.arange(
                min(df["anchor_age"]) - 1, max(df["anchor_age"]) + b_width, b_width
            ),
        )  # we are setting the bins values in a list by incrementing them with bin width = 5
        plt.xlabel("Age")  # Label of x-axis
        plt.ylabel("Patients")  # Label of y-axis
        plt.title("Age distribution of patients")  # Title of the plot
        plt.xticks(
            np.arange(min(df["anchor_age"]), max(df["anchor_age"]) + 10, 5)
        )  # We set the values in the x-axis
        plt.yticks(np.arange(0, 25, 2))  # Setting the values in y-axis
        df.plot(kind="scatter", x="anchor_age", y="gender")  # Scatter plot
        plt.show()  # Display the plot
        id = input("Enter subject_id: ")  # Ask the user to enter the subject_id
        patient = df[
            df["subject_id"].astype(str) == id
        ]  # Get the patient with the entered subject_id
        return patient

    def read_pharmacy(self):
        df = pd.read_csv(self.pharmacy_csv_path)
        print(df.head())
        id = input("Enter subject_id: ")
        patient = df[df["subject_id"].astype(str) == id]
        return patient

    def read_procedures_icd(self):
        df = pd.read_csv(self.procedures_icd_csv_path)
        print(df.head())
        id = input("Enter subject_id: ")
        patient = df[df["subject_id"].astype(str) == id]
        return patient

    def read_d_icd_diagnoses(self):
        df = pd.read_csv(self.d_icd_diagnoses_csv_path)
        print(df.head())
        id = input("Enter subject_id: ")
        patient = df[df["subject_id"].astype(str) == id]
        return patient

    def read_d_icd_procedures(self):
        df = pd.read_csv(self.d_icd_procedures_csv_path)
        print(df.head())
        id = input("Enter subject_id: ")
        patient = df[df["subject_id"].astype(str) == id]
        return patient


# filterwarnings("ignore", category=UserWarning, message='.*pandas only supports SQLAlchemy connectable.*')
# conn_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=LAPTOP-CC0D63;DATABASE=LANK;UID=LANK_USER;PWD=Lank1.;TrustServerCertificate=YES'
# conn = pyodbc.connect(conn_string)
# sql = "SELECT * FROM omr"
# pd.read_sql(sql, conn)
