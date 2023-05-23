import string           # https://docs.python.org/3/library/string.html
import secrets          # https://docs.python.org/3/library/secrets.html
import time             # https://docs.python.org/3/library/time.html


characters = []


# ~~~~~ Password Characters ~~~~~ #
# Choose the characters you want in your password

def pass_length():
    length = input("How long do you want your password to be ? ")
    
    if length == "":
        length = 16
    else:
        try:
            length = int(length)
            if length < 8:
                print("\nYour password is too short. It has to be at least 8 characters long.")
                return pass_length()
            elif length > 60:
                print("\nYour password is too long. It has to be less than 60 characters long.")
                return pass_length()
        except ValueError:
            print("\nInvalid input. Please enter a valid integer for the password length.")
            return pass_length()    
    
    return length


def pass_lower_case():
    lower_case = input("Do you want lower case letters in your password ? [YES/NO] ")
    if lower_case == "YES" or lower_case == "yes":
        characters.extend(string.ascii_lowercase)
    elif lower_case == "NO" or lower_case == "no":
        lower_case = False
    elif lower_case == "":
        characters.extend(string.ascii_lowercase)
    else:
        print("\nInvalid input. Please enter YES or NO.")
        return pass_lower_case()


def pass_upper_case():
    upper_case = input("Do you want upper case letters in your password ? [YES/NO] ")
    if upper_case == "YES" or upper_case == "yes":
        characters.extend(string.ascii_uppercase)
    elif upper_case == "NO" or upper_case == "no":
        upper_case = False
    elif upper_case == "":
        characters.extend(string.ascii_uppercase)
    else:
        print("\nInvalid input. Please enter YES or NO.")
        return pass_upper_case()
    
    
def pass_digits():
    digits = input("Do you want digits in your password ? [YES/NO] ")
    if digits == "YES" or digits == "yes":
        characters.extend(string.digits)
    elif digits == "NO"or digits == "no":
        digits = False
    elif digits == "":
        characters.extend(string.digits)
    else:
        print("\nInvalid input. Please enter YES or NO.")
        return pass_digits()

    
def pass_symbols():
    symbols = input("Do you want symbols in your password ? [YES/NO] ")
    if symbols == "YES" or symbols == "yes":
        characters.extend(string.punctuation)
    elif symbols == "NO" or symbols == "no":
        symbols = False
    elif symbols == "":
        characters.extend(string.punctuation)
    else:
        print("\nInvalid input. Please enter YES or NO.")
        return pass_symbols()


# ~~~~~ Password Generator ~~~~~ # 
# Generate the password

def pass_gen(lenght, lower_case, upper_case, digits, symbols):
    if lower_case == False and upper_case == False and digits == False and symbols == False:
        print("\nYou have to choose at least one type of character for your password.")
        password = pass_gen(pass_length(), pass_lower_case(), pass_upper_case(), pass_digits(), pass_symbols())
    else:
        try:
            password = "".join(secrets.choice(characters) for i in range(lenght))
            return password
        except IndexError:
            print("\nYou have to choose at least one type of character for your password.")
            password = pass_gen(pass_length(), pass_lower_case(), pass_upper_case(), pass_digits(), pass_symbols())
    return password