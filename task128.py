count = 4

while count > 0:
    height = float(input("What is your height in cm? "))

    if height < 135:
        print("Sorry, you cannot go on this ride \n")
        continue

    gender = input("Are you male or female? ").lower()

    while not (gender == "male") and not (gender == "female"):
        print("Please select a gender")
        gender = input("Are you male or female? ").lower()

    if gender == "female":
        pregnant = input("Are you pregnant? (y/n) ")
        pregnant = True if pregnant == "y" else False

        if pregnant:
            print("Sorry, you cannot go on this ride \n")
            continue

    print()
    count -= 1

print("The ride is now full, enjoy your ride!")
