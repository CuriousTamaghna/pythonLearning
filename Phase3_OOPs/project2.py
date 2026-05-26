#May 26 20:23 
#Banking System using classes

class BankAccount:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance


    def deposit(self,amount):
        self.balance += amount
        print(f"Amount deposited successfully!")
        
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Amount withdrawn successfully!")
        else:
            print("Insuficient balance!")

    def display_balance(self):
        print(f"{self.name}'s balance!")
        print(f"{self.balance}")

account1 = BankAccount("Rahul", 100)
account2 = BankAccount("Tamaghna", 400)

account1.display_balance()
account1.deposit(2000)
account1.withdraw(1000)
account1.display_balance()
print()
account2.display_balance()