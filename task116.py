salah = 0
vardy = 0

vote = ""

while vote != "STOP":
    vote = input("Enter Salah, Vardy or STOP: ")
    if vote == "Salah":
        print("You have voted for Salah")
        salah += 1
    elif vote == "Vardy":
        print("You have voted for Vardy")
        vardy += 1
    else:
        if vote != "STOP":
            print("Invalid vote")

print("Salah:", salah)
print("Vardy:", vardy)

if salah > vardy:
    print("Salah won")
elif vardy > salah:
    print("Vardy won")
else:
    print("It was a draw")
