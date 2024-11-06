from validation import user_input_validation
from view import user_account_creation
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def user_signup():

    """
    Creates new user account.
    Parameters - None
    Return - account_number(int)
    """
    
    print(Fore.YELLOW + "Enter the following details to create a new account")

    user_name = input(Fore.BLUE + "Please enter your full name: ")
    user_email = input(Fore.BLUE + "Please enter your email_id: ")
    user_number = input(Fore.BLUE + "Please enter your phone number: ")
    user_age = int(input(Fore.BLUE + "Please enter your age: "))
    user_password = input(Fore.BLUE + "Please enter a valid password: ")

    # Validate user details
    if user_password == input(Fore.BLUE + "Re-enter your password: "):
        validation = user_input_validation.user_validation(user_name, user_age,
                                                           user_email, user_number,
                                                           user_password)
        # Validation successful then insert into database
        if validation:
            user_details = user_account_creation.UserDetails(user_name, user_age,
                                                             user_email, user_number,
                                                             user_password)
            print(Fore.GREEN + "Account created successfully!")
            return user_details.create_user_id()
    else:
        print(Fore.RED + "Password match error. Please try again.")
        raise Exception("Password match error")