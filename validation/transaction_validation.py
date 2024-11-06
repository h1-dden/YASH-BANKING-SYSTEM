from models import database
from services import account_service
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def validate_account(reciever_account):

    """
    Checks if bank account is present in bank_account_details.
    Parameters - receiver_account(int)
    Returns - bool: True if the bank account exists, False otherwise.
    """
    query = "SELECT * FROM bank_details WHERE account_number = %s"
    database.cursor.execute(query, (reciever_account,))
    result = database.cursor.fetchone()
    if result:
        return True
    else:
        return False


def max_transaction(transaction_amount):
    
    """Check if transaction amount is out of range"""

    if transaction_amount > 100000:
        print(Fore.RED + "Max transaction amount is 1,00,000 at a time" + Style.RESET_ALL)
        return False
    if transaction_amount < 10:
        print(Fore.RED + "Minimum transaction amount is 10 rupees" + Style.RESET_ALL)
        return False
    return True


def transfer_validation(account_number, transfer_amount):

    """Validate user transaction is within bounds"""

    user_balance = account_service.check_balance(account_number)

    if user_balance < transfer_amount:
        print(Fore.RED + "Insufficient Funds" + Style.RESET_ALL)
        return False
    
    if not max_transaction(transfer_amount):
        return False
    
    print(Fore.GREEN + "Transaction is valid." + Style.RESET_ALL)
    return True