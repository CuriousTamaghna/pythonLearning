#May 28 12:36 Student Management System with File Handling
#File Handling + OOP

import json

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"{self.name} : {self.marks}")
    
    def to_dict(self):
        #Convert object to dictionary { } format
        return {
            'name' : self.name,
            'marks' : self.marks
        }
    
def save_students(students):

        data = []
        for student in students:
            data.append(student.to_dict())
        
        with open("Phase3_OOPs/students_oop.json", "w") as file:
            json.dump(data,file,indent=4)
        
        print("Students saved successfully!")

def load_students():
        try:
            with open("Phase3_OOPs/students_oop.json" , "r") as file:
                data=json.load(file)
                students = []
                for student_data in data:
                    student = Student(student_data['name'],student_data['marks'])
                    students.append(student)
                return students
        except FileNotFoundError:
            return []
    

#Main program
students = load_students()

while True:
    print("1.Add Student" \
     "\n2.View Students" \
     "\n3.Save Students" \
     "\n4.Exit")
     
    choice = input("Enter your choice: ").strip()

    if choice == "1":
          name = input("Enter student's name: ").strip()

          marks = float(input("Enter marks: "))

          student = Student(name,marks)

          students.append(student)
          print("Student added!")
    
    #View Students 
    elif choice == "2":
        if not students:
            print("No student available!")
        else:
            for student in students:
                 student.display()
                 print()
    
    elif choice == "3":
        save_students(students)

    elif choice == "4":
        print("Exiting system. . .")
        break
    else:
        print("Invalid choice!")