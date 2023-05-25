import re

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
    
