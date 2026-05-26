#May 26 22:33 OOP STUDENT MANAGEMENT SYSTEM

class Students:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

students = []

while True:
    
    print("1.Add Student" \
    "2.View Students" \
    "3.Search Students" \
    "4.Update Marks" \
    "5.Delete Student" \
    "6.Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        name = input("Enter student's name: ").strip()
        marks = int(input("Enter student's marks: "))

        student = Students(name,marks)

        students.append(student)

        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student available!")
        else:
            for student in students:
                student.display()
                print()
    
    elif choice == "3":
        name = input("Enter the student's name: ").strip()

        found = False

        for student in students:
            if student.name == name :
                student.display()
                found = True
                break
        if not found :
            print("Student not found!")
    
    elif choice == "4":
        name = input("Enter the student's name: ").strip()

        found = False

        for student in students:
            if student.name == name :
                new_marks = int(input("Enter student's updated marks: "))
                student.marks = new_marks
                found = True
                break
        if not found :
            print("Student not found!")

    elif choice == "5":
        name = input("Enter the student's name: ").strip()

        found = False

        for student in students:
            if student.name == name :
                students.remove(student)
                found = True
                break
        if not found :
            print("Student not found!")
    
    elif choice == "6":
        print("Exiting. . . .")
        break
    else:
        print("Invalid choice!")