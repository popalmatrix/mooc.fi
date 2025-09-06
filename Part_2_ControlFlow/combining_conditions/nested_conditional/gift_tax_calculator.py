# The program prompts the user for the value of the gift.
# The `input()` function is used to get the user's input, which is a string.
# `int()` is then used to convert the string to an integer so we can perform calculations.
value = int(input("Value of gift: "))

# The program uses a series of `if...elif...else` statements to determine the correct tax bracket.
# It checks the value of the gift against the ranges provided in the tax table.

# If the gift value is less than 5000, no tax is owed.
if value < 5000:
    print("No tax!")

# If the gift is between 5,000 and 25,000 euros, this block calculates the tax.
# `elif` stands for "else if" and is used to check the next condition if the first one was false.
# The calculation follows the formula: Tax at lower limit + (amount exceeding lower limit) * tax rate.
elif value <= 25000:
    tax = 100 + (value - 5000) * 0.08
    # The `f-string` is used to format the output. `{tax:.1f}` formats the tax amount to one decimal place.
    print(f"Amount of tax: {tax:.1f} euros")

# If the gift is between 25,000 and 55,000 euros.
elif value <= 55000:
    tax = 1700 + (value - 25000) * 0.10
    print(f"Amount of tax: {tax:.1f} euros")

# If the gift is between 55,000 and 200,000 euros.
elif value <= 200000:
    tax = 4700 + (value - 55000) * 0.12
    print(f"Amount of tax: {tax:.1f} euros")

# If the gift is between 200,000 and 1,000,000 euros.
elif value <= 1000000:
    tax = 22100 + (value - 200000) * 0.15
    print(f"Amount of tax: {tax:.1f} euros")

# This is the final `else` block, which handles any gift value over 1,000,000 euros.
# It's the "catch-all" for any value that didn't fit into the previous conditions.
else:
    tax = 142100 + (value - 1000000) * 0.17
    print(f"Amount of tax: {tax:.1f} euros")
