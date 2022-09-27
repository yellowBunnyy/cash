from dataclasses import dataclass
import datetime

@dataclass
class TransactionsStatment:
    balance: str
    amount: str
    date: str


class Account:
    def __init__(self, statting_account_state):
        self.account = statting_account_state
        self.transactions = {}
        self.transactions_id = 0

    def preserve_transaction_in_container(self, transaction:TransactionsStatment):
        self.transactions.update({self.transactions_id: transaction})


    def withdraw(self, withdraw_money: int) -> None:
        self.account -= withdraw_money
        self.transactions_id += 1
        transaction = TransactionsStatment(self.account, withdraw_money, self.get_string_current_date())
        self.preserve_transaction_in_container(transaction)


    def deposit(self, money: int) -> None:
        self.account += money
        self.transactions_id += 1

    def get_string_current_date(self):
        return datetime.date.today().strftime("%d-%m-%Y")

    def printStatment(self) -> None:
        pass

