singer_name = input("Enter the name of your favorite singer: ")
characters = int(input("How many characters do you want to see? "))

nameLength = len(singer_name)

if characters > nameLength:
    print("Error")
else:
    print(singer_name[0:characters])
