class Bank_Account():

    def __init__(self,name,balance):

        self.name = name

        self.balance = balance

    def add_amount(self,amount):

        self.balance += amount

    def show_balance(self):

        print(self.balance)

obj = Bank_Account("Athul",1000)

obj.add_amount(500)

obj.show_balance()


        