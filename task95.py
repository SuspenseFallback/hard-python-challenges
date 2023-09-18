total = 0
highest_amount = 0
lowest_amount = float("inf")

for i in range(1, 7):
    num_of_rolls = int(input("How many did you buy in supermarket " + str(i) + "? "))

    if num_of_rolls > 0:
        price_of_roll = float(input("How much did each roll cost? "))

        if price_of_roll > highest_amount:
            highest_amount = price_of_roll
        elif price_of_roll < lowest_amount:
            lowest_amount = price_of_roll

        total += num_of_rolls * price_of_roll

print("\n", "-" * 30, "\n")

print("Total amount:", total)
print("Highest amount spent on a single roll:", highest_amount)
print("Lowest amount spent on a single roll:", lowest_amount)
