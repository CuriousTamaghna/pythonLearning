#May 3 23:30 todo list but it saves the information in a file

try:
    with open ("tasks.txt", "r") as files:
        tasks = [line.strip() for line in files]
        #with open ("tasks.txt", "r") as files:
            #tasks=[]
            #for line in files:
            #    tasks.append(line.strip()) 
            #   this is as same as above task code
except FileNotFoundError:
    tasks=[]

while True:
    print("""\n 1.Add Task
             \n  2.View Tasks
             \n3.Delete Task
             \n4.Exit
""")
    

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        task = input("Enter the task: ").strip()
        tasks.append(task)

        with open ("tasks.txt", "a") as files:
            files.write(task+"\n")

    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:
            for i,task in enumerate(tasks, start=1):
                print(f"{i}.{task}")    
    elif choice == "3":
        if not tasks:
            print("No tasks to delete!")
        else:
            print("choose from the list which task you want to delete. . .")
            for i,task in enumerate(tasks, start=1):
                print(f"{i}.{task}")

            try:
                index = int(input("Enter task number to delete: "))
                if 1<=index <= len(tasks):
                    removed_task =tasks.pop(index-1)
                    print(f"Deleted: {removed_task}")

                    #after deleting now we need to update the task
                    with open("tasks.txt", "w") as files:
                        for t in tasks:
                            files.write(t+"\n")
                else:
                    print("Invalid Number!")                
            except ValueError:
                print("Please enter a valid number!")            
    elif choice == "4":
        print("Exiting...")
        break       
    else:
        print("Invalid Choice!")             

#finished in may 5 , 21:59

