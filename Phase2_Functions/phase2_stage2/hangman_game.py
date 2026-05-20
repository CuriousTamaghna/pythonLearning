#May 20 14:53 Hangman Game

import random

def hangman_game():
    words=['python','coding','apple']
    secret_word = random.choice(words)
    display=[]

    for letters in secret_word:
       display.append("_")
    
    attempts = 6

    print("\nWelcome to Hangman!")
    player_input= input("Enter your guess: ").strip().lower()

    while attempts>0:
        print("\nWord: "," ".join(display))

        print(f"Attempts Left: {attempts}")

        guess= input("Guess a letter: ").lower().strip()
        found =False
        for i in range(len(secret_word)):
            if guess == secret_word[i]:
                display[i] = guess
                found = True
        if not found:
            attempts -=1
            print["Wrong guess!"]
        else:
            print("Correct guess!")
        #win check
        if "_" not in display:
            print("\nYou guessed the word!")
            print(f"Word was: {secret_word}")
            break
    if "_" in display:
        print("\nGame Over!")
        print(f"The word was: {secret_word}")
        

while True:
    print("1.Start Game" \
    "\n2.Exit")
    choice = input("Please enter your chocie ").strip()

    if choice == "1":
        hangman_game()
    elif choice == "2":
           print("Exiting. . . .")
           break
    else:
        print("Invalid choice!")