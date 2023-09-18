positives = 0
negatives = 0
zero = 0
even = 0
odd = 0

for i in range(5):
    num = int(input("Enter a number: "))

    if num == 0:
        zero += 1
    elif num > 0:
        positives += 1
    else:
        negatives += 1

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Positives:", positives)
print("Negatives:", negatives)
print("Zero:", zero)
print("Even:", even)
print("Odd:", odd)
