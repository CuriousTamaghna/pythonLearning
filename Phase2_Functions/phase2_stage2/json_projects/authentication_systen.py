#May 23 11:50 Login and signup system

import json

def load_users():
    
    try:
        with open("Phase2_Functions/phase2_stage2/json_projects/login.json" , "r") as file:
            users = json.load(file)
            return users
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
def save_user(users):
    with open("Phase2_Functions/phase2_stage2/json_projects/login.json","w") as file:
        json.dump(users,file,indent=4)

def add_user(users):
    username = input("Enter the username: ").strip()

    password = input("Enter passoword for this user: ").strip()

    user = {
        "username":username,
        "password":password
    }

    users.append(user)
    save_user(users)

def login_user(users):
    if not users:
        print("No users registered!")
    else:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        found = False

        for user in users:
            if (user['username'] == username and user['password'] == password):
                print(f"Welcome {user['username']}!")
                found = True
                break
        
        if not found:
            print("Invalid username or password!")

def view_users(users):
    if not users:
        print("No user registered!")
    else:
        print("\nRegistered Users:\n")

        for i, user in enumerate(users,start = 1):
            print(f"{i}."
                  f"{user['username']}")
            
def delete_user(users):
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        found = False

        for user in users:
            if (user['username'] == username and user['password'] == password):
                
                users.remove(user)

                found = True
                break
        
        if not found:
            print("Invalid username or password!")


users = load_users()

while True:
    print("""
            1.Registered User
            2.Login User
            3.View Users
            4.Exit
""")
    
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_user(users)
    
    elif choice == "2":
        login_user(users)
    
    elif choice == "3":
        view_users(users)
    elif choice == "4":
        print("Exiting System. . .")
        break
    else:
        print("Invalid choice!")

