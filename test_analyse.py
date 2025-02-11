import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
#import seaborn as sns
#import pyodbc

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
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = df[df["subject_id"] == id]  # Get the patient with the entered subject_id
        patient = patient.sort_values(by='chartdate')
        
        x1 = x2 = x3 = x4 = None

        x1 = patient[patient['result_name'] == "Height (Inches)"]
        x2 = patient[patient['result_name'] == "Weight (Lbs)"]
        x3 = patient[patient['result_name'] == "BMI (kg/m2)"]
        x4 = patient[patient['result_name'] == "Blood Pressure"]

        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 6))

        axes[0, 0].plot(x1['chartdate'], pd.to_numeric(x1['result_value']))
        axes[0, 0].set_title('Height (Inches)')
        axes[0, 0].tick_params(axis='x', rotation=30)

        axes[0, 1].plot(x2['chartdate'], pd.to_numeric(x2['result_value']))
        axes[0, 1].set_title('Weight (Lbs)')
        axes[0, 1].tick_params(axis='x', rotation=30)

        axes[1, 0].plot(x3['chartdate'], pd.to_numeric(x3['result_value']))
        axes[1, 0].set_title('BMI (kg/m2)')
        axes[1, 0].tick_params(axis='x', rotation=30)

        axes[1, 1].plot(x4['chartdate'], x4['result_value'].sort_values())
        axes[1, 1].set_title('Blood Pressure')
        axes[1, 1].tick_params(axis='x', rotation=30)

        plt.tight_layout()      
        plt.show()      
        return patient


    def read_admissions(self):
        df = pd.read_csv(self.admissions_csv_path)
        print(df.head())
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = df[df["subject_id"] == id]  # Get the patient with the entered subject_id
        return patient

    def read_diagnoses_icd(self):
        df = pd.read_csv(self.diagnoses_icd_csv_path)
        print(df.head())
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = df[df["subject_id"] == id]  # Get the patient with the entered subject_id
        return patient

    def read_drgcodes(self):
        df = pd.read_csv(self.drgcodes_csv_path)
        print(df.head())
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = df[df["subject_id"] == id]  # Get the patient with the entered subject_id
        return patient

    def read_emar(self):
        df = pd.read_csv(self.emar_csv_path)
        print(df.head())
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = df[df["subject_id"] == id]  # Get the patient with the entered subject_id
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
        #sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
        plt.show()  # Display the plot
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = df[df["subject_id"] == id]  # Get the patient with the entered subject_id
        return patient

    def read_pharmacy(self):
        df = pd.read_csv(self.pharmacy_csv_path)
        print(df.head())
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = df[df["subject_id"] == id]  # Get the patient with the entered subject_id
        return patient

    def read_procedures_icd(self):
        df = pd.read_csv(self.procedures_icd_csv_path)
        print(df.head())
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = df[df["subject_id"] == id]  # Get the patient with the entered subject_id
        return patient

    def read_d_icd_diagnoses(self):
        df = pd.read_csv(self.d_icd_diagnoses_csv_path)
        print(df.head())
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = df[df["subject_id"] == id]  # Get the patient with the entered subject_id
        return patient

    def read_d_icd_procedures(self):
        df = pd.read_csv(self.d_icd_procedures_csv_path)
        print(df.head())
        id = int(input("Enter subject_id: "))  # Ask the user to enter the subject_id
        patient = df[df["subject_id"] == id]  # Get the patient with the entered subject_id
        return patient
