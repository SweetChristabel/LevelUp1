# Fix the program
pointsin = int(input("How many points are on your card? "))
if pointsin < 100:
    pointsout = pointsin * 1.1
    print("Your bonus is 10 %")

if pointsin >= 100:
    pointsout = pointsin * 1.15
    print("Your bonus is 15 %")

print("You now have", pointsout, "points")