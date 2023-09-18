school_name = input("Enter school name: ")
upper_or_lower = input(
    "Would you like it to be displayed in uppercase or lowercase? "
).lower()

if upper_or_lower == "uppercase":
    print(school_name.upper())
elif upper_or_lower == "lowercase":
    print(school_name.lower())
else:
    print("Wrong option")
