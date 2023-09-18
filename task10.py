number_of_meals = int(input("How many meals do you want to buy? "))
price_of_meal = float(input("What is the price of one meal (in dollars)? "))
number_of_drinks = int(input("How many drinks do you want to buy? "))
price_of_drink = float(input("What is the price of one drink (in dollars)?? "))

total_meal_price = number_of_meals * price_of_meal
total_drink_price = number_of_drinks * price_of_drink

total = total_meal_price + total_drink_price

print("Your total price comes up to", total, "dollars")
