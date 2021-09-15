#This program calculates the end of year bonus a customer receives on their loyalty card

points = int(input("How many points are on your card? "))

if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

elif points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")