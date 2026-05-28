#May 28 14:42  
#New Topic 'Composition'

class CPU:
    def __init__(self,brand,cores):
        self.brand = brand
        self.cores = cores
    
    def display_cpu(self):
        print(f"CPU Brand: {self.brand}")
        print(f"Cores: {self.cores}")
    

class Computer:
    def __init__(self,company,cpu):
        self.company = company
        #composition
        self.cpu = cpu

    def display_computer(self):
        print(f"Company: {self.company}")

        #Access cpu object
        self.cpu.display_cpu()

cpu1 = CPU("Intel",8)

#Pass CPU object into Computer
computer1 = Computer("Dell",cpu1)

#display
computer1.display_computer()