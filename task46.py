is_it_august = input("Is it August? (y/n) ").lower()

if is_it_august == "y":
    print("Yay summer holiday")
else:
    is_it_weekend = input("Is it the weekend? (y/n) ").lower()

    if is_it_weekend == "y":
        print("Yay no school")
    else:
        print("Bad luck, you have school today")
