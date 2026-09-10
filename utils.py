import re

def get_valid_integer(prompt_text, error_message):
    while True:
        try:
            return int(input(prompt_text))
        except ValueError:
            print(f"\033[91m{error_message}\033[0m\n")

def is_valid_gpa(gpa):
    try:
        gpa = float(gpa)
    except(ValueError,TypeError):
        return False
    
    if 0.0<= gpa <= 4.0:
        return True
    return False

def is_valid_year(year):
    try:
        year = int(year)
    except(ValueError,TypeError):
        return False
    
    return 1900 <= year <= 2100

def is_valid_name(name):
    if not isinstance(name, str):
        return False

    name = name.strip()

    if len(name) == 0:
        return False

    return name.replace(" ", "").isalpha()

def is_valid_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.fullmatch(pattern, email):
        return True
    return False

def get_valid_float(prompt_text, error_message, min_value=None, max_value=None):
    while True:
        try:
            value = float(input(prompt_text))

            if min_value is not None and value < min_value:
                print(f"\033[91mValue must be at least {min_value}.\033[0m\n")
                continue

            if max_value is not None and value > max_value:
                print(f"\033[91mValue must be at most {max_value}.\033[0m\n")
                continue

            return value

        except ValueError:
            print(f"\033[91m{error_message}\033[0m\n")

def get_valid_email(prompt_text, error_message):
    while True:
        email = input(prompt_text).strip()

        if (is_valid_email(email)):
            return email
        
        print(f"\033[91m{error_message}\033[0m\n")