#May 16 Authentication System(Login&SignUp)

users=[]
while True:
    print("""
1. Register User
2. Login
3. Change Password
4. Delete Account
5. View Users
6. Exit
""")

    choice=input("Enter your choice!")

    #Register User
    if choice=="1":
        username=input("Enter the user name: ")
        password = input("Enter password: ")
        
        found=False
        for user in users: #did not wrote this logic
            if username == user['username']: 
                found =True
                break
        if found:
            print("Username already exits!")
        else:
            user = {'username': username, 'password': password}
            users.append(user)
            print("User registered successfully!")
    #Login
    elif choice=="2":
        if not users:
            print("No registered users!")
        else:
            auth_user=input("Enter the username: ").strip()
            auth_password=input("Enter the password: ").strip()
            found=False
            for user in users:
                if auth_user==user['username'] and auth_password==user['password']:
                    found=True
                    print("Login successfull!")
                    break #did wrong forget to writie it!
            if not found:
                print("Invalid username or password!")
    #Change Password
    elif choice=="3":
        if not users:
            print("No registered users!")
        else:
            username=input("Enter username: ").strip()
            old_password=input("Enter password: ").strip()

            found=False
            for user in users:
                if username==user['username'] and old_password==user['password']:
                    new_password=input("Enter new password: ").strip()
                    user['password']=new_password
                    #users.append(user) #did not need this line because the user is pointing to the users list so it's not a matter!
                    print("Password changed successfully!")
                    found=True
                    break
            if not found:
                print("Invalid username or password")
    #Delete Account (May 18 15:38)
    elif choice=="4":
        if not users:
            print("No registered user!")
        else:
            username= input("Enter username to delete account: ").strip()
            password= input("Enter password: ").strip()
            found = False
            for i,user in enumerate(users):
                if username == user["username"] and password ==user["password"]:
                    users.pop(i)
                    print("Account deleted successfully!")
                    found=True
                    break
            if not found:
                print("Invalid username or password!")
    #View users
    elif choice=="5":
        if not users:
            print("No registered users!")
        else:
            print("\nRegistered Users: ")
            for i , user in enumerate(users,start=1):
                print(f"{i}.{user['username']}")
    #Exit choice
    elif choice=="6":
        print("Exiting Authentication System. . .")
        break
    #Invalid choice
    else:
        print("Invalid choice!")                 
        
        
        




