#May 26 20:00 Basic programming for using class 
#Student Class System

#Create class
class Student:
    #constructor
    def __init__(self,name,marks):
        #Object Attributes
        self.name = name
        self.marks = marks

    #Methods
    def display(self):
        print(f"Student name: {self.name}")
        print(f"Student Marks: {self.marks}")

#Create Objects

student1 = Student("Raj", 90)
student2 = Student("Bibhu", 92)
student3 = Student("Swarnayu", 87)

#Access attributes
print(student1.name)
print(student2.marks)

#Call methods
student1.display()
print()
student2.display()