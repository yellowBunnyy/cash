from dataclasses import dataclass
import datetime
import dataclasses

@dataclass
class TransactionsStatment:
    transaction_id: int
    balance: str
    amount: str
    date: str


class Account:
    def __init__(self, statting_account_state):
        self.account = statting_account_state
        self.transactions = {}
        self.transactions_id = 0

    def withdraw(self, withdraw_money: int) -> None:
        self.account -= withdraw_money
        self.transactions_id += 1
        transaction = TransactionsStatment(self.transactions_id, self.account, withdraw_money, self.get_string_current_date())
        self.transactions.update(transaction)


    def deposit(self, money: int) -> None:
        self.account += money

    def get_string_current_date(self):
        return datetime.date.today().strftime("%d-%m-%Y")

    def printStatment(self) -> None:
        pass

