import os
import datetime
from controllers import bank_routing
from view import update_jsonfile
from models import database

def generate_account_number(user_details):
    ########### take from JSON file ###############
    if len(user_details)!=0:
        new_number = max(user_details)+1
    else:
        new_number =100002
    return new_number

def create_bank_account(account_number,password):
    new_account={
            "balance" : 0,
            "last_transaction" : 0,
            "last_transacted_date" : None,
            "password" : password
            }
    database.bank_account_details[account_number]=new_account

def create_user_id(name,age,email,number,password):

    new_user= {
        "name" : name,
        "age" : age,
        "email" : email,
        "number" : number
        }
    
    if new_user in database.user_details.values():
        print("User Already Exists")
        return None
    else:
        account_number = generate_account_number(database.user_details)
        database.user_details[account_number] = new_user # password stored with bank details
        create_bank_account(account_number,password)
        update_jsonfile.update_user_database(database.user_details) #update JSON file
        return account_number