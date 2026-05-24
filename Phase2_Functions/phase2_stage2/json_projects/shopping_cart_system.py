#May 23 JSON-Based Shopping Cart System 13:44

import json

def load_cart():
    try:
        with open("Phase2_Functions/phase2_stage2/json_projects/cart.json", "r") as file:
            cart = json.load(file)
            return cart
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
def save_cart(cart):
    with open("Phase2_Functions/phase2_stage2/json_projects/cart.json", "w") as file: #mistake1
        json.dump(cart,file,indent=4) #mistake2

def add_product(cart):
    name = input("Enter the product's name: ").strip()

    price = float(input("Enter product's price: "))

    quantity = int(input("Enter product's quantity: "))

    #Existing product check
    for item in cart:
        if (item['product'].lower() == name.lower()):
            item['quantity'] += quantity

            save_cart(cart)

            print("Quantity updated!")
            return
    #New product    
    product = {'product':name, 'price':price, 'quantity': quantity }

    cart.append(product)
    save_cart(cart) #mistake3
    print("Product added successfully!")

def view_cart(cart):
    if not cart:
        print("No product available!")
    else:
        print("Product List!")
        for i,product in enumerate(cart, start=1):
            print(f"{i}.{product['product']}"
                  f"{product['price']} - {product['quantity']}")

def remove_product(cart):
    
    if not cart:
        print("No product available!")
    else:
        delete_name = input("Enter the product's name: ").strip()
        found = False

        for product in cart:
            if (delete_name.lower() == product['product'].lower()): 
                cart.remove(product) #mistake4
                save_cart(cart)
                print("Product deleted!")
                found = True
                break
        if not found:
            print("Product not found!")

def total_value(cart):
    if not cart:
        print("No product available!")
    else:
        total_value = 0
        for product in cart:
            total_value += (product['price']*product['quantity'])
        print(f"Total value: {total_value}")


cart = load_cart()

while True:

    print("""
1. Add Product
2. View Cart
3. Remove Product
4. Calculate Total
5. Exit
""")

    choice = input(
        "Enter your choice: "
    ).strip()

    # 🟢 Add Product
    if choice == "1":

        add_product(cart)

    # 🔵 View Cart
    elif choice == "2":

        view_cart(cart)

    # 🟡 Remove Product
    elif choice == "3":

        remove_product(cart)

    # 🟣 Calculate Total
    elif choice == "4":

        total_value(cart)

    # 🔴 Exit
    elif choice == "5":

        print(
            "Exiting Shopping Cart..."
        )

        break

    # ❌ Invalid
    else:

        print("Invalid choice!")