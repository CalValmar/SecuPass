import re           # https://docs.python.org/3/library/re.html

# ~~~~~ Password Strength ~~~~~ #
# Check the strength of your password

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
        print("Your password is very weak, you should change it.")
    elif complexity == 4 and len(password) >= 8:
        print("Your password is weak, you should change it.")
    elif complexity == 5 and len(password) >= 8:
        print("Your password is medium.")
    elif complexity == 6:
        print("Your password is strong.")
    else:
        print("Invalid password.")