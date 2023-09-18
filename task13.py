num_of_apples = int(input("How many apples do you want? "))
shared = int(input("How many people will you share the apples with? "))

equal_dividend = num_of_apples // shared
remainder = num_of_apples % equal_dividend

print(remainder, "apple(s) will remain.")
