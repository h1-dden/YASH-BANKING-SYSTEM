
from models import database

login_status = False

def account_validation(account,password,user_database):
    """
    Checks if account is present in database.

    Parameters -    account(int)
                    password(str)
                    user_database(dict)
    
    Return - bool
    """
    try:
        if user_database[account]["password"] == password:
            global login_status
            login_status = True
            return True
        return False
    
    except KeyError:
        print("Key error occoured")

def login_form():
    """
    Takes username and password to login to bank account.

    Parameters - None

    Return - user_account(int)
    """
    print("Please enter account number and pasword\n")

    try:
        user_account = int(input("ACCOUNT : "))
        user_password = input("PASSWORD : ")

        if account_validation(user_account,user_password,database.bank_account_details):
            print("Login Successful")
            return user_account
        else:
            raise Exception("Account not valid")
    
    except EOFError:
        print("User input not given")
    
    except ValueError or TypeError:
        print("Wrong input given")


