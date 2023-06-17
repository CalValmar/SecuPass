from pass_check import *        
from pass_gen import *
import tkinter as tk                # https://docs.python.org/fr/3/library/tkinter.html
from tkinter import messagebox      # https://docs.python.org/fr/3/library/tkinter.messagebox.html
import subprocess

# The GUI ask if execute pass_gen.py to generate a password or pass_check.py to check the strength of a password
# If the user click on "Generate a password", the GUI execute pass_gen.py
# If the user click on "Check the strength of a password", the GUI execute pass_check.py
# If the user click on "Exit", the GUI close
# If the user click on "Help", the GUI display a messagebox with the help
# If the user click on "About", the GUI display a messagebox with the about
# If the user click on "Contact", the GUI display a messagebox with the contact

def execute_pass_gen():
    subprocess.run(["python3", "pass_gen.py"])

def execute_pass_check():
    subprocess.run(["python3", "pass_check.py"])

def display_about():
    messagebox.showinfo("About", "SecuPass a simple password generator and checker. It is written in python3 and uses the tkinter library for the GUI.")

def exit_gui():
    root.destroy()


# ~~~~~ GUI ~~~~~ #

root = tk.Tk()
root.title("SecuPass - Password Manager")

generate_button = tk.Button(root, text="Generate a password", command=execute_pass_gen)
generate_button.pack()

check_button = tk.Button(root, text="Check the strength of a password", command=execute_pass_check)
check_button.pack()

about_button = tk.Button(root, text="About", command=display_about)
about_button.pack()

exit_button = tk.Button(root, text="Exit", command=exit_gui)
exit_button.pack()

root.mainloop()