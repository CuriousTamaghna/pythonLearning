#May 19 Expense Tracker using function 18:16

expenses = []

def add_expenses(expenses):
    category= input("Enter the category name: ").strip()
    amount = float(input("Enter the amount: "))

    expense = {"name":category,"amount":amount}

    expenses.append(expense)

def view_expense(expenses):
    print("All expenses:-\n")
    for i,expense in enumerate(expenses,start=1):
        print(f"{i}.{expense['name']} : {expense['amount']}")

def total_expense(expenses):
    if not expenses:
        print("No expense available!")
    else:
        total = 0

        for expense in expenses:
            total +=expense['amount']

        print(f"Total Expense = {total}/-")
def delete_expense(expenses):
    if not expenses:
        print("No expenses available!")
    else:
        print("\nExpenses List: ")
        for i,expense in enumerate(expenses,start=1):
            print(f"{i}.{expense['name']} - {expense['amount']}")
        try:
            index = int(input("Enter expense number to delete: "))
            if 1<=index<=len(expenses):
                removed_expense=expenses.pop(index-1)
                print(f"{removed_expense['name']} is removed")
            else:
                print("Please choose a valid number!")
        except ValueError:
            print("Please choose a valid option!")

#Main Program
while True:
    print("""
            1.Add Expense
            2.View Expense
            3.view Total Expense
            4.Delete Expense
            5.Exit
""")   
    
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_expenses(expenses)

    elif choice == "2":
        view_expense(expenses)
    elif choice == "3":
        total_expense(expenses)
    elif choice =="4":
        delete_expense(expenses)
    elif choice == "5":
        print("Exiting Expense Tracker App. . .")
        break
    else:
        print("Invalid choice!")
