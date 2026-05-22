#May 22 19:25 JSON based expense tracker

import json

#Load expense from JSON file
def load_expenses():
    try:
        with open("Phase2_Functions/phase2_stage2/json_projects/expense.json", "r") as file:
            expenses = json.load(file)
            return expenses
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

#Save expenses into JSON file
def save_expenses(expenses):
    with open("Phase2_Functions/phase2_stage2/json_projects/expense.json") as file:
        json.dump(expenses,file,indent=4)

#Add expense
def add_expense(expenses):
    title = input("Enter expense title: ").strip()

    amount = float(input("Enter expense amount: "))

    expense = {
        "title":title,
        "amount":amount
    }
    expenses.append(expense)

    save_expenses(expenses)

    print("Expense saved successfully!")

#View expenses
def view_expenses(expenses):
    if not expenses:
        print("No expense found")
    else:
        print("\nExpense List\n")
        for i,expense in enumerate(expenses,start=1):
            print(f"{i}." 
                  f"{expense['title']}"
                  f"->{expense['amount']}/-"
                  )

#Total Expense
def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']
    print(f"\nTotal Expense = {total}/-")


expenses = load_expenses()

while True:
    print("\n1.Add Expense" \
    "\n2.View Expenses" \
    "\n3.Total Expenses" \
    "\n4.Exit")

    choice = input("Enter your choice: ").strip()

    #Add Expense
    if choice=="1":
        add_expense(expenses)
    
    #View Expenses
    elif choice == "2":
        view_expenses(expenses)

    #Total Expense
    elif choice == "3":
        total_expenses()

    #Exit
    elif choice == "4":
        print("Exiting. . . .")
        break
    else:
        print("Invalid choice!")