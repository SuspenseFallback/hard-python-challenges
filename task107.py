count = 4
password = input("Enter password: ")

while count > 0:
    if password == "Rashford":
        break
    print("Incorrect password")
    count -= 1

    if count == 0:
        print("Locked")
        exit(0)
    password = input("Enter password: ")

print("Correct password")
