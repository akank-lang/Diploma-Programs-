allowed_users = ["admin", "manager", "student", "teacher"]

print("Allowed users are:", allowed_users)
username = input("Enter username: ")

if username in allowed_users:
    print("Access Granted")
else:
    print("Access Denied")

choice = input("Do you want to check another user (yes/no): ")

if choice == "yes":
    username = input("Enter username: ")
    if username in allowed_users:
        print("Access Granted")
    else:
        print("Access Denied")
else:
    print("Program Ended")