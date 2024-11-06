import pytest
from unittest.mock import patch
from models import database
from validation import transaction_validation
from services import account_service
from view import update_transaction_csv
from decorators import user_auth
from view import login
import datetime
from view import banking_transactions

@pytest.fixture
def test_db_connection():
    # Create a temporary database connection for testing
    test_connection = database.DbService()
    yield test_connection
    database.con.close()
    database.cursor.close()

@pytest.fixture
def mock_input():
    with patch('builtins.input', return_value=500) as mocked_input:
        yield mocked_input
    
@pytest.fixture
def mock_account():
    with patch('builtins.input', return_value=100003) as mocked_account:
            yield mocked_account
 
def test_deposit_money(test_db_connection,mock_input):
    test_account = 100002
    bank_operations = banking_transactions.BankOperations(test_account)

    # Get initial balance
    initial_balance = account_service.check_balance(test_account)

    # Deposit money
    bank_operations.deposit_money()

    # Assert updated balance
    assert account_service.check_balance(test_account) == initial_balance + 500

    # Verify transaction history
    query = "SELECT * FROM transaction_history WHERE account_number = %s AND transaction_type = 'CREDIT'"
    database.cursor.execute(query, (test_account,))
    transaction_history = database.cursor.fetchall()
    assert transaction_history[0][0] == test_account
    assert transaction_history[0][1] == "CREDIT"
    assert transaction_history[0][2] == 500


def test_withdraw_money(test_db_connection, mock_input):
    test_account = 100002
    bank_operations = banking_transactions.BankOperations(test_account)
    withdraw_amount = 300

    # Get initial balance
    initial_balance = account_service.check_balance(test_account)

    # Withdraw money
    bank_operations.withdraw_money()

    assert mock_input.call_args[0] == ("Please enter the amount to withdraw\n",)

    # Assert updated balance
    assert account_service.check_balance(test_account) == initial_balance - 500

    # Verify transaction history
    query = "SELECT * FROM transaction_history WHERE account_number = %s AND transaction_type = 'DEBIT'"
    database.cursor.execute(query, (test_account,))
    transaction_history = database.cursor.fetchall()
    assert transaction_history[0][0] == test_account
    assert transaction_history[0][1] == 'DEBIT'
    assert transaction_history[0][2] == 500

