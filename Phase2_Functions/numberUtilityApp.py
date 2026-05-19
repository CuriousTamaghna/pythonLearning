#May 18 23:47 Number Utility App

#a even number is when a number doesn't have any reaminder
def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
#a prime is number is which only divides by 1 & the number itself , 1 is not a prime number & when it is divided it should have remainder!
def is_prime(number):
    if number<=1:
        return False
    for i in range(2,number):
        number % i == 0
        return False
    return True
#A palindrome number is any number that reads exactly the same forwards and backwards. exp . 1331 | 1331 but 2331 | 1332 it's not!
def is_palindrome(number):
    original = str(number)
    reversed_number = original[::-1]
    if original == reversed_number:
        return True
    else:
        return False
#Factorial of a number
def factorial(number):
    result = 1
    for i in range(1,number+1):
        result = result*i
    return result
#Reversed number
def reversed_number(number):
    reversed_num = str(number)[::-1]
    return reversed_num

while True:
        print("""
            1. Even or Odd
            2. Prime Number Check
            3. Palindrome Check
            4. Factorial
            5. Reverse Number
            6. Exit
            """)
        
        choice =input("Enter your choice: ").strip()

        if choice=="1":
            number = int(input("Enter number: "))
            result = is_even(number)
            print(result)
        elif choice=="2":
            number = int(input("Enter number: "))
            result = is_prime(number)
            if result:
                print("Prime number!")
            else:
                print("Not a prime number!")
        elif choice=="3":
            number = int(input("Enter number: "))
            result = is_palindrome(number)
            if result:
                print("Palindrome!")
            else:
                print("Not a palindrome!")
        elif choice=="4":
            number = int(input("Enter number: "))
            result = factorial(number)
            print(f"The factorial of the {number} is: {result}")
        elif choice=="5":
            number = int(input("Enter number: "))
            result = reversed_number(number)
            print(f"The reversed number of {number} is: {result}")
        elif choice == "6":
            print("Exiting. . .")
            break
        else:
            print("Invalid choice!")