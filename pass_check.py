import re
import tkinter as tk
from tkinter import messagebox

def password_strength(password):
    complexity = 0

    if len(password) >= 12:
        complexity += 1

    if re.search(r'\d', password):
        complexity += 1

    if re.search(r'[a-z]', password):
        complexity += 1

    if re.search(r'[A-Z]', password):
        complexity += 1

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        complexity += 1

    if not re.search(r'(.)\1{2,}', password):
        complexity += 1

    if complexity <= 3:
        return "Your password is very weak, you should change it."
    elif complexity == 4 and len(password) >= 8:
        return "Your password is weak, you should change it."
    elif complexity == 5 and len(password) >= 8:
        return "Your password is medium."
    elif complexity == 6:
        return "Your password is strong."
    else:
        return "Invalid password."


# ~~~~~ GUI ~~~~~ #

def check_password_strength():
    password = entry.get()
    strength = password_strength(password)
    messagebox.showinfo("Password Strength", strength)

def toggle_password_visibility():
    if password_checkbox.get():
        entry.config(show="")
    else:
        entry.config(show="*")

def go_back():
    root.destroy()

root = tk.Tk()
root.title("Password Strength Checker")

label = tk.Label(root, text="Enter your password:")
label.pack()

entry = tk.Entry(root, show="*")
entry.pack()

password_checkbox = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Show password", variable=password_checkbox, command=toggle_password_visibility)
checkbox.pack()

check_button = tk.Button(root, text="Check", command=check_password_strength)
check_button.pack()

back_button = tk.Button(root, text="Back", command=go_back)
back_button.pack()

root.mainloop()
