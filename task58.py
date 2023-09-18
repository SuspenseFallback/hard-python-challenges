name = input("Enter your name: ")
upper_or_lower = input(
    "Would you like your name to be displayed in uppercase or lowercase? "
).lower()

if upper_or_lower == "uppercase" or upper_or_lower == "upper":
    print(name.upper())
elif upper_or_lower == "lowercase" or upper_or_lower == "lower":
    print(name.lower())
else:
    print("Wrong choice.")
