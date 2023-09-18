username = input("Enter username: ")
password = input("Enter password: ")

attempts = 1

while username != "David" or password != "abc":
    print("Incorrect username or password")
    attempts += 1

    username = input("Enter username: ")
    password = input("Enter password: ")

print("It took", attempts, "attempts")
