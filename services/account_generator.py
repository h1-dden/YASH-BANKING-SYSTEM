from models import database

def generate_account_number():
    
    """Service to generate account number"""

    query = "SELECT MAX(account_number) FROM user_details"
    database.cursor.execute(query)
    result = database.cursor.fetchone()

    if result:
        new_number = result[0]+1
    else:
        new_number = 100000
        
    return new_number
