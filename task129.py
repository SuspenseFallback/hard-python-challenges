male = 0
female = 0

while True:
    gender = input("Male, female, or quit? ").lower()

    while gender != "male" and gender != "female" and gender != "quit":
        print("Wrong option")
        gender = input("Male, female, or quit? ")

    if gender == "female":
        female += 1

    if gender == "male":
        male += 1

    if gender == "quit":
        break

print(male, "males")
print(female, "females")
