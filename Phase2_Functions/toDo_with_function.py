#May 19 Todo with function 18:14 

tasks =[]

def add_task(tasks):
    task = input("Enter task: ").strip()
    tasks.append(task)
    print("Task addded successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available!")
    else:
        for i ,task in enumerate(tasks,start=1):
            print(f"{i}.{task}")

def delete_task(tasks):

    if not tasks:
        print("No tasks available!")
    else:
        print("\nTasks List:")
        for i,task in enumerate(tasks,start=1):
            print(f"{i}.{task}")
        try:
            index = int(input("Enter task number to delette: "))
            if 1<=index<=len(tasks):
                removed_task=tasks.pop(index-1)
                print(f"{removed_task} is removed!")
            else:
                print("Please enter a valid number!")
        except ValueError:
            print("Please enter a valid number!")

#Main Program
while True:
    print("""
                1.Add Task
                2.View Task
                3.Delete Task
                4.Exit
""")
    
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        delete_task(tasks)
    elif choice == "4":
        print("Exiting To-Do App. . .")
        break
    else:
        print("Invalid choice!")


