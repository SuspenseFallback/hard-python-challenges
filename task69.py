number = int(input("Enter a number: "))

print("\n", "-" * 30, "\n")

for i in range(1, 101):
    print(number, "x", i, "=", number * i)
