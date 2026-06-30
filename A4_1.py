class BankAccount:
    def __init__(self,acc_no,name,balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
    def deposit(self,balance):
        self.balance+=balance
        print(self.name,"your balance is ", self.balance)


    def withdraw(self,balance):
        self.balance-=balance
        print(self.name,"your balance is ", self.balance)
    
    def get_balance(self):
        print(self.name,"your balance is ", self.balance)
 
cus1 = BankAccount(23244,"Anonymous",7000)
cus1.get_balance()
cus1.deposit(5483)
cus1.withdraw(7900)
cus1.deposit(7000)
cus1.withdraw(1583)