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

    def withdraw(self, money: int) -> None:
        self.account -= money


    def deposit(self, money: int) -> None:
        self.account += money

    def get_string_current_date(self):
        return datetime.date.today().strftime("%d-%m-%Y")

    def printStatment(self) -> None:
        pass

