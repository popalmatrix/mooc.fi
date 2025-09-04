# The goal is to check for divisibility by 3, 5, or both.

# 1. Ask the user for an integer number.
# We use the `input()` function to get a string from the user.
# Then, we use `int()` to convert the string into a number.
integer_number = int(input("Number: "))

# 2. Use a conditional statement to check for divisibility.
# The order of the conditions is crucial here. We must check for the most
# specific condition (divisible by both 3 and 5) first.

# Check if the number is divisible by both 3 and 5.
# The modulo operator (%) gives the remainder of a division.
# If `number % 3 == 0` AND `number % 5 == 0`, it means the number is divisible by both.
if integer_number % 3 == 0 and integer_number % 5 == 0:
    print("FizzBuzz")

# If the first condition is not met, check if the number is divisible by 3.
elif integer_number % 3 == 0:
    print("Fizz")

# If the first two conditions are not met, check if the number is divisible by 5.
elif integer_number % 5 == 0:
    print("Buzz")

# If none of the above conditions are true, we don't need to print anything.
# This else block is optional because the problem doesn't specify an output for
# numbers not divisible by 3 or 5, but it can be added for clarity.
# else:
#     pass
