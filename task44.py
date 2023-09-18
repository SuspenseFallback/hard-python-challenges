num = ""
while num == "":
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid number")

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
