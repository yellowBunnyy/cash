from app import Account
def test_withdraw_money_from_account():
    account = Account(100)
    account.withdraw(100)
    assert account.account == 0