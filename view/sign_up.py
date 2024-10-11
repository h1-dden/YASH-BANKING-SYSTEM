
from validation import user_input_validation
from view import database_insertion

def take_input():
    """
    Take user input to sign in and create account.

    Parameters - None

    Return - account_number(int)
    """

    user_name = input("Please enter your full name :")
    user_email = input("Please enter your email_id :")
    user_number = int(input("Please enter your phone number :"))
    user_age = int(input("Please enter your age :"))
    user_password = input("Please enter a valid password :")

    #validate user detils
    if user_password == input("Re-enter your password :"):
        validation = user_input_validation.user_validation(user_name,user_age,
                                               user_email,user_number,
                                               user_password)
        #validation successful then insert into database
        if validation == True:
            account_number = database_insertion.create_user_id(user_name,user_age,
                                                               user_email,user_number,
                                                               user_password)
            return account_number
    else:
        raise Exception("Password match error")


def user_signup():
    """
    Creates new user account.

    Parameters - None

    Return - account_number(int)
    """

    print("Enter the following details to create a new account")
    account_number = take_input()
    return account_number


     

