to_convert = ""
while to_convert == "":
    to_convert = input("Would you like to convert to Celsius or Fahrenheit: ").lower()
    if to_convert != "celsius" and to_convert != "fahrenheit":
        print("Please enter a valid value")
        to_convert = ""

temp = ""
while temp == "":
    try:
        if to_convert == "celsius":
            temp = float(input("Enter a temperature in Fahrenheit: "))
        else:
            temp = float(input("Enter a temperature in Celsius: "))
    except ValueError:
        print("Invalid temperature")


def convert_to_celsius(val):
    return (val - 32) * 5 / 9


def convert_to_fahrenheit(val):
    return (val * 9 / 5) + 32


if to_convert == "celsius":
    print("The temperature in Celsius is: ", convert_to_celsius(temp))
else:
    print("The temperature in Fahrenheit is: ", convert_to_fahrenheit(temp))
