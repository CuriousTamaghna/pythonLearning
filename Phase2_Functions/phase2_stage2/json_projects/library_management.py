#May 26 15:27 Json Based Library Management System

import json

def load_books():
    try:
        with open("Phase2_Functions/phase2_stage2/json_projects/books.json" , "r") as file:
            books = json.load(file)
            return books
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
def save_books(books):
    with open("Phase2_Functions/phase2_stage2/json_projects/library.json" , "w") as file:
        json.dump(books,file,indent=4)

def add_book(books):
        name = input("Enter the book's name: ").strip()
        author = input("Enter author's name: ").strip()

        book = {
            'name':name,
            'author':author,
            'available':True
        }

        books.append(book)
        save_books(books)
        print("Book added successfully!")

def view_books(books):
    if not books:
        print("No book available!")
    else:
        for i,book in enumerate(books,start=1):
            print(f"{book['name']} : {book['author']}")
            print(f"Availability: {book['available']}")

def borrow_book(books):
    if not books:
        print("No book available!")
    else:
        title = input("Enter the book name to borrow: ").strip()

        found = False

        for book in books:
            if book['name'].lower() == title.lower():
                if book['available']:    
                    book['available'] = False
                    save_books(books)
                    print("Book borrowed successfully!")
                else:
                    print("Book already borrowed!")
                found = True
                break
        if not found:
            print("The book you are searching hasn't been found!")
        
def return_book(books):
    if not books:
        print("No book available!")
    else:
        title = input("Enter the book name to borrow: ").strip()

        found = False

        for book in books:
            if book['name'].lower() == title.lower():
                if not book['available']:    
                    book['available'] = True
                    save_books(books)
                    print("Book returned successfully!")
                else:
                    print("Book is already available!")
                found = True
                break
        if not found:
            print("The book you are searching hasn't been found!")

def delete_book(books):
    title = input("Enter the book name to borrow: ").strip()

    found = False

    for book in books:
        if book['name'].lower() == title.lower():
            books.remove(book)
            save_books(books)
            print("Book deleted successfully!")
            found = True
            break
    if not found:
        print("The book you are searching hasn't been found!")

def search_book(books):
    title = input("Enter the book name to borrow: ").strip()

    found = False


    for book in books:
        if book['name'].lower() == title.lower():
            status = ("Available" if book['available'] else "Borrowed")
            print("Book found:-\n")
            print(f"Book {book['name']} : {book['author']}!")
            print(f"Availability: {status}")
            found = True
            break
    if not found:
        print("The book you are searching hasn't been found!")    

books = load_books()

while True:

    print("""
1. Add Book
2. View Books
3. Borrow Book
4. Return Book
5. Delete Book
6. Search Book
7. Exit
""")

    choice = input(
        "Enter your choice: "
    ).strip()

    # 🟢 Add
    if choice == "1":

        add_book(books)

    # 🔵 View
    elif choice == "2":

        view_books(books)

    # 🟡 Borrow
    elif choice == "3":

        borrow_book(books)

    # 🟣 Return
    elif choice == "4":

        return_book(books)

    # ⚫ Delete
    elif choice == "5":

        delete_book(books)

    # 🔥 Search
    elif choice == "6":

        search_book(books)

    # 🔴 Exit
    elif choice == "7":

        print(
            "Exiting Library System..."
        )

        break

    # ❌ Invalid
    else:

        print("Invalid choice!")
