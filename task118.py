donated = 0
not_donated = 0
total = 0

while True:
    did_donate = input("Did the customer donate? (yes, no, or end) ").lower()

    if did_donate == "end":
        break

    if did_donate == "yes":
        donated += 1
        amount = float(input("How much did the customer donate? "))

        total += amount

    if did_donate == "no":
        not_donated += 1

print("Total number of customers who donated:", donated)
print("Total number of customers who didn't donate:", not_donated)
print("Total donations:", total)
