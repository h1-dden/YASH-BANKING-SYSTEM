from controllers import bank_routing


def main():
    print("---Welcome to Online Banking System---")
    print("Please Sign Up or Log In to avail services")
    while(True):
        bank_routing.user_logon_routing()

main()
