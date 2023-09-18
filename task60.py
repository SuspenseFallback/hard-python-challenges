school = input("What school do you go to? ")
first_or_last = input("Do you want to see the first or last letter? ").lower()

if first_or_last == "first":
    print(school[0])
elif first_or_last == "last":
    print(school[-1])
else:
    print("Wrong option")
