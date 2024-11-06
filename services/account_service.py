from models import database
from decorators import user_auth

@user_auth.login_status_check
def check_balance(account_number):

    """
    Service to check account balance.
    Parameters - account_number(int)
    Return - No return value
    """
    
    query = "SELECT balance FROM bank_details WHERE account_number = %s"
    database.cursor.execute(query,(account_number))
    result = database.cursor.fetchone()
    
    return result[0]
