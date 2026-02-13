
actual_password = "today"

password = ""
while password != actual_password:
    password = input("Enter your password:")
    if password != actual_password:
        print("Incorrect password. Please try again.")
print("Access Granted")
