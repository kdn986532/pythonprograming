class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def Deposit(self,amount):
        self.balance = balance + amount

    def withdraw(self, amount):
        if self.balance <= amount:
            self.balance = balance - amount

        else:
            print("출금이 불가합니다.")

    def display(self):
        print("현재 잔액은  = ", self.balance)


account = BankAccount("홍길동", 10000)
account.display()
account.deposit(5000)
account.display()
account.withdraw(3000)
account.display()  