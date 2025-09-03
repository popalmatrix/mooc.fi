# The goal is to determine if a person is of age based on a simple rule.

# 1. Define the age of maturity.
# We create a variable called `adult_age` and assign it the value 18.
# Using a variable makes the code easy to update if the legal age changes.
adult_age = 18

# 2. Get the user's age.
# The `input()` function prompts the user with the given text.
# It returns the user's response as a string.
# We use `int()` to convert that string into a number (an integer)
# so we can compare it to our `adult_age` variable.
# The result is stored in the `age` variable.
age = int(input("How old are you? "))

# 3. Use a conditional statement to check the age.
# The `if` statement checks if the `age` is greater than or equal to (`>=`) the `adult_age`.
if age >= adult_age:
    # If the condition is True, this code block runs.
    # It prints a message confirming the user is of age.
    print("You are of age!")
else:
    # If the `if` condition is False, the code in the `else` block runs instead.
    # This prints a message for users who are not yet of age.
    print("You are not of age!")
