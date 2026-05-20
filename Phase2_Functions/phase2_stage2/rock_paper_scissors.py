#May 20 13:49 Rock paper scissor game 

"""
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
"""

import random

def rps_game():
    choices = ['rock','paper','scissor']
    player_score= 0
    computer_score = 0
    while True:
        print("1.Rock" \
        "\n2.Paper" \
        "\n3.Scissor" \
        "\n4.Exit Round")
        player_choice= input("Enter your choice: ").strip().lower()

        #Exit round
        if choice == "4":
             print("Exiting round. . .")
             break
        #Input validation
        if player_choice not in ['1','2','3']:
             print("Invalid choice!")
             continue
        
        #convert number to actual choice
        player= choices[int(player_choice)-1]

        #computer choice
        computer = random.choice(choices)

        print(f"\nYou chose: {player}")
        print(f"Computer chose: {computer}")

        #Draw
        if player == computer :
             print("it's a draw!")
             #player wins logic
        elif ((player == "rock" and computer =="scissors") 
              or
              (player == "scissor" and computer == "paper")
              or
              (player == "paper" and computer == "rock")
              ):
             print("You win this round!")
             player_score +=1
        else:
            print("Computer wins this round!")
            computer_score +=1

            #Scoreboard
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")        

while True:
    print("1.Start Game" \
    "\n2.Exit")
    choice = input("Please enter your chocie ").strip()

    if choice == "1":
        rps_game()
    elif choice == "2":
           print("Exiting. . . .")
           break
    else:
        print("Invalid choice!")

