num_of_hand_sanitizers = int(input("How many hand sanitizers? "))

while num_of_hand_sanitizers > 1:
    print("Can only buy maximum of 1 hand sanitizer")
    num_of_hand_sanitizers = int(input("How many hand sanitizers? "))

num_of_toilet_rolls = int(input("How many toilet rolls? "))

while num_of_toilet_rolls > 1:
    print("Can only buy maximum of 1 toilet roll")
    num_of_toilet_rolls = int(input("How many toilet rolls? "))

overall_cost = float(input("What is your overall cost? "))

more_than_2_of_same_item = input("Do you have more than 2 of the same item? (y/n) ")
more_than_2_of_same_item = True if more_than_2_of_same_item == "y" else False

while more_than_2_of_same_item:
    print("Can only buy maximum of 2 of the same item")
    more_than_2_of_same_item = input("Do you have more than 2 of the same item? (y/n) ")
    more_than_2_of_same_item = True if more_than_2_of_same_item == "y" else False

print("Your order has been accepted.")
