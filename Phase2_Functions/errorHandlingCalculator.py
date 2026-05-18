#May 18 21:34 Advanced calculator that handles errors and saves history

def add(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0 :
        return "Cannot divide by zero!"
    return a/b

#using thhe operations from dictionary
operations ={
    "1":("Addition",add),
    "2":("Subtraction",subtraction),
    "3":("Multiply",multiply),
    "4":("Divide",divide)
}

#list for saving history
history_file="Phase2_Functions/calculator_history.txt"

while True:
    print("""
========= CALCULATOR =========

1. Add
2. Subtract
3. Multiply
4. Divide
5. Show History
6. Exit

==============================
""")

    choice= input("Enter your choice: ").strip()

    #Exit function
    if choice=="6":
        print("Exiting calculator. . .")
        break
    #Show History 
    elif choice=="5":
        """if not history:
            print("No history to print!")
        else:
            print("====HISTORIES====")
            for hist in history:
                print(hist)
            print("=================")"""
        try:
            with open(history_file,"r") as file:
                content=file.read()
                if content :
                    print("\n=====Calculator History=====")
                    print(content)
                else:
                    print("No history available!")
        except FileNotFoundError:
            print("No history file found yet. . .")
    elif choice in operations:
        try:
            num1=int(input("Please enter the first number: "))
            num2=int(input("please enter the second number: "))

            operation_name, operation_function =operations[choice]

            result = operation_function(num1,num2)

            print(f"{operation_name} Result: {result}")

            #save history

            """history.append(f"{num1} {operation_name} {num2} = {result}")"""
            with open(history_file, "a") as file:
                file.write(f"{num1} {operation_name} {num2} = {result}\n")
        except ValueError:
            print("Invalid input! Please enter numbers only.")
        except Exception as e:
            print(f"An error occured: {e}")
    else:
        print("Invalid choice! Please select a valid option.")