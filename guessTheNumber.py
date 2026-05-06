#May 3 16:40 Number guessing game!

import random;

number = random.randint(1,10);

attempts=1; #for counting how many attempts

print("Guess a number between 1,10");

while True:

    guessedNum = int(input("Enter your guessed number: "))

    if guessedNum>number:
        print("Wrong guess!")
        print("Your guessing is too high")
        attempts +=1
    elif guessedNum<number:
        print("Wrong guess!")
        print("Your guessing is too low")
        attempts +=1
    else:
        print(f"You guessed it in {attempts} attempts!")
        break
