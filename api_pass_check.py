import re
import requests
from bs4 import BeautifulSoup

password = input("Enter your password: ")
print("")

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
        print("Your password is weak, you should change it.")
    elif complexity == 4 and len(password) >= 8:
        print("Your password is medium, you should change it.")
    elif complexity == 5 and len(password) >= 8:
        print("Your password is strong.")
    elif complexity == 6:
        print("Your password is very strong.")
    else:
        print("Invalid password.")

    # Send password to Kaspersky Password Checker
    url = 'https://password.kaspersky.com/en/'
    response = requests.post(url, data={'password': password})

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        strength_element = soup.find('div', class_='password-rating-value')
        if strength_element:
            strength = strength_element.text.strip()
            print("Kaspersky Password Strength: ", strength)
        else:
            print("Failed to retrieve Kaspersky Password Strength.")
    else:
        print("Failed to connect to Kaspersky Password Checker.")


if __name__ == "__main__":
    password_strength(password)
