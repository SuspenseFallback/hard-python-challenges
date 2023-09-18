num_of_toilet_rolls = int(input("How many toilet rolls are you going to buy? "))

while num_of_toilet_rolls > 3:
    num_of_toilet_rolls = int(input("How many toilet rolls are you going to buy? "))

if num_of_toilet_rolls == 1:
    print("The price is $2")
elif num_of_toilet_rolls == 2:
    print("The price is $6")
else:
    print("The price is $12")
