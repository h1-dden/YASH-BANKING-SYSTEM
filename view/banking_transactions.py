import log
from models import database
from validation import transaction_validation
from services import account_service
from decorators import user_auth
from view import login
import datetime
from unittest.mock import patch
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class BankOperations:
    
    def __init__(self, account_number):

        self.account_number = account_number
        log.logging.info(f'Initialized BankOperations for account: {self.account_number}')
    

    def account_update(self, type, amount):

        """Updates transaction history when new transaction is performed"""

        query = "INSERT INTO transaction_history VALUES (%s, %s, %s, CURDATE())"
        database.cursor.execute(query, (self.account_number, type, amount))
        database.con.commit()
        log.logging.info(f'Updated transaction history: {type} of amount {amount} for account: {self.account_number}')


    @user_auth.login_status_check
    def deposit_money(self):
       
        """Deposits specific amount into user account."""

        deposit_amount = int(input(Fore.WHITE + Style.BRIGHT + "Please enter the amount to deposit \n"))
        type = "CREDIT"

        if transaction_validation.max_transaction(deposit_amount):
            # Update bank_details table
            update_query = "UPDATE bank_details SET balance = balance + %s , last_transaction = %s, last_transacted_date = CURDATE() WHERE account_number = %s"
            database.cursor.execute(update_query, (deposit_amount, deposit_amount, self.account_number))
            database.con.commit()

            log.logging.info(f'Deposit successful: {deposit_amount} into account: {self.account_number}')
            print(Fore.GREEN + Style.BRIGHT + "Deposit Successful")
            self.account_update(type, deposit_amount)
        else:
            log.logging.error(f'Deposit failed: Transaction amount out of bounds for account: {self.account_number}')
            raise Exception("Transaction amount out of bounds")


    @user_auth.login_status_check
    def withdraw_money(self):
        
        """Withdraws specific amount from user account."""

        withdraw_amount = int(input(Fore.WHITE + Style.BRIGHT + "Please enter the amount to withdraw\n"))
        type = "DEBIT"

        if transaction_validation.transfer_validation(self.account_number, withdraw_amount):
            update_query = "UPDATE bank_details SET balance = balance - %s , last_transaction = -%s, last_transacted_date = CURDATE() WHERE account_number = %s"
            database.cursor.execute(update_query, (withdraw_amount, withdraw_amount, self.account_number))
            database.con.commit()
            self.account_update(type, withdraw_amount)
            log.logging.info(f'Withdrawal successful: {withdraw_amount} from account: {self.account_number}')
            print(Fore.GREEN + Style.BRIGHT + "Withdraw Successful")
        else:
            log.logging.warning(f'Withdrawal cancelled: Insufficient funds or invalid amount for account: {self.account_number}')
            print(Fore.RED + Style.BRIGHT + "Transaction Cancelled" + Style.RESET_ALL)


    @user_auth.login_status_check
    def transfer_money(self):
        
        """Transfers funds from current to receiver account"""

        receiver_account = int(input(Fore.WHITE + Style.BRIGHT + "Please Enter the receiver's account\n"))

        if transaction_validation.validate_account(receiver_account):
            transfer_amount = int(input(Fore.WHITE + Style.BRIGHT + "Please enter the amount of money to transfer\n"))

            if transaction_validation.transfer_validation(self.account_number, transfer_amount):
                sender_type = "DEBIT"
                receiver_type = "CREDIT"
                
                # debit from sender account
                debit_query = "UPDATE bank_details SET balance = balance - %s , last_transaction = -%s, last_transacted_date = CURDATE() WHERE account_number = %s"
                database.cursor.execute(debit_query, (transfer_amount, transfer_amount, self.account_number))
                database.con.commit()
                self.account_update(sender_type, transfer_amount)
                
                # credit to receiver
                update_query = "UPDATE bank_details SET balance = balance + %s , last_transaction = %s, last_transacted_date = CURDATE() WHERE account_number = %s"
                database.cursor.execute(update_query, (transfer_amount, transfer_amount, receiver_account))
                database.con.commit()
                self.account_update(receiver_type, transfer_amount)
                
                log.logging.info(f'Transfer successful: {transfer_amount} from account: {self.account_number} to account: {receiver_account}')
                print(Fore.GREEN + Style.BRIGHT+"Transaction completed successfully")
            
            else:
                log.logging.warning(f'Transfer cancelled: Insufficient funds for account: {self.account_number}')
                print(Fore.RED + Style.BRIGHT + "Transaction Cancelled" + Style.RESET_ALL)
        else:
            log.logging.error(f'Transfer failed: Invalid receiver account: {receiver_account}')
            print(Fore.RED + Style.BRIGHT + "Receiver Account not valid." + Style.RESET_ALL)
