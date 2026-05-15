#May 15 13:12 Banking System App

accounts =[]

while True:
    print("""
          1.Create Account
          2.View Account
          3.Deposite Money
          4.Withdraw Money
          5.Transfer Money
          6.Delete Account
          7.Exit  
""")
    choice = input("Enter the operation you want to perform: ").strip()

    if choice == "1":
        account_name = input("Please enter the name of the account holder: ").strip()
        account_balance = int(input("Enter the amount you want to open your bank account with: "))

        account = {"name":account_name, "balance":account_balance}
        accounts.append(account)
        print("Account created successfully!")
    elif choice == "2":
        if not accounts:
            print("No account to display!")
        else:
            print("Accounts Loading. . .")
            for i,account in enumerate(accounts,start=1):
                print(f"{i}.{account['name']} : {account['balance']:.2f}")
    elif choice=="3":
        if not accounts:
            print("No account to show!")
        else:
            name=input("Please enter the account holder's name: ").strip()
            found = False
            for account in accounts:
                if name==account['name']:
                    print("Account Found!")
                    amount = float(input("Please enter the amount to deposit: "))
                    account['balance']+=amount
                    print(f"{amount} deposited successfully!")
                    print(f"New balance: {account['balance']:.2f}")
                    found =True
                    break
            if not found:
                print("Account not found!")
    elif choice=="4":
        if not accounts:
            print("No account to show!")
        else:
            name=input("Please enter the account holder's name: ").strip()
            found = False
            for account in accounts:
                if name==account['name']:
                    print("Account Found!")
                    amount = float(input("Please enter the amount to withdraw: "))
                    account['balance']-=amount
                    print(f"{amount} withdraw successful!")
                    print(f"Remaining balance: {account['balance']:.2f}")
                    found =True
                    break
            if not found:
                print("Account not found!")
    elif choice == "5":
        if len(accounts)<2:
            print("At least two accounts required to transfer money!")
        else:
            sender_name=input("Enter the sender's name: ").strip()
            receiver_name=input("Enter the receiver's name: ").strip()

            sender=None
            receiver=None
            for account in accounts:
                if sender_name == account['name']:
                    sender=account
                if receiver_name==account['name']:
                    receiver=account
            if sender and receiver:
                amount=float(input("Please enter the amount to transfer: "))
                if amount<= sender['balance']:
                    sender['balance']-=amount
                    receiver['balance']+=amount
                    print("Transfer Successful!")
                    print(f"{sender['name']} balance : {sender['balance']:.2f}")
                    print(f"{receiver['name']} balance : {receiver['balance']:.2f}")
                else:
                    print("Insufficient balance!")
            else:
                print("Sender or Receiver's account not found")
    elif choice == "6":
        if not accounts:
            print("No accounts available")
        else:
            print("\nAccount List:")

            for i,account in enumerate(accounts,start=1):
                print(f"{i}.{account['name']}")
            try:
                index=int(input("Please enter the account by it's serial number: "))

                if 1<=index<=len(accounts):
                    removed_account = accounts.pop(index-1)

                    print(f"Deleted Account of {removed_account['name']}")   
                else:
                    print("Invalid account serial number!")
            except ValueError:
                print("Please enter a valid number!")
    elif choice=="7":
        print("Exiting banking system. . . .")
        break
    else:
        print("Invalid choice!")
