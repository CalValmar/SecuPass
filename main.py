from pass_check import *        
from pass_gen import *
from tkinter import *               # https://docs.python.org/fr/3/library/tkinter.html
from tkinter import messagebox      # https://docs.python.org/fr/3/library/tkinter.messagebox.html

banner = """

"""

if __name__ == "__main__":
    # Test for pass_gen.py
    lenght = pass_length()
    lower_case = pass_lower_case()
    upper_case = pass_upper_case()
    digits = pass_digits()
    symbols = pass_symbols()
    password = pass_gen(lenght, lower_case, upper_case, digits, symbols)
    print("Your password is", password)
    time.sleep(5)