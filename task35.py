ticket_price = 20

season_ticket = input("Do you have a season ticket (y/n)? ").lower()

if season_ticket == "y":
    print("£" + str(20 * 0.5))
else:
    print("£" + str(20 * 0.75))
