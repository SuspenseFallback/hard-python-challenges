booking_fee = 5
first_mile_price = 2
mile_price = 0.25
gas_price_per_mile = 0.5

miles = float(input("How many miles are you going to drive? "))

total = (
    booking_fee
    + first_mile_price
    + (mile_price * (miles - 1))
    + (gas_price_per_mile * miles)
)

print("Your total is:", total, "pounds.")
