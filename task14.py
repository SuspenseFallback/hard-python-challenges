home_team = input("What is the name of the home team? ")
away_team = input("What is the name of the opponent team? ")

home_team_goals = int(input("How many goals did the " + home_team + " score? "))
away_team_goals = int(input("How many goals did the " + away_team + " score? "))

print("Scorecard: ", home_team_goals, "-", away_team_goals)
print("Goal difference for the home team:", home_team_goals - away_team_goals)
