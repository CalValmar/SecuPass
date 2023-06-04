import requests

def fetch_password_check_result(password):
    url = 'https://password.kaspersky.com/'
    data = {
        'password': password
    }
    response = requests.post(url, data=data)
    return response.text

# Demande à l'utilisateur de saisir un mot de passe
user_password = input("Entrez votre mot de passe : ")

# Effectue la requête vers le site et affiche la réponse
result = fetch_password_check_result(user_password)
print(result)
