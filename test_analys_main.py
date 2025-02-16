from test_analyse import Analyse
import pandas as pd


def analyse_main():
    analyse = Analyse()
    try:
        test = input("Enter the name of the file you want to read: ")
        id = input("Enter the patient's id: ")
        if test == "omr":
            print(analyse.read_omr(id))
        elif test == "admissions":
            print(analyse.read_admissions(id))
        elif test == "diagnoses_icd":
            print(analyse.read_diagnoses_icd(id))
        elif test == "drgcodes":
            print(analyse.read_drgcodes(id))
        elif test == "emar":
            print(analyse.read_emar(id))
        elif test == "patients":
            print(analyse.read_patients(id))
        elif test == "pharmacy":
            print(analyse.read_pharmacy(id))
        elif test == "procedures_icd":
            print(analyse.read_procedures_icd(id))
        elif test == "d_icd_diagnoses":
            print(analyse.read_d_icd_diagnoses())
        elif test == "d_icd_procedures":
            print(analyse.read_d_icd_procedures())
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
    analyse_main()
