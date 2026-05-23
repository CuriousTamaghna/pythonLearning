#May 23 JSON Based Contact Book 10:06

#Add Contact
#View Contacts 
#Search Contact
#Update Contact
#Delete Contact
#Exit
import json


def load_contact_book():
    try:
        with open("Phase2_Functions/phase2_stage2/json_projects/contacts.json", "r") as file:
            contacts = json.load(file)
            return contacts
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_contact(contacts):
    with open("Phase2_Functions/phase2_stage2/json_projects/contacts.json", "w") as file:
        json.dump(contacts,file,indent=4)

def add_contact(contacts):
    name = input("Enter contact's name: ").strip()

    phone = input("Enter contact's phone")

    contact = {
        "name":name,
        "phone":phone
    }

    contacts.append(contact)
    save_contact(contacts)

    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available!")
    else:
        print("\nContact List")
        for i, contact in enumerate(contacts,start=1):
            print(f"{i}." \
            f"{contact['name']}" \
            f"->{contact['phone']}")

def search_contact(contacts):
    if not contacts:
        print("No contacts to print!")
    else:
        contact_name = input("Enter the name you want to search: ").strip()
        found =False
        for contact in contacts:
            if contact['name'].lower() == contact_name.lower():
                print("Contact found!")
                print(f"Contact's name: {contact['name']} & Contact's Phone: {contact['phone']}")
                found = True
                break
        if not found:
            print("Contact Not Found!")

#Update Contact
def update_contact(contacts):
    if not contacts:
        print("No contacts to print!")
    else:
        contact_name = input("Enter the name you want to search: ").strip()
        found =False
        for contact in contacts:
            if contact_name.lower() == contact['name'].lower():
                print("Contact found!")
                update_contact_name = input("Enter the updated name: ").strip()
                update_contact_phone = input("Enter contact's phone: ")
                contact['phone'] = update_contact_phone
                contact['name'] = update_contact_name
                save_contact(contacts)
                found = True
                break
        if not found:
            print("Contact Not Found!")

#Delete contact
def delete_contact(contacts):
    if not contacts:
        print("No contacts found!")
    else:
        name = input("Enter contact  name to delete: ").strip()

        found = False

        for contact in contacts: 
            if (contact["name"].lower() == name.lower()):
                contacts.remove(contact)
                save_contact(contacts)
                print("Contact deleted successfully!")
                found = True
                break
        if not found:
            print("Contact not found!")

#Main program
contacts = load_contact_book()

while True:
    print("""\n1.Add Contact
          2.View Contact
          3.Search Contact
          4.Update Coontact
          5.Delete Contact
          6.Exit
""")
    
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        view_contacts(contacts)
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
        print("Invalid choice!")
