import os
import datetime
from controllers import bank_routing
from view import update_jsonfile
from services import account_generator
from models import database

class UserDetails:
    #constructor to create new user
    def __init__(self,name,age,email,number,password):
        self.new_user = {
            "name" : name,
            "age" : age,
            "email" : email,
            "number" : number
            }
        self.password = password
        
    #Create new bank account
    def create_bank_account(self):
        self.new_account = {
                "balance" : 0,
                "last_transaction" : 0,
                "last_transacted_date" : None,
                "password" : self.password
                }

    def create_user_id(self):
        #create user details object

        if self.new_user in database.user_details.values():
            print("User Already Exists")
            return None

        else:
            account_number = account_generator.generate_account_number()

            #insert into database from objects
            database.user_details[account_number] = self.new_user # password stored with bank details

            user_bank_account=self.create_bank_account() #initalize bank account
            database.bank_account_details[account_number]=self.new_account

            update_jsonfile.update_user_database(database.user_details) #update JSON file

            return account_number