#May 22 13:43 Quiz Based Math Game

import random


def math_quiz_generator():

    score = 0

    total_question = 5

    operators = ['+','-','*']

    print("Start the quiz game!")

    for i in range(total_question): #here i did a mistake of not writing the range function and it throwed me a error ! the int object is not iterable!
        num1= random.randint(1,20)
        num2 = random.randint(1,20)

        operator= random.choice(operators)

        
        if operator == '+':
            correct_answer = num1+num2
        elif operator == '-':
            correct_answer = num1-num2
        elif operator == '*':
            correct_answer = num1*num2
        else:
            print("Invalid operator choice for this quiz!")
        
        print(f"\nQuestion {i+1}")

        print(f"{num1} {operator} {num2}")

        try:
            user_answer = int(input("Enter your answer: "))
            if user_answer == correct_answer :
                print("Correct!!!")
                score += 1
            else:
                print("Wrong!")
                print(f"Correct Answer: {correct_answer}")
        except ValueError:
            print("Please enter a valid number!")
    
    print("Quiz finished!")
    print(f"Your final score: {score}/{total_question}")

#Main program
while True:
    print("1.Start Game" \
    "\n2.Exit")
    choice = input("Please enter your chocie ").strip()

    if choice == "1":
        math_quiz_generator()

    elif choice == "2":
        print("Exiting. . . .")
        break
    else:
        print("Invalid choice!")