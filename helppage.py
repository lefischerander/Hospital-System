from tkinter import Tk, Button, messagebox, Label, Entry, Toplevel, Frame, LEFT, RIGHT
import tkinter.ttk as ttk
import sys

class HelpPage:
    def help_page():
        help_window = Tk()
        help_window.title("Help Page")
        help_window.geometry("800x600")
        
        Label(help_window, text="Help Page", font=("Arial", 20)).pack(pady=10)
        Label(help_window, text="Welcome to the Help Page", font=("Arial", 15)).pack(pady=10)
        Label(help_window, text="This is the help page for the Hospital Management System", font=("Arial", 15)).pack(pady=10)
        Label(help_window, text="If you need help, please contact the system administrator", font=("Arial", 15)).pack(pady=10)
        Button(help_window, text="Close", font=("Arial", 15), command=help_window.destroy).pack(pady=10)
        help_window.mainloop()