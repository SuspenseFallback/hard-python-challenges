num_of_attempts = int(input("How many attempts? "))

total = 0
for i in range(num_of_attempts):
    time = int(input("How many long did it take in seconds to complete it? "))
    total += time

print("The total time is:", total)
print("The average time is:", total / num_of_attempts)
