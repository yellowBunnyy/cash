from dataclasses import dataclass
import datetime


@dataclass
class TransactionsStatment:
    balance: int
    amount: int
    date: str


class Account:
    def __init__(self, statting_account_state):
        self.money_in_account = statting_account_state
        self.transactions = {}
        self.transactions_id = 0

    def preserve_transaction_in_container(self, transaction: TransactionsStatment):
        self.transactions.update({self.transactions_id: transaction})

    def withdraw(self, withdraw_money: int) -> None:
        self.money_in_account -= withdraw_money
        self.transactions_id += 1
        transaction = TransactionsStatment(
            self.money_in_account, withdraw_money, self.get_string_current_date()
        )
        self.preserve_transaction_in_container(transaction)

    def deposit(self, deposit_money: int) -> None:
        self.money_in_account += deposit_money
        self.transactions_id += 1
        transaction = TransactionsStatment(
            self.money_in_account, deposit_money, self.get_string_current_date()
        )
        self.preserve_transaction_in_container(transaction)

    def get_string_current_date(self) -> str:
        return datetime.date.today().strftime("%d-%m-%Y")

    def printStatment(self) -> str:
        statment = "Date          Amount      Balance\n"
        for _, transaction in self.transactions.items():
            transaction_row = (
                f"{transaction.date}\t{transaction.amount}\t{transaction.balance}\n"
            )
            statment += transaction_row
        return statment
