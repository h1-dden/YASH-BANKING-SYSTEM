from view import login,sign_up,banking_transactions
from constants import const
from services import account_service
from models import database

def user_logon_routing():
    """
    Allows the user to login/signup or exit based on given choice.
    """
    user_login_choice = int(input("Please enter 0 to sign up ,1 to log On or 5 to exit \n"))
    match(user_login_choice):
        
        case const.SIGNUP:
            account_number = sign_up.user_signup() #Send to sign up page and return account number if sucessful else None
            if account_number != None:
                print(f"Sign Up completed.Your account with number {account_number} has been created")
                banking_menu(account_number) #send to menu if successful creation
            else: #account number is none
                print("SignUp Unsuccessful")
        
        case const.LOGON:
            account_number = login.login_form()
            if account_number != None:
                banking_menu(account_number)
        
        case const.EXIT:
            print("Thank You for using our online banking services.")
            return False

        case _:
            print("Wrong Input Given")

def banking_menu(account_number):
    """
    Allows user to perform banking operations(deposit,withdraw,check_balance,transfer) based on user
    choice.

    Parameters - account_number(int)

    Returns - No return value
    """

    print("Please choose one of the following actions to perform")
    
    while(True):
        user_choice = int(input("1-Deposit, 2-Withdraw, 3-Check Balance, 4-Transfer Money, 5-Exit \n"))
        
        match(user_choice):

            case const.DEPOSIT : 
                banking_transactions.deposit_money(account_number)

            case const.WITHDRAW : 
                banking_transactions.withdraw_money(account_number)

            case const.CHECK_BALANCE : 
                account_service.check_balance(account_number)

            case const.TRANSFER : 
                banking_transactions.transfer_money(account_number)

            case const.EXIT :
                print("Signing Out from Accout")
                break
            
            case _ : 
                print("Wrong input given")
