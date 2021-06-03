speed = float(input("Whats is the speed? "))
if speed <=70:
        print("Ok")
else:
    points = str((speed - 70) // 5)
    print("Points: " + points)
    if float(points) >=12:
        print("License suspended")