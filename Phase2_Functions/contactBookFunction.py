#May 19 21:38 Contact Book Function

contacts = []

def add_contact(contacts):
    name = input("Enter contact's name: ").strip()
    phone = input("Enter contact's phone number: ").strip()

    contact={"name":name,"phone":phone}
    contacts.append(contact)

def view_contact(contacts):
    if not contacts:
        print("No contacts to print!")
    else:
        print("Contact List. . . ")
        for i,contact in enumerate(contacts,start=1):
            print(f"{i}.{contact['name']} : {contact['phone']}")

def search_contact(contacts):
    if not contacts:
        print("No contacts available!")
    else:
        name=input("Enter the contact name to search: ").strip()
        found =False
        for i,contact in enumerate(contacts,start=1):
            if name == contacts['name']:
                print("Contact found!")
                print(f"{i}.{contact['name']} : {contact['phone']}")
                found =True
                break
        if not found:
            print("Contact not found!")

def update_contact(contacts):
    if not contacts:
        print("No contact found!")
    else:
        name=input("Enter the name of the contact: ").strip()
        found =False
        for contact in contacts:
            if name == contact['name']:
                print("Contact found!")
                updated_phone=input("Enter the new number: ").strip()
                contact['phone']=updated_phone
                print("Contact updated successfully!")
                found =True
                break
        if not found:
            print("Contact not found!")

def delete_contact(contacts):
    if not contacts:
        print("No contacts to print!")
    else:
        try:
            for i,contact in enumerate(contacts,start=1):
                print(f"{i}.{contact['name']}")
            index=int(input("Enter the number of contact to delete: "))
            if 1<=index<=len(contacts):
                removed_contact=contacts.pop(index-1)
                print(f"{removed_contact['name']} : {removed_contact['phone']}")
                print("Contact deleted successfully. . .")
            else:
                print("Enter number from list")
        except ValueError:
            print("Invalid input!")

while True:
    print("""
            1. Add Contact
            2. View Contacts
            3. Search Contact
            4. Update Contact
            5. Delete Contact
            6. Exit
            """)
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        view_contact(contacts)
    elif choice == "3":
        search_contact(contacts)
    elif choice == "4":
        update_contact(contacts)
    elif choice == "5":
        delete_contact(contacts)
    elif choice == "6":
        print("Exiting. . . ")
        break
    else:
        print("Enter valid choice!")

#completed 22:25 May 19
