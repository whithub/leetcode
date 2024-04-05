class Bank:

    def __init__(self, balance: List[int]):
        self.account_balances = balance
        self.max_account_num = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.valid_acct(account1) and self.valid_acct(account2):
            if self.account_balances[account1-1] >= money:
                self.account_balances[account1-1] -= money
                self.account_balances[account2-1] += money
                return True
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        if self.valid_acct(account):
            self.account_balances[account-1] += money
            return True
        return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if self.valid_acct(account) and self.account_balances[account-1] >= money:
            self.account_balances[account-1] -= money
            return True
        return False

    def valid_acct(self, account: int):
        return account <= self.max_account_num
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)