#May 14 17:26 Student Management System

students = []

while True :
    print("""
            1.Add Student
            2.View Students
            3.Search Student
            4.Update Marks
            5.Delete Student
            6.View Average Marks
            7.Exit
""")
    
    choice = input("Enter your choice: ")
    if choice == "1" :
        name = input("Enter student's name: ").strip()
        mark1= int(input("Enter the marks obtained in Physics: "))
        mark2= int(input("Enter the marks obtained in Math: "))
        mark3= int(input("Enter the marks obtained in Chemistry: "))

        marks= [mark1,mark2,mark3]

        student = {"name": name, "marks":marks}

        students.append(student)

    elif choice == "2":
        if not students:
            print("No students to show!")
        else:
            print("\n Students List:")
            for i,student in enumerate(students,start=1):
                print(f"\n{i}. Name:{student['name']}")
                print("Marks: ")
                for j,mark in enumerate(student['marks'], start=1):
                    print(f"Subject {j}:{mark}")


    elif choice == "3":
        if not students:
            print("No students are there to search!")
        else:
            found=False
            search_name = input("Enter the name of the student you want to find: ").strip()
            for student in students:
                if search_name == student['name']:
                    print("Student found!")
                    print(f"{student['name']} : {student['marks']}")
                    found=True
                    break

            if not found:
                print("The student is not found!")
#Update , delete , average, exit is remaining!
#20:48
    elif choice== "4":
        if not students :
            print("No students available!")

        else:

            update_name = input("Enter student name to update marks: ").strip()
            found = False
            for student in students:
                if update_name == student['name']:
                    print("Student found!")
                    mark1=int(input("Enter the first mark to update: "))
                    mark2=int(input("Enter the second mark to update: "))
                    mark3=int(input("Enter the third mark to update: "))

                    student["marks"]=[mark1,mark2,mark3]
                    found=True
                    break
            if not found :
                print("Student not found!")
    elif choice=="5":
        if not students:
            print("No Student available!")
        else:
            for i,student in enumerate(students, start=1):
                print(f"{i}.{student['name']}")

            try:
                index = int(input("Enter from the number to delete student: "))
                if 1<=index<=len(students):
                    removed_student=students.pop(index-1)
                    print(f"student deleted: {removed_student['name']}")
                else:
                    print("Invalid student number!" )
            except ValueError:
                print("Please enter a valid number!")

#average marks:
    elif choice == "6":
        if not students:
            print("No students available!")
        else:
            print("\nAverage Marks!")

            for student in students:
                average = sum(student['marks']) / len(student['marks'])
                print (f"{student['name']} -> {average:.2f}")
    elif choice == "7":
        print("Exiting Student Management System. . . .")
        break
    else:
        print("Invalid choice!")