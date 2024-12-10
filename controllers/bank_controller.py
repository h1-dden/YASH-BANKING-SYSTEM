from view import login, sign_up, banking_transactions
from constants import const
from services import account_service
from decorators import user_auth
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

account_number = 0

class BankController:

    def user_logon_routing(self):

        """Allows the user to login/signup or exit based on given choice."""
        
        while(True):

            self.user_login_choice = int(input("Please enter 1 to sign up, 2 to log On, 3 for banking or 5 to exit \n"))
            global account_number 
            match(self.user_login_choice):

                case const.SIGNUP:
                    try:
                        account_number = sign_up.user_signup()
                    except Exception as e:
                        print(Fore.RED + str(e))
                    if account_number is not None:
                        print(Fore.BLUE + Style.BRIGHT + f"Sign Up completed. Your account with number {account_number} has been created")
                        print(Fore.BLUE + "Please Login to continue")
                        continue
                    else:  # account number is none
                        print(Fore.RED + "SignUp Unsuccessful")

                case const.LOGON:
                    try:
                        account_number = login.login_form()
                    except Exception as e:
                        print(Fore.RED + str(e))
                    if account_number is not None:
                        try:
                            self.banking_menu(account_number) 
                        except Exception as e:
                            print(Fore.RED + f"Error: {e}")

                case const.BANKING:
                    try:
                        self.banking_menu(account_number) 
                    except Exception as e:
                        print(Fore.RED + f"Error: {e}")

                case const.EXIT:
                    print(Fore.BLUE + Style.BRIGHT + "Thank You for using our online banking services.")
                    break

                case _:
                    print(Fore.RED + "Wrong Input Given")


    @user_auth.login_status_check
    def banking_menu(self, account_number):

        """
        Allows user to perform banking operations(deposit, withdraw, check_balance, transfer) based on user
        choice.
        Parameters - account_number(int)
        Returns - No return value
        """

        while(True):

            print(Fore.BLUE + Style.BRIGHT + "\nPlease choose one of the following actions to perform : ")
            print("1-Deposit")
            print("2-Withdraw")
            print("3-Check Balance")
            print("4-Transfer Money")
            print("5-Exit\n")

            user_choice = int(input())
            match(user_choice):

                case const.DEPOSIT: 
                    banking = banking_transactions.BankOperations(account_number)
                    try:
                        banking.deposit_money()
                    except Exception as e:
                        print(Fore.RED + str(e))

                case const.WITHDRAW: 
                    banking = banking_transactions.BankOperations(account_number)
                    try:
                        banking.withdraw_money()
                    except Exception as e:
                        print(Fore.RED + f"Error: {e}")

                case const.CHECK_BALANCE:
                    try:
                        print(Fore.BLUE + Style.BRIGHT + f"Your balance is: {account_service.check_balance(account_number)}")
                    except Exception as e:
                        print(Fore.RED + f"Error: {e}")
                    
                case const.TRANSFER: 
                    banking = banking_transactions.BankOperations(account_number)
                    try:
                        banking.transfer_money()
                    except Exception as e:
                        print(Fore.RED + f"Error: {e}")

                case const.EXIT:
                    print(Fore.YELLOW + "Signing Out from Account...")
                    login.login_status = False
                    break
                
                case _: 
                    print(Fore.RED + "Wrong input given")