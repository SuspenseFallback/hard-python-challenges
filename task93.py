points = 0

for i in range(5):
    result = input("Did you win, lose or draw the match? ").lower()

    if result == "win":
        points += 3
    elif result == "draw":
        points += 1

print("Total points earned:", points)

if points < 6:
    print("You are getting demoted")
elif points >= 12:
    print("You are getting promoted")
else:
    print("You are staying in the same division.")
