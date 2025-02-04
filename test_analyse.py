import pandas as pd
import os

class Analyse:
    def __init__(self):
        self.current_dir = '/mnt/c/Users/Konst/Desktop/Uni/Python/Kurs Projekt/Lank'
        self.omr_csv_path = os.path.join(self.current_dir, "Datenbank", "mimic", "mimic-demo", "hosp", "omr.csv.gz")
        self.admissions_csv_path = os.path.join(self.current_dir, "Datenbank", "mimic", "mimic-demo", "hosp", "admissions.csv.gz")
        self.diagnoses_icd_csv_path = os.path.join(self.current_dir, "Datenbank", "mimic", "mimic-demo", "hosp", "diagnoses_icd.csv.gz")
        self.drgcodes_csv_path = os.path.join(self.current_dir, "Datenbank", "mimic", "mimic-demo", "hosp", "drgcodes.csv.gz")
        self.emar_csv_path = os.path.join(self.current_dir, "Datenbank", "mimic", "mimic-demo", "hosp", "emar.csv.gz")
        self.patients_csv_path = os.path.join(self.current_dir, "Datenbank", "mimic", "mimic-demo", "hosp", "patients.csv.gz")
        self.pharmacy_csv_path = os.path.join(self.current_dir, "Datenbank", "mimic", "mimic-demo", "hosp", "pharmacy.csv.gz")
        self.procedures_icd_csv_path = os.path.join(self.current_dir, "Datenbank", "mimic", "mimic-demo", "hosp", "procedures_icd.csv.gz")
        self.d_icd_diagnoses_csv_path = os.path.join(self.current_dir, "Datenbank", "mimic", "mimic-demo", "hosp", "d_icd_diagnoses.csv.gz")
        self.d_icd_procedures_csv_path = os.path.join(self.current_dir, "Datenbank", "mimic", "mimic-demo", "hosp", "d_icd_procedures.csv.gz")
    
    #def read_csv(self, csv_path):
        
        