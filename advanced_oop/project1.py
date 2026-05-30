#May 30 11:49 
#Employee project using OOP

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self._salary = salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if value >= 0 :
            self._salary = value
        else:
            print("Invalid salary!")
    def __str__(self):
        return f"Employee name: {self.name} , age: {self.age} , salary: {self._salary}"
    
"""emp = Employee("Rahul",25,50000)
print(emp)

emp.salary = -1000
print(emp)"""

employees = []

while True:
    print("1.Add Employee" \
    "\n2.View Employee" \
    "\n3.Search Employee" \
    "\n4.Delete Employee" \
    "\n5.Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        name = input("Enter employee name: ").strip()
        age = int(input("Enter employee's age: "))
        salary = int(input("Enter employee's salary: "))

        emp = Employee(name,age,salary)

        employees.append(emp)
        print("Employees added suceessfully!")

    elif choice == "2":
        if not employees:
            print("No employees to print!")
        else:
            print("Employees list: ")
            for employee in employees:
                print(employee)
    
    elif choice == "3":
        search_name = input("Enter employee name to search: ").strip()

        found = False

        for employee in employees:
            if employee.name.lower() == search_name.lower():
                print(employee)
                found = True
                break
        if not found:
            print("Employee not found!")
    
    elif choice == "4":
        delete_name = input("Enter employee name to delete: ").strip()

        found = False

        for employee in employees:
            if employee.name.lower() == delete_name.lower():
                employee.remove(employee)
                print("Employee deleted successfully!")
                found = True
                break
        if not found:
            print("Employee not found!")

    elif choice == "5":
        print("Exiting program. . .")
        break

    else:
        print("Invalid choice! Please try again: ")
