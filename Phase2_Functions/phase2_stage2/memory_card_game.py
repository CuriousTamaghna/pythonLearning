#May 22 14:36 Memory Card Game

import random 
import time
import subprocess

def memory_game():

    level = 1

    print("Welcome to Memory Game!")

    while True:
        numbers = []

        print(f"\n Level {level}")

        for i in range(level+2):
            random_number = random.randint(1,9)
            numbers.append(random_number)
        
        print("Remember this sequence: ")

        print(*numbers)

        time.sleep(3)

        subprocess.run("cls", shell = True)

        user_inp = input("Please enter the sequence separated by spaces: ")

        user_numbers = []

        split_numbers = user_inp.split()

        for num in split_numbers:
            user_numbers.append(int(num))
        
        if user_numbers == numbers:
            print("Correct Memory!")
            level +=1
        else:
            print("Wrong sequence!")
            print(f"Correct Sequence: {numbers}")
            print(f"You reached level: {level}")
            break


while True:
    print("1.Start Game" \
    "\n2.Exit")
    choice = input("Please enter your chocie ").strip()

    if choice == "1":
        memory_game()
    elif choice == "2":
           print("Exiting. . . .")
           break
    else:
        print("Invalid choice!") 