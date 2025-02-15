from test_analyse import Analyse
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk

class Analyse_ui:
    def analyse_action_main(subject_id):
        def selected_option(event):
            selection = combo.get()
            if selection == "omr":
                print(Analyse.read_omr(subject_id))
            elif selection == "admissions":
                print(Analyse.read_admissions(subject_id))
            elif selection == "diagnoses_icd":
                print(Analyse.read_diagnoses_icd(subject_id))
            elif selection == "drgcodes":
                print(Analyse.read_drgcodes(subject_id))
            elif selection == "emar":
                print(Analyse.read_emar(subject_id))
            elif selection == "patients":
                print(Analyse.read_patients(subject_id))
            elif selection == "pharmacy":
                print(Analyse.read_pharmacy(subject_id))
            elif selection == "procedures_icd":
                print(Analyse.read_procedures_icd(subject_id))

        analyse_window = tk.Tk()  
        analyse_window.title("Analyse")
        analyse_window.geometry("400x300")
        combo = ttk.Combobox(values=["omr", "admissions", "diagnoses_icd", "drgcodes", "emar", "patients", "pharmacy", "procedures_icd"])
        combo.bind("<<ComboboxSelected>>", selected_option)
        analyse_window.mainloop()

    def analyse_action_doctor(subject_id):
        def selected_option(event):
            selection = combo.get()
            if selection == "omr":
                print(Analyse.read_omr(subject_id))
            elif selection == "admissions":
                print(Analyse.read_admissions(subject_id))
            elif selection == "diagnoses_icd":
                print(Analyse.read_diagnoses_icd(subject_id))
            elif selection == "drgcodes":
                print(Analyse.read_drgcodes(subject_id))
            elif selection == "emar":
                print(Analyse.read_emar(subject_id))
            elif selection == "patients":
                print(Analyse.read_patients(subject_id))
            elif selection == "pharmacy":
                print(Analyse.read_pharmacy(subject_id))
            elif selection == "procedures_icd":
                print(Analyse.read_procedures_icd(subject_id))
            elif selection == "d_icd_diagnoses":
                print(Analyse.read_d_icd_diagnoses(subject_id))
            elif selection == "d_icd_procedures":
                print(Analyse.read_d_icd_procedures(subject_id))

        analyse_window = tk.Tk()  
        analyse_window.title("Analyse")
        analyse_window.geometry("400x300")
        combo = ttk.Combobox(values=["omr", "admissions", "diagnoses_icd", "drgcodes", "emar", "patients", "pharmacy", "procedures_icd", "d_icd_diagnoses", "d_icd_procedures"])
        combo.bind("<<ComboboxSelected>>", selected_option)
        analyse_window.mainloop()
