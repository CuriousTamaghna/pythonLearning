#May 20 13:32 Number Guessing Game
import random

def number_game():
    num = random.randint(1, 15)
    while True:
        try:
            guessed_num = int(input("Enter your guess between 1 to 15: "))
            if num < guessed_num :
                print("The number is smaller!")
            elif num> guessed_num:
                print("The number is bigger!")
            else:
                print("You guessed it!")
                break
        except ValueError:
            print("Please enter a valid number")        

while True:
    print("1.Start Game" \
    "\n2.Exit")
    choice = input("Please enter your chocie ").strip()

    if choice == "1":
        number_game()
    elif choice == "2":
        print("Exiting. . . .")
        break
    else:
        print("Invalid choice!")