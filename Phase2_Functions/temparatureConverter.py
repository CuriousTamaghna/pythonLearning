#May 19 Temparature Converter Project 

def celsius_to_farenheit(temp):
    return (temp*(9/5))+32

def farenheit_to_celsius(temp):
    return (5/9)*(temp-32)

def celsius_to_kelvin(temp):
    return temp+273.15

def kelvin_to_celsius(temp):
    return temp-273.15

while True:
    print("""
                1.Celsius to Farenheit
                2.Farenheit to Celsius
                3.Celsius to Kelvin
                4.Kelvin to Celsius
                5.Exit
        """)
    
    choice=input("Enter your choice: ").strip()

    if choice == "1":
        temparature=int(input("Enter temperature in celsius: "))
        result=celsius_to_farenheit(temparature)
        print(f"{result} Farenheit")
    elif choice == "2":
        temparature=int(input("Enter temperature in farenheit: "))
        result=farenheit_to_celsius(temparature)
        print(f"{result} Celsius")
    elif choice == "3":
        temparature=int(input("Enter temperature in celsius: "))
        result=celsius_to_kelvin(temparature)
        print(f"{result} Kelvin")
    elif choice == "4":
        temparature=int(input("Enter temperature in Kelvin: "))
        result=kelvin_to_celsius(temparature)
        print(f"{result} Celsius")
    elif choice=="5":
        print("Exiting. . .")
        break
    else:
        print("Invalid choice!")
    