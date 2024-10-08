import csv
import os
from constants import const
from models import database

def transaction_logs(account_number):
    """
    Stores transaction logs into CSV file.

    Parameters - account_number(int)

    Returns - None
    """
    csv_filename = const.CSV_PATH
    user_balance = database.bank_account_details[account_number]["balance"]
    user_last_transaction = database.bank_account_details[account_number]["last_transaction"]
    user_last_transacted_date = database.bank_account_details[account_number]["last_transacted_date"]

    try:
        with open(csv_filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([account_number,user_balance,user_last_transaction,user_last_transacted_date])

    except FileNotFoundError or FileExistsError:
        print("The file does not exist")

    except csv.Error:
        print("Error occoured with the csv file")