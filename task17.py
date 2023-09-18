num_of_sweets = int(input("How many sweets do you want to buy? "))
price_of_sweets = float(input("How much does 1 sweet cost? "))

total = num_of_sweets * price_of_sweets
finaltotal = "{:.2f}".format(total * 1.2)

print("Your total after tax is $" + str(finaltotal))
