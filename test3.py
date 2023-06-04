import requests
from bs4 import BeautifulSoup

url = 'https://password.kaspersky.com'
password = 'your_password'

payload = {'password': password}
response = requests.post(url, data=payload)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    strength_element = soup.find('input', class_="passwd-check pl-4")
    if strength_element:
        strength = strength_element['value']
        print("Kaspersky Password Strength:", strength)
    else:
        print("Failed to retrieve Kaspersky Password Strength.")
else:
    print("Failed to connect to Kaspersky Password Checker.")
