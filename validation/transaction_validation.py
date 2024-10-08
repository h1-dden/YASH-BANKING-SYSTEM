"""
Checks is transactions are possible or not -->
    max and min transaction amount checks
    user balance amount checks

"""
from models import database

def validate_account(reciever_account):
    """
    Checks if bank account is present in bank_account_details.

    Parameters - receiver_account(int)

    Returns - bool: True if the bank account exists, False otherwise.
    """
    if reciever_account in database.bank_account_details:
        return True
    else:
        return False

def max_transaction(transaction_amount):
    if transaction_amount>100000:
        print("Max transaction amount is 1,00,000 at a time")
        return False
    if transaction_amount<10:
        print("Minimum transaction amount is 10 rupees")
        return False
    return True

def transfer_validation(account_number,transfer_amount):
    user_balance = database.bank_account_details[account_number]["balance"]

    if user_balance < transfer_amount:
        print("Insufficient Funds")
        return False
    
    if not max_transaction(transfer_amount):
        return False
    
    return True
    
