from view import login,sign_up,banking_transactions
from constants import const
from services import account_service
from models import database
from decorators import user_auth

account_number = 0

class BankController:
    #turn the controller into 2 def functions object that is called in main

    def user_logon_routing(self):
        """
        Allows the user to login/signup or exit based on given choice.
        """
        while(True):
            self.user_login_choice = int(input("Please enter 0 to sign up ,1 to log On ,3 for banking or 5 to exit \n"))
            global account_number 
            match(self.user_login_choice):

                case const.SIGNUP:
                    account_number = sign_up.user_signup()
                    #Send to sign up page and return account number if sucessful else None
                    if account_number != None:
                        print(f"Sign Up completed.Your account with number {account_number} has been created")
                        print("Please Login to continue")
                        """"account_number = login.login_form()
                        if account_number != None:
                            self.banking_menu(account_number) #send to menu if successful creation"""
                        continue
                    else: #account number is none
                        print("SignUp Unsuccessful")

                case const.LOGON:
                    account_number = login.login_form()
                    if account_number != None:
                        self.banking_menu(account_number)

                case const.BANKING:
                    try:
                        self.banking_menu(account_number) 
                    except Exception:
                        print("Please Login to continue")

                case const.EXIT:
                    print("Thank You for using our online banking services.")
                    break

                case _:
                    print("Wrong Input Given")

    @user_auth.login_status_check
    def banking_menu(self,account_number):
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
                    banking = banking_transactions.BankOperations(account_number)
                    banking.deposit_money()

                case const.WITHDRAW : 
                    banking = banking_transactions.BankOperations(account_number)
                    banking.withdraw_money()

                case const.CHECK_BALANCE : 
                    account_service.check_balance(account_number)

                case const.TRANSFER : 
                    banking = banking_transactions.BankOperations(account_number)
                    banking.transfer_money()

                case const.EXIT :
                    print("Signing Out from Account")
                    login.login_status = False
                    break
                
                case _ : 
                    print("Wrong input given")
