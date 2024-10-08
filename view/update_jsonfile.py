import json
from constants import const
from os import path

def update_user_database(user_database):
    filename = const.JSON_PATH
    try:
        with open(filename,"r+") as jsonfile:
            existing_users = json.load(jsonfile)
        
        for account in user_database:
            if str(account) not in existing_users.keys():
                existing_users[account]=user_database[account]

        with open(filename, "w") as f:
            json.dump(existing_users, f, indent=4)
    
    except FileNotFoundError:
        print("The file does not exist")

    except KeyError:
        print("Key not found or duplicate key exists")
    
        
