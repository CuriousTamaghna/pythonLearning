#May 14 01:55 Starting Contacts book app!

contacts=[]

while True :
    
    print("""\n1.Add Contact
          2.View Contact
          3.Search Contact
          4.Update Coontact
          5.Delete Contact
          6.Exit
""")
    
    choice = input("Enter your choice: ")

    if choice == "1" :
        name = input("Enter name: ").strip()
        phone = input("Enter the phone number: ").strip()

        contact ={"name":name,"phone":phone}

        contacts.append(contact)

    elif choice== "2":
         if not contacts:
              print("No contacts to print!")
         else:
              for contact in contacts:
                   print(f"{contact['name']} : {contact['phone']}")

    elif choice == "3" :
        if not contacts:
            print("No contact to show!")
        else:
            name= input("Enter name you want to search: ")
            found= False
            for contact in contacts:
                     if name == contact["name"]:
                          print("Contact Found!")
                          print(f"\n{contact['name']} : {contact['phone']}")

                          found = True
                          break
                     if not found:
                          print("Contact is not in the book!")
    elif choice== "4":
         if not contacts :
              print("No contacts to update!")
         else:
              name = input("Enter the name of the contact: ").strip()
              found= False
              for contact in contacts:
                   if name== contact['name']:
                        new_phone = input("Enter the new number for this contact: ").strip()
                        contact['phone']= new_phone

                        found = True
                        break
                   if not found:
                        print("Contact not found!")
    elif choice== "5":
            if not contacts :
                print("No contacts to delete!")
            else:
                print("\ncontacts list:")
                for i,contact in enumerate(contacts, start=1):
                     print(f"{i}.{contact['name']} - {contact['phone']}")

                try:
                    index = int(input("Enter contact number to delete: "))
                    if 1<=index<=len(contacts):
                         removed_contact=contacts.pop(index-1)  
                         print(f"Deleted: {removed_contact['name']} : {removed_contact['phone']}")
                except ValueError:
                     print("Please enter a valid number!")
    elif choice == "6":
         print("Exiting. . . ")
         break
    else:
         print("Please enter a valid choice!")
         #completed at 3:00 AM May 14th 