#May 26 13:36 JSON Based Banking App

import json

def load_accounts():
    try:
        with open("Phase2_Functions/phase2_stage2/json_projects/bank.json", "r") as file:
            accounts = json.load(file)
            return accounts
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return[]
    
def save_account(accounts):
    with open("Phase2_Functions/phase2_stage2/json_projects/bank.json", "w") as file:
        json.dump(accounts,file,indent=4) #mistake 1

def create_account(accounts):
    name = input("Enter the name of the acount holder: ").strip()

    balance = int(input("Enter deposit amount: "))

    account_number = input("Enter account number: ").strip()

    for account in accounts:
        if account['account_number'] == account_number:
            print("Account number already exits!")
            return
    
    new_account = {
        "name": name,
        "balance":balance,
        "account_number":account_number
    }

    accounts.append(new_account)
    save_account(accounts)

    print("Account created successfully!")

def view_accounts(accounts):
    if not accounts:
        print("No accounts found!")
    else:
        print("\nAccount List:-")
        
        for i,account in enumerate(accounts, start=1):
            print(f"{account['name']} : {account['account_number']}")
            print(f"Account balance: {account['balance']}")

def deposit_money(accounts):
    if not accounts:
        print("No account available!")
    else:
        account_number = input("Enter the account number: ").strip()
        amount = int(input("Enter deposit amount: "))

        found = False
        
        for account in accounts:
            if account['account_number'] == account_number:
                account['balance'] += amount
                save_account(accounts)
                print("Money deposit successfull!")
                found = True
                break
        if not found:
            print("The account is not found!")

def withdraw_money(accounts):
    if not accounts:
        print("No account availble!")
    else:
        account_number = input("Enter the account number: ").strip()
        amount = int(input("Enter amount to withdraw: "))


        found = False
        
        for account in accounts:
            if account['account_number'] == account_number:
                if account['balance']>=amount:
                    account['balance'] -= amount
                    save_account(accounts)
                    print("Money withdrawn successfully!")
                else:
                    print("Insufficient balance!")
                found = True
                break
        if not found:
            print("The account is not found!")

def check_balance(accounts):
    if not accounts:
        print("No account available!")
    else:
        account_number = input("Enter the account number: ").strip()

        found = False
        
        for account in accounts:
            if account['account_number'] == account_number:
                print(f"Account balance is : {account['balance']}")
                found = True
                break
        if not found:
            print("The account is not found!")

def delete_account(accounts):
    if not accounts:
        print("No account available!")
    else:
        account_number = input("Enter the account number: ").strip()

        found = False
        
        for account in accounts:
            if account['account_number'] == account_number:

                accounts.remove(account)
                save_account(accounts)
                print("Money deposit successfull!")
                found = True
                break
        if not found:
            print("The account is not found!")


accounts = load_accounts()

while True:

    print("""
1. Create Account
2. View Accounts
3. Deposit Money
4. Withdraw Money
5. Check Balance
6. Delete Account
7. Exit
""")

    choice = input(
        "Enter your choice: "
    ).strip()

    # 🟢 Create
    if choice == "1":

        create_account(accounts)

    # 🔵 View
    elif choice == "2":

        view_accounts(accounts)

    # 🟡 Deposit
    elif choice == "3":

        deposit_money(accounts)

    # 🟣 Withdraw
    elif choice == "4":

        withdraw_money(accounts)

    # 🟤 Check Balance
    elif choice == "5":

        check_balance(accounts)

    # ❌ Delete
    elif choice == "6":

        delete_account(accounts)

    # 🔴 Exit
    elif choice == "7":

        print(
            "Exiting Banking System..."
        )

        break

    # ⚫ Invalid
    else:

        print("Invalid choice!")