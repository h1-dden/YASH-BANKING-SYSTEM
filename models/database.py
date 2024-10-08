
"""
Contains the database for managing transactions and user data.
user_details - Stores user data with key as account_number.
bank_account_details - Stores banking transaction data with key as account_number.
"""
#stores only the user information
user_details = {
    100000: {'name': 'harsh', 'age': 34, 'email': 'yash@gmail.com', 'number': 5656565656 },
    100001: {'name': 'harrsh', 'age': 34, 'email': 'yash@gmail.com', 'number': 5656565446 }
    }

#stores all account related information
bank_account_details ={
    100000: {'balance': 0, 'last_transaction': 0, 'last_transacted_date': 0, 'password': 'har'},
    100001: {'balance': 0, 'last_transaction': 0, 'last_transacted_date': 0, 'password': 'var'} 
    }
   