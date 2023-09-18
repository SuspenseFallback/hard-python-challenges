is_lockdown = input("Is there a lockdown? ").lower()

if is_lockdown == "no":
    print("Have a good day")
else:
    at_home = input("Are you at home? ").lower()

    if at_home == "yes":
        print("Well done")
    else:
        print("Go home")
