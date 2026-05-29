#May 29 11:17 - 14:35
#Hotel Room Booking

class Room:
    def __init__(self,room_number,room_type,price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.booked= False
    
    def display_room(self):
        status = "Booked" if self.booked else "Available"
        print(f"Room number: {self.room_number}")
        print(f"Room type: {self.room_type}")
        print(f"Price: {self.price}")
        print(f"Status: {status}")
    
    def book_room(self):
        if not self.booked:
            self.booked = True
            print("Room booked successfully!")
        else:
            print("Room already booked!")
    def checkout_room(self):
        if self.booked:
            self.booked = False
            print("Checkout successfull!")
        else:
            print("Room is already available!")

class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self,room):
        self.rooms.append(room)
        print("Room added successfully!")
    
    def view_rooms(self):
        if not self.rooms:
            print("No rooms available!")
        else:
            print("\nRoom List!")
            for room in self.rooms:
                room.display_room()
                print()
    
    def search_room(self,room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None


    
hotel = Hotel()        


while True:
    print("1.Add Room" \
    "\n2.View Room" \
    "\n3.Book Room" \
    "\n4.Checkout Room" \
    "\n5.Search Room" \
    "\n6.Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        room_number = int(input("Enter room number"))
        room_type = input("Enter room type: ").strip()
        price = float(input("Enter room price: "))
        room = Room(room_number,room_type,price)

        hotel.add_room(room)


    elif choice == "2":
        hotel.view_rooms()

    elif choice == "3":
        room_number = int(input("Enter room number: "))
        room = hotel.search_room(room_number)
        if room:
            room.book_room()
        else:
            print("Room not found!")
    
    elif choice == "4":
        room_number = int(input("Enter room number: "))
        room = hotel.search_room(room_number)
        if room :
            room.checkout_room()
        else:
            print("Room not found!")

    elif choice == "5":
        room_number = int(input("Enter room number: "))
        room = hotel.search_room(room_number)
        if room:
            room.display_room()

        else:
            print("Room not found!")

    elif choice == "6":
        print("Exiting. . .")
        break
    else:
        print("Invalid input!")