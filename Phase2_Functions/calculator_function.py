#May 18 21:06 Calculator using funciton

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

while True:
    print("""
            1.Add
            2.Substract
            3.Multiply
            4.Divide
            5.Exit
""")
    choice= input("Please enter your choice: ").strip()

    if choice=="1":
        num1=int(input("Please enter the first number: "))
        num2=int(input("please enter the second number: "))
        result= add(num1,num2)
        print(f"Value of addition: {result}")
    elif choice=="2":
        num1=int(input("Please enter the first number: "))
        num2=int(input("please enter the second number: "))
        result= subtraction(num1,num2)
        print(f"Value of subtraction: {result}")
    elif choice=="3":
        num1=int(input("Please enter the first number: "))
        num2=int(input("please enter the second number: "))
        result= multiply(num1,num2)
        print(f"Value of multiplication: {result}")
    elif choice=="4":
        num1=int(input("Please enter the first number: "))
        num2=int(input("please enter the second number: "))
        result= divide(num1,num2)
        print(f"Value of division: {result}")
    elif choice=="5":
        print("Exiting calculator. . .")
        break
    else:
        print("Invalid choice!")
    