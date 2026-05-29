#May 29 10:24 -11:16
#Movie Ticket Booking System 

class Movie:
    def __init__(self,name,total_seats):
        self.name = name
        self.total_seats = total_seats
        self.available_seats = total_seats
    def display_movies(self):
        print(f"Movie: {self.name}")
        print(f"Available seats: {self.seat}")
    
    def book_ticket(self,seats):
        if seats <= self.available_seats:
            self.available_seats -= seats
            print(f"{seats} ticket(s) booked successfully!")
        else:
            print("Not enough seats available!")
    
    def cancel_ticket(self,seats):
        if self.available_seats + seats <= self.total_seats:
            self.available_seats += seats
            print(f"{seats} ticket(s) cancelled successfully!")
        else:
            print("Invalid cancellation!")

class Theatre:
    def __init__(self):
        self.movies = []
    
    def add_movies(self,movie):
        self.movies.append(movie)
        print("Movie added successfully!")
    
    def view_movies(self):
        if not self.movies:
            print("No movies available!")
        else:
            print("Movies: ")
            for movie in self.movies:
                movie.display_movies()
                print()
    
    def search_movies(self,name):
        for movie in self.movies:
            if movie.name.lower() == name.lower():
                return movie
        return None
    
theatre = Theatre()

while True:
    print("1.Add Movie" \
    "\n2.View Movies" \
    "\n3.Book Ticket" \
    "\n4.Cancel Ticket" \
    "\n5.Exit")

    choice = input("Enter your choice").strip()

    if choice == "1":
        name = input("Enter movie's name: ").strip()
        seats = int(input("Enter total seats: "))
        movie = Movie(name,seats)
        #composition
        theatre.add_movies(movie)
    elif choice == "2":
        theatre.view_movies()
    elif choice == "3":
        #book ticket
        name = input("Enter the movie's name: ").strip()
        movie = theatre.search_movies(name)
        if movie:
            seats = int(input("How many tickets?"))
            movie.book_ticket(seats)
        else:
            print("Movie not found!")
    elif choice == "4":
        name = input("Enter movie name: ").strip()
        movie = theatre.search_movies(name)
        if movie:
            seats = int(input("How many tickets to cancel?"))
            movie.cancel_ticket(seats)
        else:
            print("Movie not found!")
    elif choice == "5":
        print("Exiting. . .")
        break
    else:
        print("Invalid choice!")
