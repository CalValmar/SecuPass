import re
import tkinter as tk
from tkinter import messagebox

def password_strength(password):
    # Vérification de la longueur minimale
    if len(password) < 8:
        return "Faible"
    
    # Vérification de la complexité
    complexity = 0
    
    # Vérification de la présence de chiffres
    if re.search(r'\d', password):
        complexity += 1
    
    # Vérification de la présence de lettres minuscules
    if re.search(r'[a-z]', password):
        complexity += 1
    
    # Vérification de la présence de lettres majuscules
    if re.search(r'[A-Z]', password):
        complexity += 1
    
    # Vérification de la présence de caractères spéciaux
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        complexity += 1
    
    # Vérification de l'absence de caractères répétitifs
    if not re.search(r'(.)\1{2,}', password):
        complexity += 1
    
    # Vérification de la résistance aux attaques par force brute
    brute_force_resistant = True
    
    # Vérification de la présence de séquences de chiffres consécutifs (123, 789, etc.)
    if re.search(r'\d{3}', password):
        brute_force_resistant = False
    
    # Vérification de la présence de séquences de lettres consécutives (abc, xyz, etc.)
    if re.search(r'[a-zA-Z]{3}', password):
        brute_force_resistant = False
    
    # Attribution de la force en fonction de la complexité et de la résistance aux attaques par force brute
    if complexity < 3 or not brute_force_resistant:
        return "Moyen"
    elif complexity < 5:
        return "Fort"
    else:
        return "Très fort"

def check_password():
    mot_de_passe = password_entry.get()
    force = password_strength(mot_de_passe)
    messagebox.showinfo("Résultat", f"Force du mot de passe selon SecuPass : {force}")

# Création de la fenêtre
window = tk.Tk()
window.title("SecuPass - Checker de mots de passe")

# Création du libellé et de la zone de saisie pour le mot de passe
password_label = tk.Label(window, text="Mot de passe :")
password_label.pack()

password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Création du bouton pour vérifier le mot de passe
check_button = tk.Button(window, text="Vérifier", command=check_password)
check_button.pack()

# Lancement de la boucle principale de la fenêtre
window.mainloop()
