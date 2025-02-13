import pandas as pd
from pathlib import Path
import os
import time

start_time = time.time()
pd.options.mode.chained_assignment = None

path = Path(__file__).parent / "Files/"

# Columns that are not allowed to have NaN/NULL values
nn_col = (
    "subject_id",
    "gender",
    "anchor_age",
    "anchor_year",
    "anchor_year_group",
    "chartdate",
    "result_name",
    "result_value",
    "seq_num",
    "hadm_id",
    "admittime",
    "admission_type",
    "icd_code",
    "icd_version",
    "emar_id",
    "emar_seq",
    "charttime",
    "storetime",
    "pharmacy_id",
    "drug_type",
    "drug",
    "proc_type",
    "entertime",
)


def clean(filename):
    """
    Cleans the files in the Files directory and saves them in the CleanedFiles directory

    Parameters:
    filename (str): The name of the file to be cleaned
    """
    temp_path = f"{path}/{filename}"
    target_path = Path(__file__).parent / f"CleanedFiles/cleaned_{filename}"

    df = pd.read_csv(open(temp_path))

    for c in df.columns:
        if c in nn_col:
            df = df[df[c].notna()]

    df.to_csv(target_path, index=False, encoding="utf-8", header=True)


for filename in os.listdir(path):
    clean(filename)


# Cleaning the patients.csv file with specific conditions
path = Path(__file__).parent / "CleanedFiles/cleaned_patients.csv"

patients = pd.read_csv(open(path))

deleteCondition = patients[
    (patients["anchor_age"] < 0)
    | (patients["anchor_age"] > 120)  # Check if age is lower than 0 or higher than 120
].index
patients.drop(deleteCondition, inplace=True)

patients.to_csv(path, index=False, encoding="utf-8", header=True)


# CLeaning the omr.csv file with specific conditions
path = Path(__file__).parent / "CleanedFiles/cleaned_omr.csv"

omr = pd.read_csv(open(path))

bp_temp = omr[omr["result_name"] == "Blood Pressure"]
omr = omr[omr["result_name"] != "Blood Pressure"]

omr["result_value"] = pd.to_numeric(omr["result_value"], errors="coerce")

deleteCondition = omr[
    (
        (
            omr["result_name"] == "Weight (Lbs)"
        )  # Check if Weight-value is higher than 1500Lbs (> than highest recorded weight) or lower than 1 (< than smallest baby)
        & ((omr["result_value"] >= 1500) | (omr["result_value"] <= 1))
    )
    | (
        (
            omr["result_name"] == "Height (Inches)"
        )  # Check if Height-value is higher than 110 (> than highest recorded height) or lower than 15 (< than smallest baby)
        & ((omr["result_value"] >= 110) | (omr["result_value"] <= 15))
    )
    | (
        omr["result_name"] == "BMI (kg/m2)"
    )  # Check if BMI-value is higher than 250 (> than highest recorded BMI) or lower than 7 (< than lowest recorded BMI)
    & ((omr["result_value"] >= 250) | (omr["result_value"] <= 7))
    | omr["result_value"].isnull()
].index
omr.drop(deleteCondition, inplace=True)
omr["result_value"] = omr["result_value"].astype(object)
omr = pd.concat([omr, bp_temp], ignore_index=True)

omr.to_csv(path, index=False, encoding="utf-8", header=True)

print("--- %s seconds ---" % (time.time() - start_time))
