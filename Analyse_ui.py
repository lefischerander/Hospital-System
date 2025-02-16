from test_analyse import Analyse
from tkinter import *
import tkinter.ttk as ttk

class Analyse_ui:
    """This class is responsible for the user interface of the Analyse class"""
    def analyse_action_main(subject_id):
        """This method is responsible for the main actions of the Analyse class for patients and admins
        
        Args:
            subject_id (int): The id of the user
        """
        def selected_option(event): # arg: event might be unnecessary
            """This method is responsible for calling the right function from the combobox input"""
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
        print(subject_id)

        analyse_window = Tk()  
        analyse_window.title("Analyse")
        analyse_window.geometry("400x300")
        combo = ttk.Combobox(master=analyse_window, values=["omr", "admissions", "diagnoses_icd", "drgcodes", "emar", "patients", "pharmacy", "procedures_icd"])
        combo.pack()
        combo.bind("<<ComboboxSelected>>", selected_option)
        analyse_window.mainloop()

    def analyse_action_doctor(subject_id):
        """This method is responsible for the main actions of the Analyse class for doctors
        
        Args:
            subject_id (int): The id of the patient the doctor wants to view
        """
        def selected_option(): # arg: event might be unnecessary
            """This method is responsible for calling the right function from the combobox input"""
            selection = combo.get()
            id = int(subject_id)
            print(id)
            print(selection)
            if selection == "omr":
                print(Analyse.read_omr(id))
            elif selection == "admissions":
                print(Analyse.read_admissions(id))
            elif selection == "diagnoses_icd":
                print(Analyse.read_diagnoses_icd(id))
            elif selection == "drgcodes":
                print(Analyse.read_drgcodes(id))
            elif selection == "emar":
                print(Analyse.read_emar(id))
            elif selection == "patients":
                print(Analyse.read_patients(id))
            elif selection == "pharmacy":
                print(Analyse.read_pharmacy(id))
            elif selection == "procedures_icd":
                print(Analyse.read_procedures_icd(id))
            elif selection == "d_icd_diagnoses":
                print(Analyse.read_d_icd_diagnoses())
            elif selection == "d_icd_procedures":
                print(Analyse.read_d_icd_procedures())

        analyse_window = Tk()  
        analyse_window.title("Analyse")
        analyse_window.geometry("400x300")
        combo = ttk.Combobox(master=analyse_window, values=["omr", "admissions", "diagnoses_icd", "drgcodes", "emar", "patients", "pharmacy", "procedures_icd", "d_icd_diagnoses", "d_icd_procedures"])
        combo.pack()
        combo.bind("<<ComboboxSelected>>", selected_option)
        analyse_window.mainloop()
