num_of_tickets = int(input("How many tickets do you want to buy? "))

while num_of_tickets < 5 or num_of_tickets > 30:
    print("Incorrect - must be between 5 and 30 tickets")
    num_of_tickets = int(input("How many tickets do you want to buy? "))

num_of_children = int(input("How many children will there be? "))

while num_of_children < 5 or num_of_children > 25:
    print("Incorrect - must be between 5 and 25 children")
    num_of_children = int(input("How many children will there be? "))


num_of_adults = int(input("How many adults will there be? "))

while num_of_adults >= 6:
    print("Incorrect - must be below 6")
    num_of_adults = int(input("How many adults will there be? "))

total = num_of_children * 6 + num_of_adults * 8

print("The total will be", total, "dollars")
