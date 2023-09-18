num_of_sweets = int(input("How many sweets are needed? "))
num_of_students = int(input("How many students want candy? "))
cost_of_sweets = float(input("What is the total cost of all the sweets? "))

sweets_per_student = num_of_sweets // num_of_students
remainder = num_of_sweets % num_of_students
share_per_student = "{:.2f}".format(cost_of_sweets / num_of_sweets)

print("Each student need to pay $" + str(share_per_student))
print("Each student receives", sweets_per_student, "sweets")
print("There will be", remainder, "candy remaining")
