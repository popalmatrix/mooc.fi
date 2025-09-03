# The goal is to compare two numbers provided by a user and print the greater one,
# or a special message if they are equal.

# --- Part 1: Ask for two integer numbers. ---
# First, we use the `input()` function to ask the user for the first number.
# The `input()` function always returns a string (text), so we use `int()` to
# convert the text into a whole number (an integer).
# This is crucial because you can't perform mathematical comparisons on strings.
number1 = int(input("Please type in the first number: "))

# We do the exact same thing for the second number.
# The result is stored in a separate variable, `number2`.
number2 = int(input("Please type in another number: "))

# --- Part 2: Compare the numbers and print the correct message. ---
# We use an `if`, `elif`, and `else` structure to handle all possible conditions.
# This structure ensures that only one of the code blocks will ever run.

# First, we check if the first number is greater than the second number.
if number1 > number2:
    # If this condition is true, we print a formatted string.
    # The `f` before the string allows us to embed the value of `number1` directly
    # into the message using curly braces `{}`.
    print(f"The greater number was {number1}")

# `elif` stands for "else if." This block is only checked if the first `if`
# condition was false. It checks if the second number is greater than the first.
elif number2 > number1:
    # If this condition is true, we print the second number.
    print(f"The greater number was {number2}")

# The `else` block is a catch-all. It runs only if ALL the previous conditions
# (`if` and `elif`) were false.
# The only remaining possibility is that the numbers are equal.
else:
    # We print a special message to handle this case.
    print("The numbers are equal!")
