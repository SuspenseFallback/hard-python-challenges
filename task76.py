negatives = int(input("How many negatives did you get? "))

if negatives == 1:
    for i in range(10):
        print("Do your homework now")
elif negatives == 2:
    for i in range(50):
        print("Reminder to do your homework")
elif negatives == 3:
    for i in range(100):
        print("If you don't do homework, you will get detention")
else:
    for i in range(500):
        print("You have detention")
