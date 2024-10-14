from models import database

def generate_account_number():
    ########### take from JSON file ###############
    if len(database.user_details)!=0:
        new_number = max(database.user_details)+1
    else:
        new_number = 100000
    return new_number
