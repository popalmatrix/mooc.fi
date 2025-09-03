# The goal is to ask for a user's age and respond differently
# based on whether the age is plausible.

# 1. Ask the user for their age.
# The `input()` function gets the user's response as a string.
# We convert it to an integer using `int()` so we can use it for numerical comparisons.
age = int(input("What is your age? "))

# 2. Use conditional logic to check for plausibility.
# We use an `if-elif-else` structure to check for three different scenarios:
# 1) The age is less than 0 (not a valid human age).
# 2) The age is between 0 and 4 (too young to plausibly type).
# 3) The age is 5 or older (a plausible age).

# First, check for ages that are not possible for a human.
# This condition covers all negative numbers.
if age < 0:
    print("That must be a mistake")

# Next, check for ages that are technically possible but not plausible for typing.
# This `elif` block will only be checked if the first `if` condition was false.
elif age >= 0 and age < 5:
    print("I suspect you can't write quite yet...")

# Finally, for all other ages that are 5 or older, we assume they are plausible.
# The `else` block acts as a catch-all for all other cases.
else:
    print(f"Ok, you're {age} years old")
