#May 28 22:14 
#E-commerce system using OOPs 

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def display_product(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")

class Cart:
    def __init__(self):
        self.products = []
    def add_product(self,product):
        self.products.append(product)
        print(f"Product: {product.name} added!")
    def view_product(self):
        if not self.products:
            print("Cart is empty!")
        else:
            print("Cart Items:\n")
            for product in self.products:
                product.display_product()
    def calculate_total(self):
        total = 0
        for product in self.products:
            total+=product.price
        print(f"Total: {total}")

class Customer:
    def __init__(self,name):
        self.name = name

        #Composition
        self.cart = Cart()

    def display_customer(self):
        print(f"Customer: {self.name}")

customer1 = Customer("Tamaghna")

product1 = Product("Laptop", 50000)
product2 = Product("Mouse", 1000)
product3 = Product("Keyboard", 2000)

customer1.cart.add_product(product1)
customer1.cart.add_product(product2)
customer1.cart.add_product(product3)

customer1.cart.view_product()
customer1.cart.calculate_total()
