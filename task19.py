def celsius_to_farenheit(degrees):
    return (degrees * 9 / 5) + 32


temp = float(input("Enter temperature (in C): "))

print("The temperature is", celsius_to_farenheit(temp), "F")
