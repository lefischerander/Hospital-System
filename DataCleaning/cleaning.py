import pandas as pd
from pathlib import Path
import os

pd.options.mode.chained_assignment = None


def clean_empty_col(df, column):
    """
    Function to clean the dataframe from empty rows in a specified column

    Parameters:
    df (DataFrame): The DataFrame to be cleaned
    column (str): The column to be checked for empty rows

    Returns:
    df (DataFrame): The cleaned DataFrame
    """
    df = df.dropna(subset=[column])
    return df


path = Path(__file__).parent / "Files/"

# Cleaning the files
for filename in os.listdir(path):
    temp_path = f"{path}/{filename}"
    target_path = Path(__file__).parent / f"CleanedFiles/cleaned_{filename}"

    df = pd.read_csv(open(temp_path))

    # Cleaning the empty rows if the column exists
    if "subject_id" in df.columns:
        df = clean_empty_col(df, "subject_id")
    elif "gender" in df.columns:
        df = clean_empty_col(df, "gender")
    elif "anchor_age" in df.columns:
        df = clean_empty_col(df, "anchor_age")
    elif "anchor_year" in df.columns:
        df = clean_empty_col(df, "anchor_year")
    elif "anchor_year_group" in df.columns:
        df = clean_empty_col(df, "anchor_year_group")
    elif "chartdate" in df.columns:
        df = clean_empty_col(df, "chartdate")
    elif "result_name" in df.columns:
        df = clean_empty_col(df, "result_name")
    elif "result_value" in df.columns:
        df = clean_empty_col(df, "result_value")
    elif "seq_num" in df.columns:
        df = clean_empty_col(df, "seq_num")
    elif "hadm_id" in df.columns:
        df = clean_empty_col(df, "hadm_id")
    elif "admittime" in df.columns:
        df = clean_empty_col(df, "admittime")
    elif "admission_type" in df.columns:
        df = clean_empty_col(df, "admission_type")
    elif "icd_code" in df.columns:
        df = clean_empty_col(df, "icd_code")
    elif "icd_version" in df.columns:
        df = clean_empty_col(df, "icd_version")
    elif "emar_id" in df.columns:
        df = clean_empty_col(df, "emar_id")
    elif "emar_seq" in df.columns:
        df = clean_empty_col(df, "emar_seq")
    elif "charttime" in df.columns:
        df = clean_empty_col(df, "charttime")
    elif "storetime" in df.columns:
        df = clean_empty_col(df, "storetime")
    elif "pharmacy_id" in df.columns:
        df = clean_empty_col(df, "pharmacy_id")
    elif "drug_type" in df.columns:
        df = clean_empty_col(df, "drug_type")
    elif "drug" in df.columns:
        df = clean_empty_col(df, "drug")
    elif "proc_type" in df.columns:
        df = clean_empty_col(df, "proc_type")
    elif "entertime" in df.columns:
        df = clean_empty_col(df, "entertime")

    df.to_csv(target_path, index=False, encoding="utf-8", header=True)


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
