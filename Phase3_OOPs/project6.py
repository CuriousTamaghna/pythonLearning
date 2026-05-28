#May 27 01:02 
#Polymorphism 

class Animal:
    def sound(self):
        print("Animal Makes Sound!")

class Dog:
    def sound(self):
        print("Dog barks!")

class Cat:
    def sound(self):
        print("Cat meows!")

dog1 = Dog()
cat1 = Cat()

dog1.sound()
cat1.sound()