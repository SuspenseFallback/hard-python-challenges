remaining_health = int(input("How much health remains since last attack? "))
time_since_last_attack = int(input("How many seconds passed since last attack? "))


time = 5 - time_since_last_attack if time_since_last_attack < 5 else 0
new_health = remaining_health

while new_health < 500:
    time += 1
    new_health += 75

print(time)
