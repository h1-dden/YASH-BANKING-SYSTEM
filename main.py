from controllers import bank_routing


def main():
    
    print("---Welcome to Online Banking System---")
    print("Please Sign Up or Log In to avail services \n")
    controller = bank_routing.BankController()
    controller.user_logon_routing()

main()
