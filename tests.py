import datetime
from unittest.mock import patch
from app import Account




def test_withdraw_money_from_account():
    account = Account(100)
    account.withdraw(100)
    assert account.account == 0

def test_depisit_money_return_sum_depisit_and_money_in_acount():
    account = Account(100)
    account.deposit(100)
    assert account.account == 200

@patch("app.datetime")
def test_get_current_date(mock_date):
    mock_date.date.today.return_value = datetime.date(2022, 1, 13)
    inst = Account(100)
    assert inst.get_string_current_date() == "13-01-2022"


