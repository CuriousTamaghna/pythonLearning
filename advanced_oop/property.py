#May30 10:52
#@property

class Employee:
    def __init__(self,salary):
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if value>=0:
            self._salary = value
        else:
            print("Invalid Salary!")

emp = Employee(50000)

print(emp.salary)
print(emp._salary)

emp.salary= -100000

print(emp.salary) 
