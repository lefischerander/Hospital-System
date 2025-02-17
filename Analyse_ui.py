from test_analyse import Analyse
from tkinter import Tk, Frame, Label, RAISED
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
            if selection == "omr":
                omr = call_analyse.read_omr(subject_id)
                omr_window = Tk()
                omr_window.title("OMR")
                omr_window.geometry("800x600")

                omr_list = ["chartdate", "resultname", "result_value"]
                for i in range(len(omr_list)):
                    for j in range(len(omr)+1):
                        omr_grid = Frame(
                            master=omr_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        omr_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(omr_grid, text=omr_list[i]).pack()
                        else:
                            Label(omr_grid, text=omr[j-1][i]).pack()
                        
            elif selection == "admissions":
                admissions = call_analyse.read_admissions(subject_id)
                admissions_window = Tk()
                admissions_window.title("Admissions")
                admissions_window.geometry("800x600")

                admissions_list = ["subject_id", "hadm_id", "admission_type" , "admittime", "dischtime", "deathtime", "insurance", "edregtime", "edouttime", "gender", "hospital_expire_flag"]
                for i in range(len(admissions_list)):
                    for j in range(len(admissions)+1):
                        admissions_grid = Frame(
                            master=admissions_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        admissions_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(admissions_grid, text=admissions_list[i]).pack()
                        else:
                            Label(admissions_grid, text=admissions[j-1][i]).pack()

            elif selection == "diagnoses_icd":
                diagnoses_icd = call_analyse.read_diagnoses_icd(subject_id)
                diagnoses_icd_window = Tk()
                diagnoses_icd_window.title("Diagnoses ICD")
                diagnoses_icd_window.geometry("800x600")

                diagnoses_icd_list = ["shadm_id", "seq_num", "icd_code", "long_title", "icd_version"]
                for i in range(len(diagnoses_icd_list)):
                    for j in range(len(diagnoses_icd)+1):
                        diagnoses_icd_grid = Frame(
                            master=diagnoses_icd_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        diagnoses_icd_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(diagnoses_icd_grid, text=diagnoses_icd_list[i]).pack()
                        else:
                            Label(diagnoses_icd_grid, text=diagnoses_icd[j-1][i]).pack()
                    
            elif selection == "drgcodes":
                drgcodes = call_analyse.read_drgcodes(subject_id)
                drgcodes_window = Tk()
                drgcodes_window.title("DRG Codes")
                drgcodes_window.geometry("800x600")

                drgcodes_list = ["hadm_id", "drg_code", "description", "drg_severity", "drg_mortality"]
                for i in range(len(drgcodes_list)):
                    for j in range(len(drgcodes)+1):
                        drgcodes_grid = Frame(
                            master=drgcodes_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        drgcodes_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(drgcodes_grid, text=drgcodes_list[i]).pack()
                        else:
                            Label(drgcodes_grid, text=drgcodes[j-1][i]).pack()

            elif selection == "emar":
                emar = call_analyse.read_emar(subject_id)
                emar_window = Tk()
                emar_window.title("EMAR")
                emar_window.geometry("800x600")

                emar_list = ["hadm_id", "pharmacy_id", "medication", "charttime", "scheduletime", "event_txt"]
                for i in range(len(emar_list)):
                    for j in range(len(emar)+1):
                        emar_grid = Frame(
                            master=emar_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        emar_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(emar_grid, text=emar_list[i]).pack()
                        else:
                            Label(emar_grid, text=emar[j-1][i]).pack()

            elif selection == "patients":
                patients = call_analyse.read_patients(subject_id)
                patients_window = Tk()
                patients_window.title("Patients")
                patients_window.geometry("800x600")

                patients_list = ["subject_id", "gender", "anchor_age", "dod"]
                for i in range(len(patients_list)):
                    for j in range(len(patients)+1):
                        patients_grid = Frame(
                            master=patients_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        patients_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(patients_grid, text=patients_list[i]).pack()
                        else:
                            Label(patients_grid, text=patients[j-1][i]).pack()

            elif selection == "pharmacy":
                pharmacy = call_analyse.read_pharmacy(subject_id)
                pharmacy_window = Tk()
                pharmacy_window.title("Pharmacy")
                pharmacy_window.geometry("800x600")

                pharmacy_list = ["hadm_id", "pharmacy_id", "medication", "proc_type", "frequency", "starttime", "stoptime"]
                for i in range(len(pharmacy_list)):
                    for j in range(len(pharmacy)+1):
                        pharmacy_grid = Frame(
                            master=pharmacy_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        pharmacy_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(pharmacy_grid, text=pharmacy_list[i]).pack()
                        else:
                            Label(pharmacy_grid, text=pharmacy[j-1][i]).pack()

            elif selection == "procedures_icd":
                procrdures_icd = call_analyse.read_procedures_icd(subject_id)
                procedures_icd_window = Tk()
                procedures_icd_window.title("Procedures ICD")
                procedures_icd_window.geometry("800x600")

                procedures_icd_list = ["hadm_id", "chartdate", "seq_num", "icd_code", "long_title", "icd_version"]
                for i in range(len(procedures_icd_list)):
                    for j in range(len(procrdures_icd)+1):
                        procedures_icd_grid = Frame(
                            master=procedures_icd_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        procedures_icd_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(procedures_icd_grid, text=procedures_icd_list[i]).pack()
                        else:
                            Label(procedures_icd_grid, text=procrdures_icd[j-1][i]).pack()

        print(subject_id)

        analyse_window = Tk()
        analyse_window.title("Analyse")
        analyse_window.geometry("400x300")
        combo = ttk.Combobox(
            master=analyse_window,
            values=[
                "omr",
                "admissions",
                "diagnoses_icd",
                "drgcodes",
                "emar",
                "patients",
                "pharmacy",
                "procedures_icd",
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

        def selected_option(event):  # arg: event is necessary
            """This method is responsible for calling the right function from the combobox input"""
            selection = combo.get()
            id = int(subject_id)
            call_analyse = Analyse()
            print(id)
            print(selection)
            if selection == "omr":
                omr = call_analyse.read_omr(subject_id)
                omr_window = Tk()
                omr_window.title("OMR")
                omr_window.geometry("800x600")

                omr_list = ["chartdate", "resultname", "result_value"]
                for i in range(len(omr_list)):
                    for j in range(len(omr)+1):
                        omr_grid = Frame(
                            master=omr_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        omr_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(omr_grid, text=omr_list[i]).pack()
                        else:
                            Label(omr_grid, text=omr[j-1][i]).pack()
                        
            elif selection == "admissions":
                admissions = call_analyse.read_admissions(subject_id)
                admissions_window = Tk()
                admissions_window.title("Admissions")
                admissions_window.geometry("800x600")

                admissions_list = ["subject_id", "hadm_id", "admission_type" , "admittime", "dischtime", "deathtime", "insurance", "edregtime", "edouttime", "gender", "hospital_expire_flag"]
                for i in range(len(admissions_list)):
                    for j in range(len(admissions)+1):
                        admissions_grid = Frame(
                            master=admissions_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        admissions_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(admissions_grid, text=admissions_list[i]).pack()
                        else:
                            Label(admissions_grid, text=admissions[j-1][i]).pack()
                            
            elif selection == "diagnoses_icd":
                diagnoses_icd = call_analyse.read_diagnoses_icd(subject_id)
                diagnoses_icd_window = Tk()
                diagnoses_icd_window.title("Diagnoses ICD")
                diagnoses_icd_window.geometry("800x600")

                diagnoses_icd_list = ["shadm_id", "seq_num", "icd_code", "long_title", "icd_version"]
                for i in range(len(diagnoses_icd_list)):
                    for j in range(len(diagnoses_icd)+1):
                        diagnoses_icd_grid = Frame(
                            master=diagnoses_icd_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        diagnoses_icd_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(diagnoses_icd_grid, text=diagnoses_icd_list[i]).pack()
                        else:
                            Label(diagnoses_icd_grid, text=diagnoses_icd[j-1][i]).pack()
                    
            elif selection == "drgcodes":
                drgcodes = call_analyse.read_drgcodes(subject_id)
                drgcodes_window = Tk()
                drgcodes_window.title("DRG Codes")
                drgcodes_window.geometry("800x600")

                drgcodes_list = ["hadm_id", "drg_code", "description", "drg_severity", "drg_mortality"]
                for i in range(len(drgcodes_list)):
                    for j in range(len(drgcodes)+1):
                        drgcodes_grid = Frame(
                            master=drgcodes_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        drgcodes_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(drgcodes_grid, text=drgcodes_list[i]).pack()
                        else:
                            Label(drgcodes_grid, text=drgcodes[j-1][i]).pack()

            elif selection == "emar":
                emar = call_analyse.read_emar(subject_id)
                emar_window = Tk()
                emar_window.title("EMAR")
                emar_window.geometry("800x600")

                emar_list = ["hadm_id", "pharmacy_id", "medication", "charttime", "scheduletime", "event_txt"]
                for i in range(len(emar_list)):
                    for j in range(len(emar)+1):
                        emar_grid = Frame(
                            master=emar_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        emar_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(emar_grid, text=emar_list[i]).pack()
                        else:
                            Label(emar_grid, text=emar[j-1][i]).pack()

            elif selection == "patients":
                patients = call_analyse.read_patients(subject_id)
                patients_window = Tk()
                patients_window.title("Patients")
                patients_window.geometry("800x600")

                patients_list = ["subject_id", "gender", "anchor_age", "dod"]
                for i in range(len(patients_list)):
                    for j in range(len(patients)+1):
                        patients_grid = Frame(
                            master=patients_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        patients_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(patients_grid, text=patients_list[i]).pack()
                        else:
                            Label(patients_grid, text=patients[j-1][i]).pack()

            elif selection == "pharmacy":
                pharmacy = call_analyse.read_pharmacy(subject_id)
                pharmacy_window = Tk()
                pharmacy_window.title("Pharmacy")
                pharmacy_window.geometry("800x600")

                pharmacy_list = ["hadm_id", "pharmacy_id", "medication", "proc_type", "frequency", "starttime", "stoptime"]
                for i in range(len(pharmacy_list)):
                    for j in range(len(pharmacy)+1):
                        pharmacy_grid = Frame(
                            master=pharmacy_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        pharmacy_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(pharmacy_grid, text=pharmacy_list[i]).pack()
                        else:
                            Label(pharmacy_grid, text=pharmacy[j-1][i]).pack()

            elif selection == "procedures_icd":
                procrdures_icd = call_analyse.read_procedures_icd(subject_id)
                procedures_icd_window = Tk()
                procedures_icd_window.title("Procedures ICD")
                procedures_icd_window.geometry("800x600")

                procedures_icd_list = ["hadm_id", "chartdate", "seq_num", "icd_code", "long_title", "icd_version"]
                for i in range(len(procedures_icd_list)):
                    for j in range(len(procrdures_icd)+1):
                        procedures_icd_grid = Frame(
                            master=procedures_icd_window,
                            relief=RAISED,
                            borderwidth=1,
                            width=15
                            )
                        
                        procedures_icd_grid.grid(
                            row=i,
                            column=j,
                            padx=5,
                            pady=5
                            )
                        if j == 0:
                            Label(procedures_icd_grid, text=procedures_icd_list[i]).pack()
                        else:
                            Label(procedures_icd_grid, text=procrdures_icd[j-1][i]).pack()

        analyse_window = Tk()
        analyse_window.title("Analyse")
        analyse_window.geometry("400x300")
        combo = ttk.Combobox(
            master=analyse_window,
            values=[
                "omr",
                "admissions",
                "diagnoses_icd",
                "drgcodes",
                "emar",
                "patients",
                "pharmacy",
                "procedures_icd",
                "d_icd_diagnoses",
                "d_icd_procedures",
            ],
        )
        combo.pack()
        combo.bind("<<ComboboxSelected>>", selected_option)
        analyse_window.mainloop()
