#May 26 22:11 Library Management System

class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = ("available" if self.available else "Borrowed")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} borrowed successfully!")

        else:
            print("book already borrowed!")
    
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"{self.title} returned succcessfully!")
        
        else:
            print("Book already available!")

book1 = Book("Python Basics", "Rahul")

book2 = Book("Data Structure", "Aman")

book1.display()

print()

book1.borrow()

print()

book1.display()

print()

book1.return_book()

print()

book1.display()

