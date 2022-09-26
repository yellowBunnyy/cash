from app import Account
def test_withdraw_money_from_account():
    account = Account(100)
    account.withdraw(100)
    assert account.account == 0

def test_depisit_money_return_sum_depisit_and_money_in_acount():
    account = Account(100)
    account.deposit(100)
    assert account.account == 200
