#May 30 02:28 
#__str__ method 
# with this method we don't need to take the created object name and print like print(car1.name)
#we just can print(car) like this

class Car:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"Car name: {self.name}"

car1 = Car("Toyota Corolla")
car2 = Car("Honda city")
car3 = Car("Hyundai eon")
car4 = Car("Maruti Suzuki IGNIS")
car5 = Car("Mahindra Thar")

print(car1)

cars = [car1,car2,car3,car4,car5]

for car in cars:
    print(car)



