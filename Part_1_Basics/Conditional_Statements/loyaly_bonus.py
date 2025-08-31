# Original program issues:
# 1. Used two separate if statements instead of if-else, which is less clear and could lead to logical errors.
# 2. Did not explain what *= does.
# 3. Points could become a float without rounding in the output, making it less readable.

# Fixed and teachable version:

# Ask the user for points on their card
points = int(input("How many points are on your card? "))

# Check the bonus according to points
if points < 100:
    # *= is a shorthand operator: points *= 1.1 is the same as points = points * 1.1
    # Here, it adds a 10% bonus to the points
    points *= 1.1  
    print("Your bonus is 10%")
else:
    # For points 100 or more, add a 15% bonus
    points *= 1.15  # same as points = points * 1.15
    print("Your bonus is 15%")

# Print the final points
# round(points, 2) rounds the number to 2 decimal places for neat output
print("You now have", round(points, 2), "points")
