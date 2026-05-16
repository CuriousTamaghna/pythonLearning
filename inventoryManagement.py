#May15 23:16 Inventory Management System

products= []

while True:
    print("""
            1.Add Product
            2.View Products
            3.Search Products
            4.Update Product Quantity
            5.Sell Product
            6.Delete Product
            7.View Total Inventory Value
            8.Exit
""")
    
    choice = input("Please enter your choice: ").strip()
    #Add product
    if choice=="1":
        name=input("Enter the product name: ").strip()
        price=int(input("Enter product price: "))
        quantity=int(input("Enter product quantity: "))

        product={'name':name,'price':price,'quantity':quantity}
        products.append(product)
    #View Product
    elif choice=="2":
        if not products:
            print("No Products Available!")
        else:
            print("Fetching Product List. . .")
            for i,product in enumerate(products,start=1):
                print(f"{i}.{product['name']} : {product['quantity']} : {product['price']:.2f}/-")
    #Search Product
    elif choice=="3":
        if not products:
            print("No products to show!")
        else:
            search_name=input("Enter the product name: ").strip()
            found=False
            for product in products:
                if search_name==product['name']:
                    print("Product Found!")
                    print(f"{i}.{product['name']} : {product['quantity']} : {product['price']:.2f}")
                    found =True
                    break
            if not found:
                print("Product not found!")
    #Update Product Quantity
    elif choice=="4":
        if not products:
            print("No products to show!")
        else:
            update_name=input("Enter the product name: ").strip()
            found=False
            for product in products:
                if update_name==product['name']:
                    new_quantity= int(input("Enter product Updated Quantity: "))
                    product['quantity']=new_quantity
                    print(f"{product['name']} is update with {product['quantity']} quantity.")
                    found =True
                    break
            if not found:
                print("Product not found!")
    #Sell product
    elif choice=="5":
        if not products:
            print("No products available!")
        else:
            selling_product=input("Enter the product you want to sell!").strip()
            found = False
            for product in products:
                if selling_product==product['name']:
                    selling_quantity = int(input("Enter quantity to sell: "))
                    if selling_quantity<=product['quantity']:
                        product['quantity']-=selling_quantity
                        print(f"Total price will be {selling_quantity*product['price']}")
                        print("Product sold successfully!")
                        print(f"Remaining quantity {product['quantity']}")
                    else:
                        print("Not enough stock available!")
                    found=True
                    break
            if not found:
                print("Product Not found!")
    #Delete Product
    elif choice=="6":
        if not products:
            print("No products available!")
        else:
            print("Products List: ")
            for i,product in enumerate(products,start=1):
                print(f"{i}.{product['name']}")
            try:
                index=input("Please enter the product number to delete: ")
                if 1<=index<=len(products):
                    removed_product = products.pop(index-1)
                    print(f"{removed_product['name']} is removed from inventory.")
                else:
                    print("Invalid product name!")
            except ValueError:
                print("Please enter a valid number")
    #View total inventory value
    elif choice=="7":
        if not products:
            print("No products available!")
        else:
            total_inventory_value=0
            for product in products:
                total_inventory_value +=(product['price']*product['quantity'])
            print(f"Total Inventory Value: {total_inventory_value:.2f}")
    #Exit
    elif choice=="8":
        print("Exiting inventory Management System. . .")
        break
    else:
        print("Invalid choice!")
        




