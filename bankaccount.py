from pprint import pprint
class BankAccount:
    all_acs = []
    def __init__(self, amount, name):
        self.balance = amount
        self.name = name
        self.intrest = 1.1
        BankAccount.all_acs.append(self)
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print('you aint got no money so im taking 5 bucks')
            self.balance -= 5
    def display_account_info(self):
        print(f'hi {self.name} you have {self.balance}$')
    def yield_intrest(self):
        if self.balance > 0:
            self.balance = self.balance * self.intrest
        else:
            print('sorry ur broke')
    @classmethod
    def printt(cls):
        new_arr = []
        x = 0
        while x < len(cls.all_acs):
            new_arr.append([cls.all_acs[x].name, f'Balance: {round(cls.all_acs[x].balance)}$'])
            x += 1
        pprint(new_arr)
alex = BankAccount(100, 'Alex')
greg = BankAccount(100, 'Greg')
# For some reason my code wont chain properly, it is giving me the error
#
# alex.deposit(20).deposit(20)
# AttributeError: 'NoneType' object has no attribute 'deposit'
#
# when chaining here are the original chains so for it to work on my pc
# so I did not do the chain but here is the orignal chain code
# alex.deposit(10).deposit(10).deposit(10).withdraw(5).yield_intrest().display_account_info()
# greg.deposit(10).deposit(10).withdrawl(1).withdrawl(1).withdrawl(1).withdrawl(1).yield_intrest().display_account_info()
# BankAccount.printt()
alex.deposit(10)
alex.deposit(10)
alex.deposit(10)
alex.withdraw(5)
alex.yield_intrest()
alex.display_account_info()
greg.deposit(10)
greg.deposit(10)
greg.withdraw(1)
greg.withdraw(1)
greg.withdraw(1)
greg.withdraw(1)
greg.yield_intrest()
greg.display_account_info()
BankAccount.printt()

