class User:

    def __init__(self,name):
        self.name = name
        self.amount = 0

    def make_withdrawal(self,amount):
        self.amount -= amount

    def make_deposit(self,amount):
        self.amount += amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()

hunter = User("Hunter")
allie = User("Allie")
violet = User("Violet")

hunter.make_deposit(200)
hunter.make_deposit(100)
hunter.make_deposit(200)
hunter.make_withdrawal(300)
hunter.display_user_balance()

allie.make_deposit(200)
allie.make_deposit(200)
allie.make_withdrawal(100)
allie.make_withdrawal(100)
allie.display_user_balance()

violet.make_deposit(1000)
violet.make_withdrawal(200)
violet.make_withdrawal(200)
violet.make_withdrawal(200)
violet.display_user_balance()

hunter.transfer_money(200, violet)