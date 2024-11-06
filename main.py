from controllers import bank_controller
from models import database
from colorama import init,Fore,Style

def main():
    
    """
    Launches the Online Banking System and initiates database connection.
    """
    # Initialize colorama
    init(autoreset=True)

    print(Style.BRIGHT + Fore.BLUE + "---Welcome to Online Banking System---")
    print(Style.BRIGHT + Fore.YELLOW + "Please Sign Up or Log In to avail services \n")
    connector = database.DbService()
    controller = bank_controller.BankController()
    controller.user_logon_routing()
    connector.cleanup()

main()
