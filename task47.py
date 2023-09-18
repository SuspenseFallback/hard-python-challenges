day = input("What day of the week is it? ").lower()

if day == "saturday" or day == "sunday":
    print("Yay it's the weekend!")
else:
    if day == "monday":
        print("5 days until the weekend")
    elif day == "tuesday":
        print("4 days until the weekend")
    elif day == "wednesday":
        print("3 days until the weekend")
    elif day == "thursday":
        print("2 days until the weekend")
    elif day == "friday":
        print("1 days until the weekend")
    else:
        print("Error")
