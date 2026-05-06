#May 3 16:52 ToDo List 

"""
In this app we will be doing four things one> add task , two> view task, three>delete task, four>Exit
"""

tasks = [];

while True:

    print("1.Add Task!\n2.View Task\n3.Delete Task\n4.Exit");

    choice = input("Enter your choice here: ").strip();

    if choice=="1":
        task=input("Enter the task: ");
        tasks.append(task);
    elif choice=="2":
        print(tasks);
    elif choice =="3":
        whichTask=input("Enter the task you want to delete: ").strip();
        if whichTask in tasks:
            tasks.remove(whichTask);
            print("Task deleted!")
        else :
            print("Invalid Task!")
    elif choice=="4":
        print("Exiting...");
        break
    else:
        print("Invalid Choice!");

