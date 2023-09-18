traffic_light_color = input("What color is the traffic light? ").lower()

if traffic_light_color == "red":
    print("STOP")
elif traffic_light_color == "yellow":
    print("GET READY")
elif traffic_light_color == "green":
    print("GO")
else:
    print("Error")
