
from models import database
from decorators import user_auth

@user_auth.login_status_check
def check_balance(account_number):
    """
    Service to check account balance.

    Parameters - account_number(int)

    Return - No return value
    """
    
    print(f"Balance for Account Number {account_number} => ",database.bank_account_details[account_number]["balance"])
