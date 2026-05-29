#May 29 14:35 - 
#Abstraction

from abc import ABC, abstractmethod

class Charachter(ABC):

    @abstractmethod
    def attack(self):
        pass

class Warrior(Charachter):
    def attack(self):
        print("Sword attack!")

class Mage(Charachter):
    def attack(self):
        print("Magic attack")

class Archer(Charachter):
    def __init__(self):
        self.run = []
    def kick(self):
        print("Archer also can kick!")
    def attack(self): #if i forget to add attack function it will throw an error!
        print("Archer throws arrows!")

warrior = Warrior()
mage = Mage()
archer = Archer()
warrior.attack()
mage.attack()
archer.attack()
archer.kick()