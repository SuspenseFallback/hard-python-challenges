num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))

want_to_multiply = input("Do you want to multiply the numbers? ").lower()

if want_to_multiply == "yes":
    print(num_1 * num_2)
else:
    print("Ok boss")
