import os
import datetime
from controllers import bank_controller
from services import account_generator
from models import database

class UserDetails:
    #constructor to create new user
    def __init__(self,name,age,email,number,password):
            
        self.name = name
        self.age = age
        self.email = email
        self.number = number
        self.password = password


    def create_user_id(self):

        """
        Creates a unique user ID for a new user if the user does not already exist in the database
        Returns:
            str or None: The account number of the newly created user or None if the user already exists.
        """
        
        #query the database for existence of user
        user_data =[self.name,self.age,self.email,self.number]
        query = "SELECT account_number FROM user_details WHERE name=%s AND age=%s AND email=%s AND number=%s"
        database.cursor.execute(query, user_data)
        result = database.cursor.fetchone()

        if result:
            print(f"User already exists with account number {result[0]}")
            return None
        else:
            #create new user_id
            account_number = account_generator.generate_account_number()
            query = "INSERT INTO user_details (account_number, name, age, email, number) VALUES (%s, %s, %s, %s, %s)"
            database.cursor.execute(query,(account_number,self.name,self.age,self.email,self.number))
            database.con.commit()

            #create new bank_account_details
            query = "INSERT INTO bank_details (account_number, balance, last_transaction, last_transacted_date, password) VALUES (%s, 0.0, NULL, NULL, %s)"
            database.cursor.execute(query,(account_number,self.password))
            database.con.commit()

            return account_number
        