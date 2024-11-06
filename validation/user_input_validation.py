from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def name_check(name):
    """Checks if the name is valid or not."""

    name_parts = name.split()
    for part in name_parts:
        if not part.isalpha():
            print(Fore.RED + "Name not valid" + Style.RESET_ALL)
            return False
    if len(name) >= 100:
        print(Fore.RED + "Name not valid" + Style.RESET_ALL)
        return False
    return True

def age_check(age):

    """Checks if the age is valid or not."""

    if age < 18 or age >= 100:
        print(Fore.RED + "Age not valid" + Style.RESET_ALL)
        return False
    return True

def email_check(email):

    """Checks if the email is valid or not."""

    if len(email) <= 5 or "@" not in email or not email.endswith(".com"):
        print(Fore.RED + "Email not valid" + Style.RESET_ALL)
        return False
    return True

def number_check(number):
    
    """Checks if the number is valid or not."""

    if len(number) > 10 or not number.isnumeric():
        print(Fore.RED + "Number not valid" + Style.RESET_ALL)
        return False
    return True

def password_check(password):

    """Checks if password is valid or not."""

    if len(password) < 12:
        print(Fore.RED + "Password not valid" + Style.RESET_ALL)
        return False
    
    upper_check = False
    lower_check = False
    special_character_check = False
    digit_check = False

    for char in password:
        if char.isupper():
            upper_check = True
        if char.islower():
            lower_check = True
        if char.isdigit():
            digit_check = True
        if not char.isalnum():
            special_character_check = True
    
    if upper_check and lower_check and digit_check and special_character_check:
        return True
    else:
        print(Fore.RED + "Password not valid" + Style.RESET_ALL)
        return False

def user_validation(name, age, email, number, password):
    return (name_check(name) and 
            number_check(number) and 
            age_check(age) and 
            email_check(email) and
            password_check(password))
