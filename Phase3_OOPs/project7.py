#May 27 01:32 
#Encapsulation

class BankAccount:

    #Constructor
    def __init__(self,name,balance):
        self.name = name

        #Private attribute
        self.__balance = balance

    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
            print(f"{amount} deposited!")
        else:
            print("Invalid deposit amount!")

    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn")
        else:
            print("Insufficient balamce!")
    
    def get_balance(self):
        return self.__balance
    
account1 = BankAccount("Tamaghna", 2000)

account1.deposit(200)
account1.withdraw(300)
print()
print(account1.get_balance())