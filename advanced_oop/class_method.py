#May 30 01:53
#Class method

class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls,new_name):
        cls.school = new_name

Student.change_school("XYZ School")
print(Student.school)
