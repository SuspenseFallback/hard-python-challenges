while True:
    number = input("Do you want to enter a number? ")

    if number == "NO":
        break

    num = int(input("Enter an even number: "))

    if num % 2 == 0:
        print(num)
    else:
        print(num + 1)
