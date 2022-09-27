import datetime
import pdb

class Account:
    def __init__(self, statting_account_state):
        self.account = statting_account_state

    def withdraw(self, money: int) -> None:
        self.account -= money

    def deposit(self, money: int) -> None:
        self.account += money
    
    def get_string_current_date(self):
        return datetime.date.today()

    def printStatment(self) -> None:
        pass

