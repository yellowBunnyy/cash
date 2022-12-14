import datetime
from unittest.mock import patch
import pytest

from app import Account, TransactionsStatment, NotEnoughMoney


def test_withdraw_money_from_account():
    account = Account(100)
    account.withdraw(100)
    assert account.money_in_account == 0
    assert account.transactions_id == 1


def test_fali_withdraw_money_if_we_have_not_enough_in_account_should_raise_exception():
    account = Account(100)
    with pytest.raises(NotEnoughMoney):
        account.withdraw(200)


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
    assert account.money_in_account == 200
    assert account.transactions_id == 1


@patch("app.datetime")
def test_get_current_date(mock_date):
    mock_date.date.today.return_value = datetime.date(2022, 1, 13)
    inst = Account(100)
    assert inst.get_string_current_date() == "13-01-2022"


def test_incrementation_id_after_making_fewe_transaction():
    account = Account(200)
    account.withdraw(100)
    account.deposit(100)
    assert account.transactions_id == 2


def test_printStatment_after_windraw_operation_should_return_string_with_operation_statment():
    account = Account(100)
    money_afret_operation = 500
    withdraw_money = 100
    date = "12-01-2022"
    withdtaw_transaction = TransactionsStatment(
        money_afret_operation, f"-{withdraw_money}", date
    )
    account.transactions = {1: withdtaw_transaction}
    expected = (
        f"Date          Amount      Balance\n{date}\t-100\t{money_afret_operation}\n"
    )
    assert account.printStatment() == expected


# integration tests


@patch("app.Account.get_string_current_date")
def test_preserve_transaction_in_container_after_few_operations(mocked_date):
    mocked_date.return_value = "12-01-2022"
    money_in_account = 200
    acconut = Account(money_in_account)
    acconut.withdraw(100)
    acconut.deposit(200)
    withdtaw_transaction = TransactionsStatment(100, "-100", "12-01-2022")
    deposit_transaction = TransactionsStatment(300, "+200", "12-01-2022")
    assert acconut.transactions == {1: withdtaw_transaction, 2: deposit_transaction}
    assert acconut.transactions_id == 2
    assert acconut.money_in_account == 300
