remaining_health = int(input("How much health remains since last attack? "))
time_since_last_attack = int(input("How many seconds passes since last attack? "))

new_health = 0

if time_since_last_attack <= 5:
    new_health = remaining_health
else:
    new_health = remaining_health + ((time_since_last_attack - 5) * 5)

print("\n", "-" * 30, "\n")
print("Current health: ", new_health)
print("Current percentage of health: ", str((new_health / 500) * 100) + "%")
