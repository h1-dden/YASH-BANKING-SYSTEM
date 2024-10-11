def name_check(name):
    if not name.isalpha() or len(name) >= 100:
        print("Name not valid")
        return False
    return True

def age_check(age):
    if age < 18 or age >= 100:
        print("Age not valid")
        return False
    return True

def email_check(email):
    if len(email) <= 5 or "@" not in email or not email.endswith(".com"):
        print("Email not valid")
        return False
    return True

def number_check(number):
    if len(number)>10 or not number.isnumeric():
        print("Number not valid")
        return False
    return True

def password_check(password):
    if len(password)<12:
        print("Password not valid")
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
            special_character_check= True
    
    if upper_check and lower_check and digit_check and special_character_check:
        return True
    else:
        print("Password not valid")
        return False

def user_validation(name,age,email,number,password):
    return (name_check(name) and 
            number_check(number) and 
            age_check(age) and 
            email_check(email) and
            password_check(password))
