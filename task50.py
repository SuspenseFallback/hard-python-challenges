game = input("What is the name of the game? ")

if game == "Guild Wars":
    print("Old but good!")
else:
    year = int(input("What year was the game released? "))

    if year > 2010:
        print("Pretty decent!")
    else:
        print("Old but decent!")
