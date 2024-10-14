"""
Banking Transaction functions --> Deposit ,Withdraw ,Transfer and Check_Balance
"""
from models import database
from validation import transaction_validation
from services import account_service
from view import update_transaction_csv
from decorators import user_auth
from view import login
import datetime

class BankOperations:
    def __init__(self,account_number):
        self.account_number = account_number

    def account_update(self):
            #Insert updated bank_details into CSV file
            update_transaction_csv.transaction_logs(self.account_number)
            #Display balance after deposit
            account_service.check_balance(self.account_number)

    @user_auth.login_status_check
    def deposit_money(self):
        """
        Deposits specific amount into user account.

        Paramters - self.account_number(int)

        Return - None
        """
        deposit_amount = int(input("Please enter the amount to deposit \n"))

        if transaction_validation.max_transaction(deposit_amount):

            database.bank_account_details[self.account_number]["balance"] += deposit_amount
            database.bank_account_details[self.account_number]["last_transacted_date"] = str(datetime.datetime.now())
            database.bank_account_details[self.account_number]["last_transaction"] = f"+{deposit_amount}"
            self.account_update(self.account_number)
            print("Deposit Successful")

        else:
            raise Exception("Transaction amount out of bounds")

    @user_auth.login_status_check
    def withdraw_money(self):
        """
        Withdraws specific amount from user account.

        Paramters - account_number(int)

        Return - None
        """
        withdraw_amount = int(input("Please enter the amount to withdraw\n"))
        user_balance = database.bank_account_details[self.account_number]["balance"]

        if transaction_validation.transfer_validation(self.account_number,withdraw_amount):

            database.bank_account_details[self.account_number]["balance"] -= withdraw_amount
            database.bank_account_details[self.account_number]["last_transacted_date"] = str(datetime.datetime.now())
            database.bank_account_details[self.account_number]["last_transaction"] = f"-{withdraw_amount}"
            self.account_update(self.account_number)
            print("Withdraw Successful")
        else:
            print("Transaction Cancelled")

    @user_auth.login_status_check
    def transfer_money(self):
        reciever_account=int(input("Please Enter the reciever's account\n"))

        if transaction_validation.validate_account(reciever_account):
            transfer_amount=int(input("Please enter the amount of money to transfer\n"))

            if transaction_validation.transfer_validation(self.account_number,transfer_amount):
                database.bank_account_details[reciever_account]["balance"] += transfer_amount
                database.bank_account_details[reciever_account]["last_transacted_date"] = str(datetime.datetime.now())
                database.bank_account_details[reciever_account]["last_transaction"] = f"+{transfer_amount}"
                update_transaction_csv.transaction_logs(reciever_account)

                database.bank_account_details[self.account_number]["balance"] -= transfer_amount
                database.bank_account_details[self.account_number]["last_transacted_date"] = str(datetime.datetime.now())
                database.bank_account_details[self.account_number]["last_transaction"] = f"-{transfer_amount}"
                self.account_update(self.account_number)

            else:
                print("Transaction Cancelled")
        else:
            print("Reciever Account not valid.")

