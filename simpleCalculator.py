#May 1 16:16 simple calculator

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

operator = input("Enter the operation you want to perform: ").strip() #strip function removes the space before or after

if operator == "+":
    print(f"{num1}+{num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1}-{num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1}*{num2} = {num1 * num2}")
elif operator == "/":
    if num2 == 0:
        print("Cannot be divided by zero")
    else:     
        print(f"{num1}/{num2} = {num1 / num2}")
else:
    print(f"The {operator} operation is invalid")            

