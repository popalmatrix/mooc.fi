# The goal is to get a user's score and output the corresponding grade.

# 1. Ask the user for the points they received.
# The `input()` function prompts the user with the text in parentheses and
# returns whatever the user types as a string.
# We use `int()` to convert this string into a number (an integer), which is
# necessary for the numerical comparisons we will make.
# The converted number is then stored in the `received_points` variable.
received_points = int(input("How many points [0-100]: "))

# 2. Use a series of `if` and `elif` statements to determine the grade.
# This structure is a chain of conditions. Python checks each condition in order,
# and if one is true, it executes that code block and skips all the others.

# First, we handle the "impossible" scores, which are outside the valid range.
# We use the logical operator `or` to check if the score is either less than 0 OR greater than 100.
if received_points < 0 or received_points > 100:
    print("Grade: impossible!")

# Next, we check for a failing grade. This block is only checked if the score
# was NOT impossible. So, if we reach this point, the score is already between 0 and 100.
elif received_points < 50:
    print("Grade: fail")

# Then, we check for a grade of 1. Because the previous `elif` was false,
# we already know the score is 50 or greater, so we only need to check the upper bound.
elif received_points < 60:
    print("Grade: 1")

# We continue this pattern for grades 2, 3, and 4.
elif received_points < 70:
    print("Grade: 2")
elif received_points < 80:
    print("Grade: 3")
elif received_points < 90:
    print("Grade: 4")

# Finally, the `else` block acts as a catch-all. If the program reaches this point,
# it means the score was not "impossible," not "fail," and not grades 1, 2, 3, or 4.
# The only remaining possibility is that the score is between 90 and 100 (inclusive),
# which corresponds to a grade of 5.
else:
    print("Grade: 5")
