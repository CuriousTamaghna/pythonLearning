#May 8 1:20AM Expense Tracker App
#May 12 3:50 again sat to complete this project!

expenses = []

#1. Add Expense
#2. View Expenses
#3. View Total
#4. Exit

while True:

    print("\n1.Add Expenses" \
    "\n2.View Expenses" \
    "\n3.View Total" \
    "\n4.Delete Expense" \
    "\n5.Exit")

    choice = input("Enter your choice: ")
    if choice == "1" :
        category = input("Enter in which category you have spent: ")
        amount= float(input("Enter amount: "))

        expense = {
        "category": category,
        "amount": amount
        }
        expenses.append(expense)
    elif choice == "2":
        if not expenses:
            print("No expenses yet")
        else:
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}.{expense['category']} - {expense['amount']}/-")

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total Expense: {total}")
    elif choice == "4":
        if not expenses:
            print("No expenses to delete!")
        else:
            print("\nChoose expense to delete:")

            for i , expense in enumerate(expenses, start=1):
                print(f"{i}. {expense['category']}- {expense['amount']}")

            try:
                index= int(input("Enter expense number to delete: "))

                if 1<= index <= len(expenses):

                    removed_expense = expenses.pop(index - 1)

                    print(f"Deleted: {removed_expense['category']} - {removed_expense['amount']}")

                else:
                    print("Please enter a valid number!")
            except ValueError:
                print("Please enter a valid number!")
    elif choice == "5":
        print ("Exiting Expense Tracker. . .")
        break

    else:
        print("Invalid choice!")