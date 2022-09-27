import datetime
from unittest.mock import patch
from app import Account, TransactionsStatment


def test_withdraw_money_from_account():
    account = Account(100)
    account.withdraw(100)
    assert account.account == 0
    assert account.transactions_id == 1

@patch("app.datetime")
def test_preserve_transaction_in_container(mocked_date):
    mocked_date.date.today.return_value = "12-01-2022"
    money_in_account = 200
    money_to_withdraw = 100
    transaction_id = 0
    acconut = Account(money_in_account)
    transaction = TransactionsStatment(100, money_to_withdraw, "12-01-2022")
    acconut.preserve_transaction_in_container(transaction)
    assert acconut.transactions == {transaction_id: transaction}


def test_depisit_money_return_sum_depisit_and_money_in_acount():
    account = Account(100)
    account.deposit(100)
    assert account.account == 200
    assert account.transactions_id == 1
    

@patch("app.datetime")
def test_get_current_date(mock_date):
    mock_date.date.today.return_value = datetime.date(2022, 1, 13)
    inst = Account(100)
    assert inst.get_string_current_date() == "13-01-2022"


