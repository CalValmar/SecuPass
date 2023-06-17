import re                                           # https://docs.python.org/3/library/re.html
import time                                         # https://docs.python.org/3/library/time.html
import itertools                                    # https://docs.python.org/3/library/itertools.html
from concurrent.futures import ProcessPoolExecutor  # https://docs.python.org/3/library/concurrent.futures.html

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
    elif complexity == 4:
        print("Your password is medium, you should change it.")
    elif complexity == 5 and not brute_force(password):
        print("Your password is strong but can be cracked by brute force.")
    elif complexity == 5 and brute_force(password):
        print("Your password is strong and cannot be cracked by brute force.")
    elif complexity == 6:
        print("Your password is very strong and cannot be cracked by brute force.")
    else:
        print("Your password is very strong and cannot be cracked by brute force.")


# ~~~~~ Brute Force Helper ~~~~~ #
# Helper function for brute_force()

def brute_force_helper(args):
    attempt, password = args
    if attempt == password:
        return True
    return False


# ~~~~~ Brute Force ~~~~~ #
# Check if your password can be cracked by brute force

def brute_force(password):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-='
    length = len(password)
    max_workers = 8  # Number of threads to use

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = []

        print("Brute force attack in progress...")
        print("Number of threads used:", max_workers)
        print("clock time:", time.ctime())
        print("")

        for i in range(length, length + 1):
            combinations = itertools.product(chars, repeat=i)
            for combination in combinations:
                attempt = ''.join(combination)
                futures.append(executor.submit(brute_force_helper, (attempt, password)))
                print(attempt)


        start_time = time.time()
    
        for future in futures:
            if future.result():
                print("Your password can be cracked by brute force.")
                end_time = time.time()
                duration = end_time - start_time
                print("Brute force attack took {:.2f} seconds.".format(duration))
                return True

    print("Your password cannot be cracked by brute force.")
    return False


if __name__ == "__main__":
    password_strength(password)
    time.sleep(5)
