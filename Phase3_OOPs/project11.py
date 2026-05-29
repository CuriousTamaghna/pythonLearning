#May29 09:47 - 10:22
#OOP Inventory Management system

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display_product(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.quantity}")
    
    def update_stock(self,amount):
        self.quantity += amount
        print("Stock Updated Successfully!")
    
    def sell_product(self,amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print(f"{amount} item(s) sold!")
        else:
            print("Insuficient stock!")

class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self,product):
        self.products.append(product)
        print(f"{product.name} is added successfully!")
    
    def view_products(self):
        if not self.products:
            print("Inventory is empty!")
        else:
            print("Product List\n")
            for product in self.products:
                product.display_product()
    
    def search_product(self,name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None
    
    def remove_product(self,name):
        product = self.search_product(name)
        if product:
            self.products.remove(product)
            print("Product removed successfully!")
        else:
            print("Product not found!")

inventory=Inventory()

while True:
    print("1.Add Product" \
    "\n2.View Products" \
    "\n3.Update product" \
    "\n4.Sell product" \
    "\n5.Remove product" \
    "\n6.Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        name = input("Enter product name: ").strip()
        price = float(input("Enter product's price: "))
        quantity = int(input("Enter stock quantity: "))

        product = Product(name,price,quantity)
        #composition
        inventory.add_product(product)
    
    elif choice == "2":
        inventory.view_products()
    elif choice == "3":
        name = input("Enter product name: ").strip()
        product = inventory.search_product(name)
        if product:
            amount = int(input("Enter stock to add: "))
            product.update_stock(amount)
        else:
            print("Product not found!")
    
    elif choice == "4":
        name = input("Enter product name: ").strip()
        product = inventory.search_product(name)
        if product:
            amount = int(input("Enter stock to sell: "))
            product.sell_product(amount)
        else:
            print("Product not found!")

    elif choice == "5":
        name = input("Enter product name to delete: ").strip()
        inventory.remove_product(name)

    elif choice == "6":
        print("Exiting system. . .")
        break
    else:
        print("Invalid choice!")