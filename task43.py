num = int(input("Enter a number: "))
unit = input("What is the unit? (bit, byte, kilobyte): ").lower()
convert = input("What is the unit to convert to? (bit, byte, kilobyte): ").lower()

while unit == convert:
    print("Please enter a different unit")
    unit = input("What is the unit? (bit, byte, kilobyte): ").lower()
    convert = input("What is the unit to convert to? (bit, byte, kilobyte): ").lower()

if unit == "bit" and convert == "byte":
    print(num / 8)
elif unit == "bit" and convert == "kilobyte":
    print(num / 8000)
elif unit == "byte" and convert == "kilobyte":
    print(num / 1000)
elif unit == "byte" and convert == "bit":
    print(num * 8)
elif unit == "kilobyte" and convert == "bit":
    print(num * 8000)
elif unit == "kilobyte" and convert == "byte":
    print(num * 1000)
else:
    print("Invalid input")
