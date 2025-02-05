from test_analyse import Analyse
import pandas as pd

def main():
    analyse = Analyse()
    try:
        test = input("Enter the name of the file you want to read: ")
        if test == "omr":
            print(analyse.read_omr())
        elif test == "admissions":
            print(analyse.read_admissions().head(10))
        elif test == "diagnoses_icd":
            print(analyse.read_diagnoses_icd().head(10))
        elif test == "drgcodes":
            print(analyse.read_drgcodes().head(10))
        elif test == "emar":
            print(analyse.read_emar().head(10))
        elif test == "patients":
            print(analyse.read_patients().head(10))
        elif test == "pharmacy":
            print(analyse.read_pharmacy().head(10))
        elif test == "procedures_icd":
            print(analyse.read_procedures_icd().head(10))
        elif test == "d_icd_diagnoses":
            print(analyse.read_d_icd_diagnoses().head(10))
        elif test == "d_icd_procedures":
            print(analyse.read_d_icd_procedures().head(10))
        else:
            print("Invalid input")
    except FileNotFoundError:
        print(f"File not found: {test}")
    except pd.errors.EmptyDataError:
        print(f"No data: {test}")
    except pd.errors.ParserError:
        print(f"Parse error: {test}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()