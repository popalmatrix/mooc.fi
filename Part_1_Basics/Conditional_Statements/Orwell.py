# Program: Check for 1984 (Teachable Version)

# Step 1: Ask the user for input
# The user might type extra spaces, e.g., "   1984   "
# Using .split() removes all spaces and "".join(...) combines the parts back
# Then we convert it to an integer using int()
user_input = "".join(input("Please type in a number: ").split())
number = int(user_input)

# Step 2: Check if the number is exactly 1984
# If the condition is True, print "Orwell"
if number == 1984:
    print("Orwell")

# Step 3: If the number is not 1984, do nothing
# No else statement is needed because "do nothing" is the default behavior
