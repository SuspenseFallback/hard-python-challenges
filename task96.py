positive = 0
negative = 0
severe = 0
mild = 0

num_of_patients = int(input("How many patients need to be tested? "))

for i in range(num_of_patients):
    print("\n", "-" * 30, "\n")
    print("Patient", i + 1)

    fever = input("Do you have a fever? (y/n) ").lower()
    dry_cough = input("Do you have a dry cough? (y/n) ").lower()

    fever = True if fever == "y" else False
    dry_cough = True if dry_cough == "y" else False

    if fever and dry_cough:
        print("You have tested positive for the virus")
        positive += 1

        severity = input("Are the symptoms mild or severe? ").lower()

        while severity != "mild" and severity != "severe":
            print("Please enter a valid entry")
            severity = input("Are the symptoms mild or severe? ").lower()

        if severity == "mild":
            mild += 1
        else:
            severe += 1
    else:
        print("You have tested negative for the virus")

print("\n", "-" * 30, "\n")
print("Results: \n")

print("Positive:", positive)
print("Negative:", negative)
print("Mild symptoms:", mild)
print("Severe symptoms:", severe)
