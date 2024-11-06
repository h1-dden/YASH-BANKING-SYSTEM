from models import database
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

login_status = False

def account_validation(account, password):

    """
    Checks if account is present in database.
    Parameters -    account(int)
                    password(str)
    Return - bool
    """

    query = "SELECT * FROM bank_details WHERE account_number=%s AND password=%s"
    database.cursor.execute(query, (account, password))
    result = database.cursor.fetchone()
    if result:
        global login_status
        login_status = True
        return True
    return False

def login_form():

    """
    Takes username and password to login to bank account.
    Parameters - None
    Return - user_account(int)
    """
    
    print(Fore.YELLOW + "Please enter account number and password")

    try:
        user_account = int(input(Fore.CYAN + "ACCOUNT : "))
        user_password = input(Fore.CYAN + "PASSWORD : ")

        if account_validation(user_account, user_password):
            print(Fore.GREEN + "Login Successful")
            print("<-------------------------------------------------------->")
            return user_account
        else:
            print(Fore.RED + "Account not valid")
    
    except EOFError:
        print(Fore.RED + "User input not given")
    
