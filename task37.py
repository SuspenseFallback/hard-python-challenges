num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))

add_or_multiply = input("Do you want to add or multiply? ").lower()

if add_or_multiply == "add":
    print(num_1 + num_2)
elif add_or_multiply == "multiply":
    print(num_1 * num_2)
else:
    print("Wrong answer")
