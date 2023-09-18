username = input("Enter your username: ")

while len(username) < 8:
    print("Username is invalid")
    username = input("Enter your username: ")

print("Your username has been accepted")

password = input("Enter your password: ")

while len(password) < 8 or len(password) > 15:
    print("Password is invalid")
    password = input("Enter your password: ")

print("Your password has been accepted")
