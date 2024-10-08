from controllers import bank_routing


def main():
    print("---Welcome to Online Banking System---")
    print("Please Sign Up or Log In to avail services")
    while(bank_routing.user_logon_routing()):
        bank_routing.user_logon_routing()

main()
