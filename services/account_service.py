
from models import database

def check_balance(account_number):
    """
    Service to check account balance.

    Parameters - account_number(int)

    Return - No return value
    """
    
    print(f"Balance for Account Number {account_number} => ",database.bank_account_details[account_number]["balance"])
