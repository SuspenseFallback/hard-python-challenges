total_price = float(input("What is the total price of all your items? (USD) "))
balance_in_gift_card = float(input("How much balance is in your gift card? (USD) "))

if total_price > balance_in_gift_card:
    print("Sorry, you don't have enough balance.")
else:
    balance_in_gift_card = balance_in_gift_card - total_price
    print(total_price, "was deducted from your gift card")
    print(balance_in_gift_card, "remains")
