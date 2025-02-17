from test_analyse import Analyse
from tkinter import Tk
import tkinter.ttk as ttk


class Analyse_ui:
    """This class is responsible for the user interface of the Analyse class"""

    def analyse_action_main(subject_id):
        """This method is responsible for the main actions of the Analyse class for patients and admins

        Args:
            subject_id (int): The id of the user
        """

        def selected_option(event):  # arg: event might be unnecessary
            """This method is responsible for calling the right function from the combobox input"""
            selection = combo.get()
            call_analyse = Analyse()
            if selection == "Medical Records":
                omr = call_analyse.read_omr(subject_id)
                omr_window = Tk()
                omr_window.title("OMR")
                omr_window.geometry("800x600")

                tree = ttk.Treeview(omr_window)

                tree["columns"] = list(omr.columns)
                tree["show"] = "headings"

                for column in omr.columns:
                    tree.heading(column, text=column)

                for index, row in omr.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

            elif selection == "Hospital Visits":
                admissions = call_analyse.read_admissions(subject_id)
                admissions_window = Tk()
                admissions_window.title("Admissions")
                admissions_window.geometry("800x600")

                tree = ttk.Treeview(admissions_window)

                tree["columns"] = list(admissions.columns)
                tree["show"] = "headings"

                for column in admissions.columns:
                    tree.heading(column, text=column)

                for index, row in admissions.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

            elif selection == "Diagnoses":
                diagnoses_icd = call_analyse.read_diagnoses_icd(subject_id)
                diagnoses_icd_window = Tk()
                diagnoses_icd_window.title("Diagnoses ICD")
                diagnoses_icd_window.geometry("800x600")

                tree = ttk.Treeview(diagnoses_icd_window)

                tree["columns"] = list(diagnoses_icd.columns)
                tree["show"] = "headings"

                for column in diagnoses_icd.columns:
                    tree.heading(column, text=column)

                for index, row in diagnoses_icd.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

            elif selection == "Diagnosis Related Group (DRG)":
                drgcodes = call_analyse.read_drgcodes(subject_id)
                drgcodes_window = Tk()
                drgcodes_window.title("DRG Codes")
                drgcodes_window.geometry("800x600")

                tree = ttk.Treeview(drgcodes_window)

                tree["columns"] = list(drgcodes.columns)
                tree["show"] = "headings"

                for column in drgcodes.columns:
                    tree.heading(column, text=column)

                for index, row in drgcodes.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

            elif selection == "Electronic Medicine Administration Record (eMAR)":
                emar = call_analyse.read_emar(subject_id)
                emar_window = Tk()
                emar_window.title("EMAR")
                emar_window.geometry("800x600")

                tree = ttk.Treeview(emar_window)

                tree["columns"] = list(emar.columns)
                tree["show"] = "headings"

                for column in emar.columns:
                    tree.heading(column, text=column)

                for index, row in emar.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

            elif selection == "Patient Data":
                patients = call_analyse.read_patients(subject_id)
                patients_window = Tk()
                patients_window.title("Patients")
                patients_window.geometry("800x600")

                tree = ttk.Treeview(patients_window)

                tree["columns"] = list(patients.columns)
                tree["show"] = "headings"

                for column in patients.columns:
                    tree.heading(column, text=column)

                for index, row in patients.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

            elif selection == "Medication":
                pharmacy = call_analyse.read_pharmacy(subject_id)
                pharmacy_window = Tk()
                pharmacy_window.title("Pharmacy")
                pharmacy_window.geometry("800x600")

                tree = ttk.Treeview(pharmacy_window)

                tree["columns"] = list(pharmacy.columns)
                tree["show"] = "headings"

                for column in pharmacy.columns:
                    tree.heading(column, text=column)

                for index, row in pharmacy.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

            elif selection == "Procedures":
                procedures_icd = call_analyse.read_procedures_icd(subject_id)
                procedures_icd_window = Tk()
                procedures_icd_window.title("Procedures ICD")
                procedures_icd_window.geometry("800x600")

                tree = ttk.Treeview(procedures_icd_window)

                tree["columns"] = list(procedures_icd.columns)
                tree["show"] = "headings"

                for column in procedures_icd.columns:
                    tree.heading(column, text=column)

                for index, row in procedures_icd.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

        print(subject_id)

        analyse_window = Tk()
        analyse_window.title("Analyse")
        analyse_window.geometry("400x300")
        combo = ttk.Combobox(
            master=analyse_window,
            values=[
                "Medical Records",
                "Hospital Visits",
                "Diagnoses",
                "Procedures",
                "Diagnosis Related Group (DRG)",
                "Electronic Medicine Administration Record (eMAR)",
                "Patient Data",
                "Medication",
            ],
        )
        combo.pack()
        combo.bind("<<ComboboxSelected>>", selected_option)
        analyse_window.mainloop()

    def analyse_action_doctor(subject_id):
        """This method is responsible for the main actions of the Analyse class for doctors

        Args:
            subject_id (int): The id of the patient the doctor wants to view
        """

        def selected_option(event):  # arg: event might be unnecessary
            """This method is responsible for calling the right function from the combobox input"""
            selection = combo.get()
            call_analyse = Analyse()
            if selection == "Medical Records":
                omr = call_analyse.read_omr(subject_id)
                omr_window = Tk()
                omr_window.title("OMR")
                omr_window.geometry("800x600")

                tree = ttk.Treeview(omr_window)

                tree["columns"] = list(omr.columns)
                tree["show"] = "headings"

                for column in omr.columns:
                    tree.heading(column, text=column)

                for index, row in omr.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

            elif selection == "Hospital Visits":
                admissions = call_analyse.read_admissions(subject_id)
                admissions_window = Tk()
                admissions_window.title("Admissions")
                admissions_window.geometry("800x600")

                tree = ttk.Treeview(admissions_window)

                tree["columns"] = list(admissions.columns)
                tree["show"] = "headings"

                for column in admissions.columns:
                    tree.heading(column, text=column)

                for index, row in admissions.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

            elif selection == "Diagnoses":
                diagnoses_icd = call_analyse.read_diagnoses_icd(subject_id)
                diagnoses_icd_window = Tk()
                diagnoses_icd_window.title("Diagnoses ICD")
                diagnoses_icd_window.geometry("800x600")

                tree = ttk.Treeview(diagnoses_icd_window)

                tree["columns"] = list(diagnoses_icd.columns)
                tree["show"] = "headings"

                for column in diagnoses_icd.columns:
                    tree.heading(column, text=column)

                for index, row in diagnoses_icd.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

            elif selection == "Diagnosis Related Group (DRG)":
                drgcodes = call_analyse.read_drgcodes(subject_id)
                drgcodes_window = Tk()
                drgcodes_window.title("DRG Codes")
                drgcodes_window.geometry("800x600")

                tree = ttk.Treeview(drgcodes_window)

                tree["columns"] = list(drgcodes.columns)
                tree["show"] = "headings"

                for column in drgcodes.columns:
                    tree.heading(column, text=column)

                for index, row in drgcodes.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

            elif selection == "Electronic Medicine Administration Record (eMAR)":
                emar = call_analyse.read_emar(subject_id)
                emar_window = Tk()
                emar_window.title("EMAR")
                emar_window.geometry("800x600")

                tree = ttk.Treeview(emar_window)

                tree["columns"] = list(emar.columns)
                tree["show"] = "headings"

                for column in emar.columns:
                    tree.heading(column, text=column)

                for index, row in emar.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

            elif selection == "Patient Data":
                patients = call_analyse.read_patients(subject_id)
                patients_window = Tk()
                patients_window.title("Patients")
                patients_window.geometry("800x600")

                tree = ttk.Treeview(patients_window)

                tree["columns"] = list(patients.columns)
                tree["show"] = "headings"

                for column in patients.columns:
                    tree.heading(column, text=column)

                for index, row in patients.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

            elif selection == "Medication":
                pharmacy = call_analyse.read_pharmacy(subject_id)
                pharmacy_window = Tk()
                pharmacy_window.title("Pharmacy")
                pharmacy_window.geometry("800x600")

                tree = ttk.Treeview(pharmacy_window)

                tree["columns"] = list(pharmacy.columns)
                tree["show"] = "headings"

                for column in pharmacy.columns:
                    tree.heading(column, text=column)

                for index, row in pharmacy.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

            elif selection == "Procedures":
                procedures_icd = call_analyse.read_procedures_icd(subject_id)
                procedures_icd_window = Tk()
                procedures_icd_window.title("Procedures ICD")
                procedures_icd_window.geometry("800x600")

                tree = ttk.Treeview(procedures_icd_window)

                tree["columns"] = list(procedures_icd.columns)
                tree["show"] = "headings"

                for column in procedures_icd.columns:
                    tree.heading(column, text=column)

                for index, row in procedures_icd.iterrows():
                    tree.insert("", "end", values=list(row))

                tree.pack(expand=True, fill="both")

        print(subject_id)

        analyse_window = Tk()
        analyse_window.title("Analyse")
        analyse_window.geometry("400x300")
        combo = ttk.Combobox(
            master=analyse_window,
            values=[
                "Medical Records",
                "Hospital Visits",
                "Diagnoses",
                "Procedures",
                "Diagnosis Related Group (DRG)",
                "Electronic Medicine Administration Record (eMAR)",
                "Patient Data",
                "Medication",
            ],
        )
        combo.pack()
        combo.bind("<<ComboboxSelected>>", selected_option)
        analyse_window.mainloop()
