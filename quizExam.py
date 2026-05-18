#May 18 16:29 Quiz/Exam System
questions =[]
highest_score=0

while True:
    print("""
            1.Add Question
            2.View Questions
            3.Start Quiz
            4.Delete Question
            5.View Highest Score
            6.Exit
""")
    
    choice=input("Enter your choice: ").strip()

    #Add Question
    if choice=="1":
        question_text = input("Enter your questions: ").strip()
        answer_text = input("Enter the answer: ").strip()

        question ={'question':question_text,'answer':answer_text}
        questions.append(question)
        print("Answer Added successfully!")
    elif choice=="2":
        if not questions:
            print("No questions available!")
        else:
            print("\nQuestions List: ")

            for i,question in enumerate(questions,start=1):
                print(f"Q{i}.{question['question']}")
            print("That's all for now!")
    elif choice=="3":
        if not questions:
            print("No questions available!")
        else:
            score=0
            print("\nQize Started: ")

            for i,question in enumerate(questions,start=1):
                print(f"Q{i}.{question['question']}")
                answer_check=input("Enter your answer: ").strip()
                if answer_check.lower()== question['answer'].lower():
                    print("Correct answer\n")
                    score+=1
                else:
                    print("Incorrect Answer!")
            print(f"Quiz Finished! Your Score: {score}")
            if score > highest_score:
                highest_score=score
    elif choice=="4":
        if not questions:
            print("No question available!")
        else:
            print("\nQueestion List:")
            for i,question in enumerate(questions,start=1):
                print(f"Q{i}.{question['question']}")
            try:
                index=int(input("Enter question number to delete: "))
                if 1<=index<=len(questions):
                    removed_question=questions.pop(index-1)
                    print(f"Deleted question: {removed_question['question']}")
                    print(f"Successfully deleted: {removed_question['question']}")
                else:
                    print("Invalid question number!")
            except ValueError:
                print("Please enter a valid number!")
    elif choice=="5":
        print(f"Highest Score: {highest_score}")
    elif choice =="6":
        print("Exiting Quiz Sytem. . .")
        break
    else:
        print("Invalid choice!")
                
