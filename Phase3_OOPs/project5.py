#May 27 00:35 
#Inheritence

#Parent Class
class Person:
    def __init__(self,name):
        self.name = name

    def display_name(self): #this will be accessed through creating object of Student class not even Person class.
        print(f"Name: {self.name}")
    
class Student(Person): #inheritence happend here! 
    def __init__(self,name,marks):

        #Call Parent Constructor
        super().__init__(name)

        self.marks = marks

    def display_marks(self):
        print(f"Marks: {self.marks}")

#creating object
student1 = Student("Tamaghna", 90)

#Access Pareent method
student1.display_name()

#Access Child Method
student1.display_marks()