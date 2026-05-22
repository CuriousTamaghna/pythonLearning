# 🧮 Quiz-Based Math Game

import random


def math_game():

    score = 0

    total_questions = 5

    operators = ["+", "-", "*"]

    print("\n🧮 Welcome to Math Quiz Game!")

    for i in range(total_questions):

        # 🟢 Random numbers
        num1 = random.randint(1, 20)

        num2 = random.randint(1, 20)

        # 🔵 Random operator
        operator = random.choice(operators)

        # 🟡 Calculate correct answer
        if operator == "+":

            correct_answer = num1 + num2

        elif operator == "-":

            correct_answer = num1 - num2

        else:

            correct_answer = num1 * num2

        # 🔴 Show question
        print(f"\nQuestion {i+1}")

        print(f"{num1} {operator} {num2}")

        # ⚫ User answer
        try:

            user_answer = int(
                input("Enter your answer: ")
            )

            # 🟣 Check answer
            if user_answer == correct_answer:

                print("✅ Correct!")

                score += 1

            else:

                print("❌ Wrong!")

                print(
                    f"Correct Answer: "
                    f"{correct_answer}"
                )

        except ValueError:

            print("Please enter a valid number!")

    # 🟤 Final score
    print("\n🎯 Quiz Finished!")

    print(
        f"Your Final Score: "
        f"{score}/{total_questions}"
    )


# 🟢 Main Program
while True:

    print("""
1. Start Math Quiz
2. Exit
""")

    choice = input("Enter your choice: ").strip()

    # 🟢 Start Quiz
    if choice == "1":

        math_game()

    # 🔴 Exit
    elif choice == "2":

        print("Exiting Math Quiz...")
        break

    # ❌ Invalid
    else:
        print("Invalid choice!")