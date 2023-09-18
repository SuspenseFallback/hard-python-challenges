temp = float(input("What is the current temperature (C) ? "))
rain = input("Is it raining (y/n) ? ")

if temp < 13:
    if rain == "y":
        print("Wear a coat and bring an umbrella")
    else:
        print("Wear a coat")
else:
    if rain == "y":
        print("Bring an umbrella")
    else:
        print("You don't need anything")
