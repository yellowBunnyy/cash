class Account:
    def __init__(self, statting_account_state):
        self.account = statting_account_state
    def withdraw(self, money: int)->None:
        self.account -=  money
        
    def printStatment(self)-> None:
        pass
    def deposit(self, money: int)->None:
        pass

